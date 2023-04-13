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
        let mut res = 0.0;
        let l1 = nums1.len();
        let l2 = nums2.len();
        let len = l1 + l2;
        // pf合并后的奇偶 1为偶数 0为奇数
        // 默认为偶数
        let mut p: usize;
        let mut pf = 1;
        match len % 2 {
            0 => p = len / 2 - 1,
            _ => {
                pf = 0;
                p = len / 2;
            }
        }
        // 左上大于右下则左移p1，左下大于右上则右移p1
        let (mut p1, mut p2): (usize, usize);
        match l1 < l2 {
            true => {
                p1 = 0;
                p2 = p;
            }
            false => {
                p2 = 0;
                p1 = p;
            }
        }
        loop {
            // p1 >=0 <=l1-1
            // p2 >=0 <=l2-1
            if nums1[p1] > nums2[p2 + 1] {
                p1 -= 1;
                p2 = p - p1;
                continue;
            }
            if nums2[p2] > nums1[p1 + 1] {
                p1 += 1;
                p2 = p - p1;
                continue;
            }
            break;
        }

        match pf {
            1 => res = (nums1[p1] + nums2[p2]) as f64 / 2.0,
            _ => {
                if nums1[p1] < nums2[p2] {
                    res = nums1[p1] as f64;
                } else {
                    res = nums2[p2] as f64;
                }
            }
        }

        return res;
    }
}
