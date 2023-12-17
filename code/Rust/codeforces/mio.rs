use std::io::*;

// 输入n，后跟n个二维数组
pub fn ni32() -> Vec<Vec<i32>> {
    let mut n = String::new();
    stdin().read_line(&mut n).unwrap();
    let mut n1 = 0;
    for i in n.trim().split(" ") {
        n1 = i.parse().unwrap();
    }
    let mut ct: Vec<Vec<i32>> = Vec::new();
    while n1 > 0 {
        let mut ct1: Vec<i32> = Vec::new();
        n.clear();
        stdin().read_line(&mut n).unwrap();
        for i in n.trim().split(" ") {
            ct1.push(i.parse().unwrap());
        }
        ct.push(ct1);
        n1 -= 1;
    }
    ct
}

// 循环输入二维数组
pub fn nni32() -> Vec<Vec<i32>> {
    let mut v: Vec<Vec<i32>> = Vec::new();
    for line in stdin().lock().lines() {
        let s = line.unwrap();
        let mut v1: Vec<i32> = Vec::new();
        for i in s.trim().split(" ") {
            v1.push(i.parse::<i32>().unwrap());
        }
        v.push(v1);
    }
    v
}
// // 输入n，后跟n个单一字符串
// pub fn nstring() -> Vec<String> {
//     // 输入n
//     let mut n = String::new();
//     stdin().read_line(&mut n).unwrap();
//     let mut n1 = 0;
//     for i in n.trim().split(" ") {
//         n1 = i.parse().unwrap();
//     }
//     // 输入字符串
//     let mut ct: Vec<String> = Vec::new();
//     while n1 > 0 {
//         let mut ct1 = String::new();
//         stdin().read_line(&mut ct1).unwrap();
//         ct1 = ct1.trim().to_string();
//         ct.push(ct1);
//         n1 -= 1;
//     }
//     ct
// }
// 输入n，后跟n个字符串组
pub fn nstring() -> Vec<Vec<String>> {
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
// 循环输入二维字符串
pub fn nnstring() -> Vec<Vec<String>> {
    let mut v: Vec<Vec<String>> = Vec::new();
    for line in stdin().lock().lines() {
        let s = line.unwrap();
        let mut v1: Vec<String> = Vec::new();
        for i in s.trim().split(" ") {
            v1.push(i.to_string());
        }
        v.push(v1);
    }
    v
}

pub fn sort_two(v: &mut Vec<Vec<i32>>) -> Vec<Vec<i32>> {
    // 二维数组特定列排序
    let v = v.sort_unstable_by(|x, y| x[2].cmp(&y[2]));
}
