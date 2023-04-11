#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        auto v12 = nums1;
        v12.insert(v12.end(), nums2.begin(), nums2.end());
        sort(v12.begin(), v12.end(), [](auto x, auto y) {
            return x < y;
            });
        auto len = v12.size();
        double res = 0.0;
        if (len % 2 == 0) {
            res = (v12[len / 2 - 1] + v12[len / 2]) / 2.0;
        }
        else {
            res = v12[len / 2];
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<int32_t> v1, v2;
    v1 = { 1,2 };
    v2 = { 2 };
    auto a = s.findMedianSortedArrays(v1, v2);
    cout << a << endl;
}