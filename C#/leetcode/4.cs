public class Solution
{
    public double FindMedianSortedArrays(int[] nums1, int[] nums2)
    {
        // 偶数是len/2-1，奇数是len/2
        var len = nums1.Length + nums2.Length;

        return 0.0;
    }
    static void L4()
    {
        var s = Console.ReadLine();
        List<Int32> v = new List<int>();
        foreach (var i in s!.Trim().Split(' '))
        {
            v.Add(Int32.Parse(i));
        }
        var a = v.ToArray();
        v.Clear();
        s = Console.ReadLine();
        foreach (var i in s!.Split(' '))
        {
            v.Add(Int32.Parse(i));
        }
        var b = v.ToArray();

        Solution sol = new Solution();
        var res = sol.FindMedianSortedArrays(a, b);
        Console.WriteLine("{0}", res);
    }
}