struct Solution {}
impl Solution {
    // 始终保存当前最大的面积，容积高度为较低侧的高度，宽为两个指针的举例
    fn vol(i: usize, j: usize, h1: i32, h2: i32) -> i32 {
        let h: i32;
        let d = (j - i) as i32;
        if h1 < h2 {
            h = h1;
        } else {
            h = h2;
        }
        return h * d;
    }

    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut res = 0;
        let len = height.len();
        for i in 0..len {
            for j in i + 1..len {
                let tmp = Solution::vol(i, j, height[i], height[j]);
                if res < tmp {
                    res = tmp;
                }
            }
        }
        return res;
    }
}

fn main() {
    let nums1 = vec![1, 8, 6, 2, 5, 4, 8, 3, 7];
    println!("{}", Solution::max_area(nums1));
}
