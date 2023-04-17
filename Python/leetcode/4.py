class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        res = 0.0
        l1 = len(nums1)
        l2 = len(nums2)
        length = l1 + l2
        # 判断总长奇偶性
        pf = 1
        if length % 2 != 0:
            pf = 0
        if l1 > l2:
            Solution.findMedianSortedArrays(self, nums2, nums1)
        # 记录最近的两个数
        x1 = 0
        x2 = 0

        return res


if __name__ == "__main__":
    num1: list[int] = [1, 3]
    num2: list[int] = [2]
    print(Solution.findMedianSortedArrays(Solution, num1, num2))
