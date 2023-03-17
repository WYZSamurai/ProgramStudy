use std::collections::HashMap;
use std::io::*;
enum Solution {}
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<i32, usize> = HashMap::new();
        for i in 0..nums.len() {
            if let Some(y) = map.get(&(target - nums[i])) {
                return vec![*y as i32, i as i32];
            }
            map.insert(nums[i], i);
        }
        panic!("not found!")
    }
}

fn main() {
    let mut n = String::new();
    stdin().read_line(&mut n).unwrap();
    let mut v: Vec<i32> = Vec::new();
    for i in n.trim().split(" ") {
        v.push(i.parse().unwrap());
    }
    n.clear();
    stdin().read_line(&mut n).unwrap();
    let n: i32 = n.trim().parse().unwrap();
    let s = Solution::two_sum(v, n);
    println!("{:?}", s);
}
