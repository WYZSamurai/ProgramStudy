use std::io::stdin;
fn main() {
    let v = iom();
    let s = Solution::max_area(v);
    println!("{}", s);
}

struct Solution;
impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        // result需要知道两个数组的index，且需要获取较低的高度
        let mut result = 0;
        // list保存两条线的index和height
        let mut list: Vec<Vec<i32>> = Vec::new();
        let len = height.len();
        result
    }
}

fn iom() -> Vec<i32> {
    let mut s = String::new();
    let mut v: Vec<i32> = Vec::new();
    stdin().read_line(&mut s).unwrap();
    for i in s.trim().split(" ") {
        v.push(i.to_string().parse().unwrap());
    }
    v
}
