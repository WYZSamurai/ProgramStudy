using System;
class P_1014
{
    static string[] day = { "MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN" };
    static void Main()
    {
        // 输入4个变量
        var s1 = Console.ReadLine();
        var s2 = Console.ReadLine();
        var s3 = Console.ReadLine();
        var s4 = Console.ReadLine();
        var point = 0;
        for (var i = 0; i < s1!.Length; i += 1)
        {
            if (s1[i] == s2![i] && (s1[i] >= 'A' && s1[i] <= 'G'))
            {
                Console.Write("{0} ", day[s1[i] - 'A']);
                point = i;
                break;
            }
        }
        for (var i = point + 1; i < s1.Length; i += 1)
        {
            if (s1[i] == s2![i] && (s1[i] >= '0' && s1[i] <= '9'))
            {
                Console.Write("0{0}:", s1[i] - '0');
                break;
            }
            if (s1[i] == s2[i] && (s1[i] >= 'A' && s1[i] <= 'N'))
            {
                Console.Write("{0}:", s1[i] - 'A' + 10);
                break;
            }
        }
        var min = 0;
        for (var i = 0; i < s3!.Length; i += 1)
        {
            if ((s3[i] >= 'a' && s3[i] <= 'z') || (s3[i] >= 'A' && s3[i] <= 'Z'))
            {
                min += 1;
                if (s3[i] == s4![i])
                {
                    break;
                }
            }
        }
        if (min < 10)
        {
            Console.Write("0{0}", min);
        }
        else
        {
            Console.Write("{0}", min);
        }
    }
}