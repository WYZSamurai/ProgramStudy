class Solution:
    # 容积为较低的一边为高，两边索引之差为低的面积
    def vol(self, i1, i2, h1, h2):
        h = 0
        if h1 < h2:
            h = h1
        else:
            h = h2
        d = abs(i1 - i2)
        return h * d

    def maxArea(self, height: list[int]) -> int:
        res: int = 0
        length = len(height)
        (i1, i2) = (0, 0)
        for i1 in range(0, length):
            for i2 in range(i1 + 1, length):
                tmp = Solution().vol(i1=i1, i2=i2, h1=height[i1], h2=height[i2])
                if res < tmp:
                    res = tmp

        return res


if __name__ == "__main__":
    num1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print("结果为：", Solution.maxArea(Solution, height=num1))
