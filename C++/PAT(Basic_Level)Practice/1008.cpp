/*
1.获取vector中第n个元素：vector.at(n-1)
2.插入vector第n个位置前：vector.insert(vector.begin()+n-1,val)
*/
#include<iostream>
#include<vector>
using namespace std;

int main() {
    int32_t n, m;
    cin >> n >> m;
    vector<int32_t> vec(n);
    for (auto& i : vec) {
        cin >> i;
    }
    for (auto i = 0;i < m;i++) {
        auto a = vec.at(n - 1);
        vec.pop_back();
        vec.insert(vec.begin(), a);
    }
    for (auto i = 0;i < n;i++) {
        if (i == n - 1) {
            cout << vec.at(i);
            continue;
        }
        cout << vec.at(i) << ' ';
    }
}