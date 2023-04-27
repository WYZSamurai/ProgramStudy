using Godot;
using System;

public partial class player : Area2D
{
    // 自定义speed属性
    [Export]
    public int Speed = 400;

    // 自定义碰撞信号
    [Signal]
    public delegate void HitEventHandler();

    public Vector2 ScreenSize;

    public override void _Ready()
    {
        Console.WriteLine("player准备就绪");
        // 返回屏幕边界
        ScreenSize = GetViewportRect().Size;
    }

    public override void _Process(double delta)
    {
        // 创建速度向量，初始为0
        var velocity = Vector2.Zero; // The player's movement vector.

        // 检测按键
        if (Input.IsActionPressed("move_right"))
        {
            velocity.X += 1;
        }

        if (Input.IsActionPressed("move_left"))
        {
            velocity.X -= 1;
        }

        if (Input.IsActionPressed("move_down"))
        {
            velocity.Y += 1;
        }

        if (Input.IsActionPressed("move_up"))
        {
            velocity.Y -= 1;
        }

        // 获取动画节点
        var animatedSprite2D = GetNode<AnimatedSprite2D>("AnimatedSprite2D");

        // 若速度向量长度大于0，归一化速度向量，并播放动画
        if (velocity.Length() > 0)
        {
            velocity = velocity.Normalized() * Speed;
            animatedSprite2D.Play();
        }
        else
        {
            animatedSprite2D.Stop();
        }

        // 改变位置向量
        Position += velocity * (float)delta;
        Position = new Vector2(
            // 防止位置离开屏幕
            x: Mathf.Clamp(Position.X, 0, ScreenSize.X),
            y: Mathf.Clamp(Position.Y, 0, ScreenSize.Y)
        );

        // 先判断上下移动的动画
        if (velocity.Y != 0)
        {
            animatedSprite2D.Animation = "up";
            // 禁用水平移动动画
            animatedSprite2D.FlipH = false;
            // 反转垂直动画
            animatedSprite2D.FlipV = velocity.Y > 0;
        }
        else if (velocity.X != 0)
        {
            animatedSprite2D.Animation = "walk";
            animatedSprite2D.FlipH = velocity.X < 0;
        }
    }

    // 进入身体检测
    private void OnBodyEntered(PhysicsBody2D body)
    {
        // 当碰撞时隐藏身体
        Hide();
        // 进入身体后发出Hit信号
        EmitSignal(SignalName.Hit);
        // 当引擎处理碰撞过程中禁用区域碰撞形状会报错，需要用SetDeferred来等待直到安全后再禁用
        GetNode<CollisionShape2D>("CollisionShape2D").SetDeferred(CollisionShape2D.PropertyName.Disabled, true);
    }

    // 新一局时初始化玩家
    public void Start(Vector2 position)
    {
        Position = position;
        Show();
        GetNode<CollisionShape2D>("CollisionShape2D").Disabled = false;
    }
}
