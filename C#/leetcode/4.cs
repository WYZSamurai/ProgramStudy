public class Solution
{
    public double FindMedianSortedArrays(int[] nums1, int[] nums2)
    {
        double res = 0.0;
        var l1 = nums1.Length;
        var l2 = nums2.Length;
        var len = l1 + l2;
        var cx = 0;
        var p1 = 0;
        var p2 = 0;
        var x1 = 0;
        var x2 = 0;

        if (l1 > l2)
        {
            res = new Solution().FindMedianSortedArrays(nums2, nums1);
            return res;
        }

        if (l1 == 0)
        {
            if (len % 2 == 0)
            {
                res = (float)(nums2[len / 2 - 1] + nums2[len / 2]) / (float)2;
            }
            else
            {
                res = (float)nums2[len / 2];
            }
            return res;
        }

        while (cx != len / 2 + 1)
        {
            x1 = x2;
            if (p1 < l1 && p2 < l2)
            {
                if (nums1[p1] < nums2[p2])
                {
                    x2 = nums1[p1];
                    p1 += 1;
                    cx += 1;
                    continue;
                }
                else
                {
                    x2 = nums2[p2];
                    p2 += 1;
                    cx += 1;
                    continue;
                }
            }
            if (p1 == l1)
            {
                x2 = nums2[p2];
                p2 += 1;
                cx += 1;
            }
            else if (p2 == l2)
            {
                x2 = nums1[p1];
                p1 += 1;
                cx += 1;
            }
        }

        if (len % 2 == 0)
        {
            res = (float)(x1 + x2) / (float)2;
        }
        else
        {
            res = (float)x2;
        }
        return res;
    }
    static void L4()
    {
        Int32[] n1 = { 1, 3 };
        Int32[] n2 = { 2 };
        Console.WriteLine("{0}", new Solution().FindMedianSortedArrays(n1, n2));
    }
}