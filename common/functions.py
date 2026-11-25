import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def softmax(a):
    # axis=-1: 最後の軸（1枚分の10個）ごとに計算する。1次元でも2次元(バッチ)でも動く
    c = np.max(a, axis=-1, keepdims=True)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a, axis=-1, keepdims=True)
    y = exp_a / sum_exp_a

    return y


def sum_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)


def cross_entropy_error(y, t):
    delta = 1e-7 
    return -np.sum(t * np.log(y + delta))
    

