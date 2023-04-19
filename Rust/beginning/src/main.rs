struct Solution {}
// 始终保存当前最大的面积，容积高度为较低侧的高度，宽为两个指针的举例
impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let res = height[0];
        return res;
    }
}
fn main() {
    let nums1 = vec![1, 8, 6, 2, 5, 4, 8, 3, 7];
    println!("{}", Solution::max_area(nums1));
}
