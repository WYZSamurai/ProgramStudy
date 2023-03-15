use std::io::*;

fn fio() -> (Vec<Vec<String>>, usize) {
    let mut n = String::new();
    stdin().read_line(&mut n).unwrap();
    let mut n: usize = n.trim().parse().unwrap();
    let n1 = n;
    let mut v: Vec<Vec<String>> = Vec::new();
    while n > 0 {
        let mut v1: Vec<String> = Vec::new();
        let mut v3 = String::new();
        stdin().read_line(&mut v3).unwrap();
        for i in v3.trim().split(" ") {
            v1.push(i.to_string());
        }
        v.push(v1);
        n -= 1;
    }
    (v, n1)
}

fn main() {
    let (mut v, n) = fio();
    sort_two(&mut v);
    println!("{} {}", v[0][0], v[0][1]);
    println!("{} {}", v[n - 1][0], v[n - 1][1]);
}

fn sort_two(v: &mut Vec<Vec<String>>) {
    v.sort_unstable_by(|y, x| {
        x[2].parse::<i32>()
            .unwrap()
            .cmp(&y[2].parse::<i32>().unwrap())
    });
}
