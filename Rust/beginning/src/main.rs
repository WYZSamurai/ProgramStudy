use std::io::stdin;

fn main() {
    let (vec, target) = iom();
    let s = Solution::find_median_sorted_arrays(vec, target);
    println!("{:?}", s);
}

fn iom() -> (Vec<i32>, Vec<i32>) {
    let mut v: Vec<i32> = Vec::new();
    let mut s = String::new();
    stdin().read_line(&mut s).unwrap();
    for i in s.trim().split(" ") {
        v.push(i.to_string().parse().unwrap());
    }
    s.clear();
    let mut v2: Vec<i32> = Vec::new();
    stdin().read_line(&mut s).unwrap();
    for i in s.trim().split(" ") {
        v2.push(i.to_string().parse().unwrap());
    }
    (v, v2)
}
struct Solution {}
impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let mut v1 = nums1;
        let mut v2 = nums2;
        v1.append(&mut v2);
        v1.sort_unstable_by(|x, y| x.cmp(y));
        let len = v1.len();
        let res: f64;
        if len % 2 == 0 {
            res = (v1[len / 2 - 1] + v1[len / 2]) as f64 / 2 as f64;
        } else {
            res = v1[len / 2] as f64;
        }
        res
    }
}
