using Godot;
using System;

public partial class main : Node
{
    // Called when the node enters the scene tree for the first time.
    public override void _Ready()
    {
        GD.Print("main准备就绪");
    }

    // Called every frame. 'delta' is the elapsed time since the previous frame.
    public override void _Process(double delta)
    {
    }
}