#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        auto res{ 1.0 };
        // auto l1{ nums1.size() };
        // auto l2{ nums2.size() };
        // auto len{ l1 + l2 };

        return res;
    }
};

int main() {
    vector<int32_t> v1{1, 3}, v2{ 2 };

    auto res{ Solution().findMedianSortedArrays(v1,v2) };
    cout << res << endl;
}