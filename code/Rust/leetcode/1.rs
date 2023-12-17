use std::collections::HashMap;
use std::io::stdin;

fn main() {
    let (vec, target) = iom();
    let s = Solution::two_sum(vec, target);
    println!("{:?}", s);
}

fn iom() -> (Vec<i32>, i32) {
    let mut v: Vec<i32> = Vec::new();
    let mut s = String::new();
    stdin().read_line(&mut s).unwrap();
    for i in s.trim().split(" ") {
        v.push(i.to_string().parse().unwrap());
    }
    s.clear();
    stdin().read_line(&mut s).unwrap();
    let target: i32 = s.trim().parse().unwrap();
    (v, target)
}
struct Solution {}
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut res: Vec<i32> = Vec::new();
        let mut map: HashMap<i32, i32> = HashMap::new();
        for i in 0..nums.len() {
            // 求出nums[i]对应的x值，如果map中有对应的x值，则输出角标
            // 否则向map输入i及其对应的值
            if map.contains_key(&(target - nums[i])) {
                res.push(*map.get(&(target - nums[i])).unwrap());
                res.push(i as i32);
            } else {
                map.insert(nums[i], i as i32);
            }
        }
        res
    }
}
