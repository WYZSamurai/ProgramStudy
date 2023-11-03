import torch
import torch.nn as nn

# 设置设备
# 默认为cpu
device = "cpu"
# 判断cuda可用性
if torch.cuda.is_available():
    device = "cuda"
print("using "+device)


class Network(nn.Module):
    # 设置模型
    def __init__(self):
        # 初始化父类构造函数
        super().__init__()
        # 开始构建
        self.mlp = nn.Sequential(
            # 全连接层
            nn.Linear(181, 256),
            nn.PReLU(),
            nn.Linear(256, 128),
            nn.PReLU(),
            nn.Linear(128, 64),
            nn.PReLU(),
            nn.Linear(64, 48),
            nn.Sigmoid()
        )

    def forward(self, x):
        x = self.mlp(x)
        return x


if __name__ == "__main__":
    # pass

    # 验证ReLU函数
    m = nn.ReLU()
    input = torch.randn(2)
    print(input)
    output = m(input)
    print(output)

    # Model参数显示
    # model = Network().to(device=device)
    # print(model)
