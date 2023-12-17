struct Solution {}
impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut res = 0;
        let (mut start, mut end) = (0, height.len() - 1);
        while start < end {
            let d = end - start;
            let h: i32;
            if height[start] < height[end] {
                h = height[start];
                start += 1;
            } else {
                h = height[end];
                end -= 1;
            }
            let tmp = d as i32 * h;
            if res < tmp {
                res = tmp;
            }
        }
        return res;
    }
}
