use std::collections::HashMap;
use std::io::*;

fn main() {
    let k = ioline();
    let mut map: HashMap<i32, i32> = HashMap::new();
    for mut i in k {
        while i != 1 {
            i = fun(i);
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
