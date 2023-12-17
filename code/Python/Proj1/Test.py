import torch
import torch.nn as nn
import numpy as np


if __name__ == "__main__":
    lamda = torch.tensor(1.0)
    # 半波长
    d = lamda * 0.5
    pi = torch.tensor(np.pi)
    # 定义波数
    k = 2 * pi / lamda
    theta = torch.cos(torch.linspace(0, np.pi, 181, dtype=torch.float64))
    position = torch.linspace(0, 24 - 1, 24, dtype=torch.int64).reshape(24, 1)
    B = position * k * d * theta
    print(theta.shape)
