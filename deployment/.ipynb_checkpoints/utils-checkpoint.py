import os
import sys
import json
import torch
import numpy as np
from tqdm import tqdm
from sklearn import metrics
from azureml.pipeline.wrapper.dsl.module import OutputDirectory
from azureml.core import Run

torch.manual_seed(1)
torch.cuda.manual_seed_all(1)
np.random.seed(1)


def train(model,
          trained_model_dir: OutputDirectory(type='AnyDirectory'),
          train_iter,
          dev_iter=None,
          epochs=20,
          learning_rate=0.0001,
          stop_patience=3,
          device=None):
    if device is None:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    model.train()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    model.to(device)
    loss = torch.nn.CrossEntropyLoss()

    min_loss_epoch = (None, None)
    stop_flag = False

    model_name = model._get_name()
    tip_str = f"\n{model_name} start training....."
    print(tip_str)
    # for logging
    run = Run.get_context()
    for epoch in range(epochs):
        loss_value_list = []
        total_iter = len(train_iter)
        for i, (x_batch, y_batch) in enumerate(train_iter):
            x_batch = torch.LongTensor(x_batch).to(device)
            y_batch = torch.LongTensor(y_batch).to(device)

            outputs = model(x_batch)
            optimizer.zero_grad()
            loss_value = loss(outputs, y_batch)
            loss_value.backward()
            optimizer.step()
            # for metrics
            run.log(name='CrossEntropyLoss', value=np.mean(loss_value_list))
            loss_value_list.append(loss_value.cpu().data.numpy())
            str_ = f"{model_name} epoch:{epoch + 1}/{epochs} step:{i + 1}/{total_iter} mean_loss:{np.mean(loss_value_list): .4f}"
            sys.stdout.write('\r' + str_)
            sys.stdout.flush()

            if (i + 1) == total_iter and dev_iter is not None:
                loss_, acc_, prec_, recall_, f1_ = eval(model, dev_iter, device)
                str_ = f" validation loss:{loss_:.4f}  acc:{acc_:.4f}"
                sys.stdout.write(str_)
                sys.stdout.flush()
                print()

                model.train()

                if (min_loss_epoch[0] is None) or (min_loss_epoch[0] > loss_):
                    min_loss_epoch = (loss_, epoch)
                    os.makedirs(trained_model_dir, exist_ok=True)
                    path = trained_model_dir
                    torch.save(obj=model, f=path)
                else:
                    if (epoch - min_loss_epoch[1]) >= stop_patience:
                        stop_flag = True
                        break

        if stop_flag is True:
            break


def test(model, test_iter=None, device=None):
    run = Run.get_context()
    loss_, acc_, prec_, recall_, f1_ = eval(model, test_iter, device)
    # for metrics
    run.log(name='CrossEntropyLoss', value=loss_)
    run.log(name='Accuracy', value=acc_)
    run.log(name='Precision', value=prec_)
    run.log(name='Recall', value=recall_)
    run.log(name='F1', value=f1_)
    str_ = f"test acc:{acc_:.4f}"
    sys.stdout.write(str_)
    sys.stdout.flush()
    return acc_


def eval(model, data_iter, device):
    model.eval()
    with torch.no_grad():
        acc_list = []
        precision_list = []
        recall_list = []
        f1_list = []
        loss_list = []

        for x, y in data_iter:
            dev_x_ = torch.LongTensor(x).to(device)
            dev_y_ = torch.LongTensor(y).to(device)
            outputs = model(dev_x_)
            p_ = torch.max(outputs.data, 1)[1].cpu().numpy()
            acc_ = metrics.accuracy_score(y, p_)
            precision_ = metrics.precision_score(y, p_, average='micro')
            recall_ = metrics.recall_score(y, p_, average='micro')
            f1_ = metrics.f1_score(y, p_, average='micro')
            loss_ = torch.nn.CrossEntropyLoss()(outputs, dev_y_)
            acc_list.append(acc_)
            precision_list.append(precision_)
            recall_list.append(recall_)
            f1_list.append(f1_)
            loss_list.append(loss_.cpu().data.numpy())
        return np.mean(loss_list), np.mean(acc_list), np.mean(precision_list), np.mean(recall_list), np.mean(f1_list)


def predict(model, data_iter, device):
    model.eval()
    # for metrics
    run = Run.get_context()
    p_ = 0
    for x, y in data_iter:
        dev_x_ = torch.LongTensor(x).to(device)
        outputs = model(dev_x_)
        p_ = torch.max(outputs.data, 0)[1].cpu()
        run.log(name='Prediction Result', value=get_classs_reverse()[int(p_)])
    return get_classs_reverse()[int(p_)]


def get_vocab(char2index_dir):
    c2i = json.load(open(char2index_dir, 'r', encoding='utf-8'))
    return c2i


def get_classs():
    res = {'finance': 0,
           'realty': 1,
           'stocks': 2,
           'education': 3,
           'science': 4,
           'society': 5,
           'politics': 6,
           'sports': 7,
           'game': 8,
           'entertainment': 9}
    return res


def get_classs_reverse():
    res = {0: 'finance',
           1: 'realty',
           2: 'stocks',
           3: 'education',
           4: 'science',
           5: 'society',
           6: 'politics',
           7: 'sports',
           8: 'game',
           9: 'entertainment'}
    return res


def shuffle_samples(samples):
    samples = np.array(samples)
    shffle_index = np.arange(len(samples))
    np.random.shuffle(shffle_index)
    samples = samples[shffle_index]
    return samples


def load_dataset(file_path='', max_len=38, char2index_dir=''):
    c2i = get_vocab(char2index_dir)
    pad_id = c2i.get('[PAD]', 0)
    samples = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            texts = f.read().split("\n")
            texts = [item.strip() for item in texts if len(item) > 0]
        for line in tqdm(texts, desc="character to index"):
            line_s = line.split('\t')
            if len(line_s) < 2:
                continue
            context, label = line_s[0], line_s[1]
            line_data = ([c2i.get(c, 1) for c in context]) + [pad_id] * (max_len - len(context))
            line_data = line_data[:max_len]
            samples.append((line_data, int(label)))
    # for prediction
    else:
        context = file_path
        line_data = ([c2i.get(c, 1) for c in context]) + [pad_id] * (max_len - len(context))
        line_data = line_data[:max_len]
        samples.append((line_data, 0))  # fake label

    samples = np.array(samples)

    return samples


class DataIter(object):
    def __init__(self, samples, batch_size=32, shuffle=True):
        if shuffle:
            samples = shuffle_samples(samples)
        self.samples = samples
        self.batch_size = batch_size
        self.n_batches = len(samples) // self.batch_size
        self.residue = (len(samples) % self.n_batches != 0)
        self.index = 0

    def split_samples(self, sub_samples):
        b_x = [item[0] for item in sub_samples]
        b_y = [item[1] for item in sub_samples]
        return np.array(b_x), np.array(b_y)

    def __next__(self):
        if (self.index == self.n_batches) and (self.residue is True):
            sub_samples = self.samples[self.index * self.batch_size: len(self.samples)]
            self.index += 1
            return self.split_samples(sub_samples)
        elif self.index >= self.n_batches:
            self.index = 0
            raise StopIteration
        else:
            sub_samples = self.samples[self.index * self.batch_size: (self.index + 1) * self.batch_size]
            self.index += 1
            return self.split_samples(sub_samples)

    def __iter__(self):
        return self

    def __len__(self):
        if self.residue:
            return self.n_batches + 1
        else:
            return self.n_batches
