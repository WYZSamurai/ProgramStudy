use std::io::stdin;
fn main() {
    let x = iom();
    let (a, b, c) = fun1(&x);
    let res = fun(&a, &b, &c);
    print!("{}", res);
}
// io功能
fn iom() -> i32 {
    let mut n: String = String::new();
    stdin().read_line(&mut n).unwrap();
    let n: i32 = n.trim().parse().unwrap();
    n
}
// 主功能
fn fun(a: &i32, b: &i32, c: &i32) -> String {
    let mut res = String::new();
    if *a != 0 {
        for _i in 0..*a {
            res.push_str("B");
        }
    }
    if *b != 0 {
        for _i in 0..*b {
            res.push_str("S");
        }
    }
    if *c != 0 {
        for i in 0..*c {
            res.push_str((i + 1).to_string().as_str());
        }
    }
    res
}
// 分解各个位数
fn fun1(x: &i32) -> (i32, i32, i32) {
    let a = x / 100;
    let b = (x - a * 100) / 10;
    let c = x - a * 100 - b * 10;
    (a, b, c)
}
