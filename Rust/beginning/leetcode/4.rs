fn main() {
    // 1,2,3
    // p1=1,p2=0
    let nums1 = vec![1];
    let nums2 = vec![2];
    let res = Solution::find_median_sorted_arrays(nums1, nums2);
    println!("{}", res);
}

struct Solution {}
impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let res: f64;
        let l1 = nums1.len();
        let l2 = nums2.len();
        // 设置nums1较短
        if l1 > l2 {
            res = Solution::find_median_sorted_arrays(nums2, nums1);
            return res;
        }
        // 设置最终的指针
        // p2若为0，则为奇数，不为0则为偶数
        let (mut _p1, mut p2): (usize, usize) = (0, 0);
        if (l1 + l2) % 2 == 0 {
            _p1 = (l1 + l2) / 2 - 1;
            p2 = (l1 + l2) / 2;
        } else {
            _p1 = (l1 + l2) / 2;
        }
        // 如果l1为0，则直接判断中位数
        if l1 == 0 {
            if p2 == 0 {
                res = nums2[_p1] as f64;
                return res;
            } else {
                res = (nums2[_p1] + nums2[p2]) as f64 / 2.0;
                return res;
            }
        }
        // 偶数情况，找第len/2和len/2-1个数
        // 奇数情况，找第len/2个数
        let (mut i, mut j): (usize, usize) = (0, 0);
        // 奇数情况
        if (l1 + l2) % 2 != 0 {
            // i+j=p1为止
            while i + j != _p1 {
                if nums1[i] < nums2[j] && i < l1 - 1 {
                    i += 1;
                    continue;
                }
                if nums2[j] < nums1[i] && j < l2 - 1 {
                    j += 1;
                    continue;
                }
                if nums1[i] == nums2[j] && i < l1 - 1 {
                    i += 1;
                    continue;
                } else if nums1[i] == nums2[j] && j < l2 - 1 {
                    j += 1;
                    continue;
                }
                break;
            }
            // 如果i+j<p1则一定是上边数组的数小，且到头了
            if i + j < _p1 {
                let res = nums2[_p1 - i - 1] as f64;
                return res;
            }
            match nums1[i] < nums2[j] {
                true => res = nums1[i] as f64,
                false => res = nums2[j] as f64,
            }
            return res;
        }
        // 偶数情况 当i+j==p1时，取n1[i],n2[j]较小的和n1[i+1],n2[j+1]较小的
        else {
            while i + j != _p1 {
                if nums1[i] < nums2[j] && i < l1 - 1 {
                    i += 1;
                    continue;
                }
                if nums2[j] < nums1[i] && j < l2 - 1 {
                    j += 1;
                    continue;
                }
                if nums1[i] == nums2[j] && i < l1 - 1 {
                    i += 1;
                    continue;
                } else if nums1[i] == nums2[j] && j < l2 - 1 {
                    j += 1;
                    continue;
                }
                break;
            }
            let (a, b): (f64, f64);
            // 如果i+j<p1则一定是上边数组的数小，且到头了
            if i + j < _p1 {
                let a = nums2[_p1 - i] as f64;
                let b = nums2[_p1 - i - 1] as f64;
                res = (a + b) / 2.0;
                return res;
            }
            // 当目标数在下边的数组时
            if nums2[j] < nums1[i] {
                a = nums2[j] as f64;
                if j < l2 - 1 {
                    j += 1;
                }
                // 下边的数组到头了，则下一个较大的数一定是上边的数组
                else {
                    b = nums1[_p1 - j] as f64;
                    res = (a + b) / 2.0;
                    return res;
                }
            }
            // 当目标数在上边的数组时
            else {
                a = nums1[i] as f64;
                if i < l1 - 1 {
                    i += 1;
                }
                // 上边的数组到头了
                else {
                    b = nums2[_p1 - i] as f64;
                    res = (a + b) / 2.0;
                    return res;
                }
            }
            // 若未到头，则更新i，j并继续判断b，取二者较小的部分
            if nums1[i] < nums2[j] {
                b = nums1[i] as f64;
            } else {
                b = nums2[j] as f64;
            }
            res = (a + b) / 2.0;
        }
        return res;
    }
}
////////////////
fn main() {
    // 1,2,3
    // p1=1,p2=0
    let nums1 = vec![1];
    let nums2 = vec![2, 3];
    let res = Solution::find_median_sorted_arrays(nums1, nums2);
    println!("{}", res);
}

struct Solution {}
impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let total = nums1.len() + nums2.len();
        let mut idx1 = 0;
        let mut idx2 = 0;
        let mut a = 0;
        let mut prev_a = 0;
        // 直到idx1+idx2=total/2
        for _ in 0..(total / 2 + 1) {
            // 将上一次循环的结果给preva
            prev_a = a;
            if let Some(&v1) = nums1.get(idx1) {
                if let Some(&v2) = nums2.get(idx2) {
                    a = v1.min(v2);
                    if v1 < v2 {
                        idx1 += 1;
                    } else {
                        idx2 += 1;
                    }
                }
                // 若nums2到头了则存储nums1的数
                else {
                    a = v1;
                    idx1 += 1;
                }
            }
            // 若nums1到头了，存nums2的数
            else {
                a = nums2[idx2];
                idx2 += 1;
            }
        }
        // 奇数，取第 total/2 + 1 个数
        // 偶数，取第 total/2 和 total/2 + 1 个数
        if total % 2 == 0 {
            (a as f64 + prev_a as f64) / 2.0
        } else {
            a as f64
        }
    }
}
