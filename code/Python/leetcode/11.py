class Solution:
    def maxArea(self, height: list[int]) -> int:
        res: int = 0
        length = len(height)
        (start, end) = (0, length - 1)
        while start < end:
            d = end - start
            h = 0
            if height[start] < height[end]:
                h = height[start]
                start += 1
            else:
                h = height[end]
                end -= 1
            tmp = d * h
            if res < tmp:
                res = tmp
        return res


if __name__ == "__main__":
    num1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print("结果为：", Solution.maxArea(Solution, height=num1), end="")
