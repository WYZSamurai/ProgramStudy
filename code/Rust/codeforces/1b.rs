use std::io::*;
//输入一行，转为多个整数
fn cin() -> Vec<i32> {
    let mut s = String::new();
    stdin().read_line(&mut s).unwrap();
    let mut v: Vec<i32> = Vec::new();
    for i in s.trim().split(" ") {
        v.push(i.parse::<i32>().unwrap());
    }
    v
}

fn main() {
    let n = cin()[0];
    println!("{}", n);
    let a = 'A' as u8;
    let b = 'B' as u8;
    println!("{}", b - a);
}
