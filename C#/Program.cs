public class Point
{
    public int X { get; }
    public int Y { get; }

    public Point(int x, int y) => (X, Y) = (x, y);
}

class Program
{
    static void Main()
    {
        // Console.WriteLine("Main");
        var P = new Point(1, 2);
        Console.WriteLine(P.X);
    }
}