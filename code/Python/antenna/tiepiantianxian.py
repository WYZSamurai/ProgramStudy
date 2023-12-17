# 导入数学模块
import math


def func():
    # 输入工作频率（单位：GHz）
    f = float(input("请输入工作频率（单位：GHz）："))
    # 输入介质的相对介电常数
    er = float(input("请输入介质的相对介电常数："))
    # 输入介质的厚度（单位：mm）
    h = float(input("请输入介质的厚度（单位：mm）："))

    # 计算贴片宽度（单位：mm）
    W = 150 / (f * math.sqrt((er + 1) / 2))
    # 计算有效介电常数
    eeff = (er + 1) / 2 + (er - 1) / 2 * (1 + 12 * h / W)**(-0.5)
    # 计算长度延伸（单位：mm）
    DL = 0.412 * h * (eeff + 0.3) * (W / h + 0.264) / \
        ((eeff - 0.258) * (W / h + 0.8))
    # 计算贴片长度（单位：mm）
    L = 150 / (f * math.sqrt(eeff)) - 2 * DL
    # 输出贴片尺寸
    print("贴片宽度为 {:.3f} mm".format(W))
    print("贴片长度为 {:.3f} mm".format(L))
    return (W, L)


if __name__ == "__main__":
    func()
