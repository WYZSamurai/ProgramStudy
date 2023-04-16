fn main() {
    let nums1 = vec![1, 8, 6, 2, 5, 4, 8, 3, 7];
    println!("{}", Solution::max_area(nums1));
}

struct Solution {}
// 始终保存当前最大的面积，容积高度为较低侧的高度，宽为两个指针的举例
impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let res = 0;
        let (leftp, rightp): (usize, usize);
        for i in 0..height.len() {}
        return res;
    }
}
