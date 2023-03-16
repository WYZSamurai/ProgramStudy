use std::io::*;

fn fio() -> (Vec<String>, usize) {
    let mut n = String::new();
    stdin().read_line(&mut n).unwrap();
    let mut n: usize = n.trim().parse().unwrap();
    let n1 = n;
    let mut v: Vec<String> = Vec::new();
    while n > 0 {
        let mut v1 = String::new();
        stdin().read_line(&mut v1).unwrap();
        v.push(v1.trim().to_string());
        n -= 1;
    }
    (v, n1)
}

fn main() {
    fun();
}

fn fun() {
    let (v, n) = fio();
    for _i in 0..n {}
}
