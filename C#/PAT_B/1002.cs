using System;
class p_1002
{
    static string[] list = { "ling", "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu" };
    static void p1002()
    {
        var s = Console.ReadLine();
        if (s != "")
        {
            var sum = 0;
            foreach (var i in s!)
            {
                sum += i - '0';
            }
            var res = sum.ToString();
            for (var i = 0; i < res.Length; i++)
            {
                if (i != res.Length - 1)
                {
                    Console.Write("{0} ", list[res[i] - '0']);
                }
                else
                {
                    Console.WriteLine("{0}", list[res[i] - '0']);
                }
            }
        }
    }
}