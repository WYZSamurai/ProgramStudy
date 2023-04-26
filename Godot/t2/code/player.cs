using Godot;
using System;

public partial class player : Sprite2D
{
    // Called when the node enters the scene tree for the first time.
    public override void _Ready()
    {
        Console.WriteLine("player准备就绪");
    }

    // Called every frame. 'delta' is the elapsed time since the previous frame.
    public override void _Process(double delta)
    {
    }
}
