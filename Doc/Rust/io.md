# 输入输出
导入库特定对象
```rust
use std::io::{stdin, BufRead};
```
或全导入
```rust
use std::io::*;
```
### 单行输入
```rust
let mut input = String::new();
stdin().read_line(&mut input).unwrap();
```
### 字符串分割
```rust
let a: Vec<&str> = input.trim().split(' ').collect(); //先存到数组中再读
for i in a {
    println!("{i}");
}
println!("----------------");
//跳过存储步骤
for i in input.trim().split(" ") {
    println!("{i}");
}
```
### 循环输入（crtl + c停止）
```rust
for line in stdin().lock().lines() {
    println!("{}", line.unwrap());
}
```
### 整型转String
```rust
let val = 5;
let val_to_str = val.to_string();
println!("{}", val_to_str);
```
### String->整型
```rust
let str_to_val = val_to_str.parse::<i32>().unwrap();
println!("{}", str_to_val);
```
### 示例
#### 给定一个n，输入长度为n的二维数组
```rust
let mut v: Vec<Vec<i32>> = Vec::new();
let mut n = String::new();
stdin().read_line(&mut n).unwrap();
let n = n.trim().parse::<i32>().unwrap();
for _i in 0..n {
    let mut s = String::new();
    stdin().read_line(&mut s).unwrap();
    let mut v1: Vec<i32> = Vec::new();
    for j in s.trim().split(" ") {
        v1.push(j.parse::<i32>().unwrap());
    }
    v.push(v1);
}
```
#### 循环输入二维数组
```rust
let mut v: Vec<Vec<i32>> = Vec::new();
for line in stdin().lock().lines() {
    let s = line.unwrap();
    let mut v1: Vec<i32> = Vec::new();
    for i in s.trim().split(" ") {
        v1.push(i.parse::<i32>().unwrap());
    }
    v.push(v1);
}
```