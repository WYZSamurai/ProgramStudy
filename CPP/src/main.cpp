#include<iostream>
#include<sstream>
#include<vector>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        auto l1{ nums1.size() };
        auto l2{ nums2.size() };
        constexpr auto len{ l1 + l2 };
        // 偶数中位数在len/2-1
        if (len % 2 == 0) {
        }
    }
};

int main() {
    vector<int32_t> v1, v2;
    while (true) {
        auto x{ cin.get() - '0' };
        v1.push_back(x);
        if (cin.get() == '\n') {
            break;
        }
    }
    while (true) {
        auto x{ cin.get() - '0' };
        v2.push_back(x);
        if (cin.get() == '\n') {
            break;
        }
    }

    auto res{ Solution::findMedianSortedArrays(v1,v2) };
    cout << res << endl;
}