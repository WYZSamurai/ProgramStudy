use std::io::*;

fn main() {
    //完成输入功能
    let k = ioline();
    //备份原数组
    let mut k1 = k.clone();
    // 创建被覆盖数组
    let mut v: Vec<i32> = Vec::new();
    for mut i in k {
        while i != 1 {
            i = fun(i);
            // 若i在输入的数中则存进数组中
            if k1.contains(&i) {
                v.push(i);
            }
        }
    }
    // 将原数组中被覆盖数除去并按从大到小排序
    k1.retain(|x| !v.contains(x));
    k1.sort_unstable_by(|x, y| y.cmp(&x));
    //输出结果
    for i in k1.iter() {
        if Some(i) != k1.last() {
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
// 核心功能
fn fun(n: i32) -> i32 {
    if n % 2 == 0 {
        n / 2
    } else {
        (3 * n + 1) / 2
    }
}
////////////////////////////////HashMap解法
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
