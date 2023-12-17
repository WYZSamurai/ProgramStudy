class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        res: float = 0.0
        l1 = len(nums1)
        l2 = len(nums2)
        leng = l1 + l2
        cx = 0
        p1 = 0
        p2 = 0
        x1 = 0
        x2 = 0

        if l1 > l2:
            res = Solution.findMedianSortedArrays(self, nums2, nums1)
            return res

        if l1 == 0:
            if leng % 2 == 0:
                res = float(nums2[leng // 2 - 1] + nums2[leng // 2]) / 2.0
            else:
                res = nums2[leng // 2]
            return res

        while cx != leng // 2 + 1:
            x1 = x2
            if p1 < l1 and p2 < l2:
                if nums1[p1] < nums2[p2]:
                    x2 = nums1[p1]
                    p1 += 1
                    cx += 1
                    continue
                else:
                    x2 = nums2[p2]
                    p2 += 1
                    cx += 1
                    continue
            if p1 == l1:
                x2 = nums2[p2]
                p2 += 1
                cx += 1
            elif p2 == l2:
                x2 = nums1[p1]
                p1 += 1
                cx += 1

        if leng % 2 == 0:
            res = float(x1 + x2) / 2.0
        else:
            res = float(x2)

        return res


if __name__ == "__main__":
    num1 = [1, 3]
    num2 = [2, 4]
    print("结果为：", Solution.findMedianSortedArrays(Solution, num1, num2))
