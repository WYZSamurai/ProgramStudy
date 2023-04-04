use std::collections::HashMap;
use std::io::*;

fn main() {
    //完成输入功能
    let k = ioline();
    let mut map: HashMap<i32, i32> = HashMap::new();
    for i in k.iter() {
        let mut x = *i;
        while x != 1 {
            x = fun(&x);
            if !map.contains_key(&x) {
                map.insert(x, x);
            }
        }
    }
    let mut res: Vec<i32> = Vec::new();
    for i in k.iter() {
        if !map.contains_key(i) {
            res.push(*i);
        }
    }
    res.sort_unstable_by(|x, y| y.cmp(x));
    for i in res.iter() {
        if Some(i) != res.last() {
            print!("{} ", i);
        } else {
            print!("{}", i);
        }
    }
}
// 输入功能
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

fn fun(n: &i32) -> i32 {
    if n % 2 == 0 {
        n / 2
    } else {
        (3 * n + 1) / 2
    }
}
