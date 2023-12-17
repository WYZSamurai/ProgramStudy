use std::io::*;

fn fun(n: &i32) -> i32 {
    if n % 2 == 0 {
        n / 2
    } else {
        (3 * n + 1) / 2
    }
}

fn main() {
    let mut s = String::new();
    stdin().read_line(&mut s).unwrap();
    let mut n = 0;
    for i in s.trim().split(' ') {
        n = i.parse().unwrap();
    }
    let mut c = 0;
    while n != 1 {
        n = fun(&n);
        c += 1;
    }
    println!("{}", c);
}
