using Godot;
using System;

public partial class main : Node
{
    private void OnVisibleOnScreenNotifier2DScreenExited()
    {
        QueueFree();
    }

    public override void _Ready()
    {
        GD.Print("main准备就绪");
        // 获取动画节点
        var animatedSprite2D = GetNode<AnimatedSprite2D>("AnimatedSprite2D");
        // 获取所有的动画名称并汇入列表
        string[] mobTypes = animatedSprite2D.SpriteFrames.GetAnimationNames();
        // 随机播放动画
        animatedSprite2D.Play(mobTypes[GD.Randi() % mobTypes.Length]);
    }

    public override void _Process(double delta)
    {
    }
}
