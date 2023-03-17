use std::io::*;

fn fio() -> (Vec<i32>, i32) {
    let mut n = String::new();
    stdin().read_line(&mut n).unwrap();
    let mut n: i32 = n.trim().parse().unwrap();
    let n1 = n;
    let mut v: Vec<i32> = Vec::new();
    while n > 0 {
        let mut v1 = String::new();
        stdin().read_line(&mut v1).unwrap();
        v.push(v1.trim().parse().unwrap());
        n -= 1;
    }
    (v, n1)
}

fn main() {
    let (mut v, n) = fio();
    let mut n = String::new();
    stdin().read_line(&mut n).unwrap();
    let n: i32 = n.trim().parse().unwrap();
    fun(&mut v, n);
}

fn fun(v: &mut Vec<i32>, n: i32) -> (i32, i32) {
    for &mut i in v {
        let tar = n - i;
    }
    (1, 2)
}
