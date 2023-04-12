using System;
class Hello
{
    static void P1001()
    {
        var n = Int32.Parse(Console.ReadLine()!);
        var cx = 0;
        while (n != 1)
        {
            if (n % 2 == 0)
            {
                n = n / 2;
            }
            else
            {
                n = (3 * n + 1) / 2;
            }
            cx += 1;
        }
        Console.WriteLine("{0}", cx);
    }
}