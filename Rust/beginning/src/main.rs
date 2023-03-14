use std::io::*;
pub fn nsstring() -> Vec<Vec<String>> {
    // 输入n
    let mut n = String::new();
    stdin().read_line(&mut n).unwrap();
    let mut n1 = 0;
    for i in n.trim().split(" ") {
        n1 = i.parse().unwrap();
    }
    // 输入字符串
    let mut ct: Vec<Vec<String>> = Vec::new();
    while n1 > 0 {
        let mut ct1: Vec<String> = Vec::new();
        let mut s = String::new();
        stdin().read_line(&mut s).unwrap();
        for i in s.trim().split(" ") {
            ct1.push(i.to_string());
        }
        ct.push(ct1);
        n1 -= 1;
    }
    ct
}

fn main() {
    let s = nsstring();
    // println!("{:?}", s);
    let mut s1 = s.clone();
}
