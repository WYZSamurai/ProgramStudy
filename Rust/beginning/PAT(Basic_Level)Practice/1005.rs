use std::io::*;

fn main() {
    let k = ioline();
    let mut k1 = k.clone();
    let mut v: Vec<i32> = Vec::new();
    for mut i in k {
        while i != 1 {
            i = fun(i);
            if k1.contains(&i) {
                v.push(i);
            }
        }
    }
    k1.retain(|x| !v.contains(x));
    k1.sort_unstable_by(|x, y| y.cmp(&x));
    for i in k1.iter() {
        if Some(i) != k1.last() {
            print!("{} ", i);
        } else {
            print!("{}", i);
        }
    }
}

fn ioline() -> Vec<i32> {
    let mut input: String = String::new();
    stdin().read_line(&mut input).unwrap();
    input.clear();
    stdin().read_line(&mut input).unwrap();
    let mut v: Vec<i32> = Vec::new();
    for i in input.trim().split(" ") {
        v.push(i.to_string().parse().unwrap());
    }
    v
}

fn fun(n: i32) -> i32 {
    if n % 2 == 0 {
        n / 2
    } else {
        (3 * n + 1) / 2
    }
}
