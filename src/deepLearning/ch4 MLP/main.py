import math
import numpy as np
import torch
from torch import nn
from d2l import torch as d2l
import matplotlib.pyplot as plt
import os
import sys
loss = nn.MSELoss(reduction='none')       #均方误差损失函数,不对损失进行求和，保留每个样本的损失值


# 定义损失函数
def evaluate_loss(net, data_iter, loss):
    """评估给定数据集上模型的损失"""
    metric = d2l.Accumulator(2)           #损失的总和，样本数量
    for X, y in data_iter:
        out = net(X)
        y = y.reshape(out.shape)
        l = loss(out, y)
        metric.add(l.sum(), l.numel())    #将损失值和样本数量加入累加器中
    return metric[0]/metric[1]            #返回平均损失值

# 定义训练函数
def train(train_features, test_features, train_labels, test_labels, num_epoches = 400):
    
    input_shape = train_features.shape[-1]
    # 不设置偏置，因为已经在多项式中实现了它
    net = nn.Sequential(nn.Linear(input_shape, 1, bias=False))
    batch_size = min(10, train_labels.shape[0])
    train_iter = d2l.load_array((train_features, train_labels.reshape(-1, 1)), batch_size=batch_size)
    test_iter =  d2l.load_array((test_features, test_labels.reshape(-1, 1)), batch_size=batch_size, is_train=False)
    trainer = torch.optim.SGD(net.parameters(), lr = 0.01)
    animator = d2l.Animator(
        xlabel='epoch', ylabel='loss', yscale='log',
        xlim = [1, num_epoches], ylim = [1e-3, 1e2],
        legend=['train', 'test']
    )

    for epoch in range(num_epoches):
        d2l.train_epoch_ch3(net, train_iter, loss, trainer)
        with open(os.devnull, 'w') as fnull:
            sys.stdout = fnull
            if epoch == 0 or (epoch + 1) % 20 == 0:
                animator.add(
                    epoch+1, (evaluate_loss(net, train_iter, loss),
                            evaluate_loss(net, test_iter, loss)))
            sys.stdout = sys.__stdout__


    print('weight:', net[0].weight.data.numpy(), "test loss:", evaluate_loss(net, test_iter, loss))
    plt.show()    



if __name__ == "__main__":

    max_degree = 20
    n_train, n_test = 100, 100
    true_w = np.zeros(max_degree)
    # print(true_w.shape)
    true_w[0:4] = np.array([5, 1.2, -3.4, 5.6])
    features = np.random.normal(size = (n_train + n_test, 1))                      #features 200*1
    np.random.shuffle(features)
    poly_features = np.power(features, np.arange(max_degree).reshape(1, -1))       #poly_features 200*20
    for i in range(max_degree):
        poly_features[:, i] /= math.gamma(i+1)                                     #math.gamma(i) = (i-1)!
    # print(poly_features.shape, true_w.shape)
    labels = np.dot(poly_features, true_w)
    labels += np.random.normal(scale = 0.1, size = labels.shape)
    # 将numpt ndarray转换为tensor
    true_w, features, poly_features, labels = [
        torch.tensor(x, dtype=torch.float32) for x in [true_w, features, poly_features, labels]
    ]
    # 拟合三阶多项式函数
    # train(poly_features[:n_train, :4], poly_features[n_train:, :4], 
    #     labels[:n_train], labels[n_train:])
    # 拟合线性函数
    # train(poly_features[:n_train, :2], poly_features[n_train:, :2], labels[:n_train], labels[n_train:])
    # 拟合为高阶多项式函数
    train(poly_features[:n_train, :], poly_features[n_train:, :], 
        labels[:n_train], labels[n_train:])
