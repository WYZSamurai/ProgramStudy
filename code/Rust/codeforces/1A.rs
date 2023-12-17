use std::io::stdin;
//输入一行，转为多个整数
fn cin() -> Vec<i64> {
    let mut s = String::new();
    stdin().read_line(&mut s).unwrap();
    let mut v: Vec<i64> = Vec::new();
    for i in s.trim().split(" ") {
        v.push(i.parse::<i64>().unwrap());
    }
    v
}

fn main() {
    let v = cin();
    let n = v[0];
    let m = v[1];
    let a = v[2];
    let x = fun(n, a);
    let y = fun(m, a);
    println!("{}", x * y);
}

//判断各边的个数
fn fun(n: i64, a: i64) -> i64 {
    let mut x = n / a;
    let y = n % a;
    if y != 0 {
        x += 1
    }
    x
}
