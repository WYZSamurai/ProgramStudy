#include<iostream>
#include<string>
#include<vector>

using std::cout, std::cin, std::endl;
using std::vector;

int main() {
    vector<int> v;
    // C++20 新的通用初始化
    int x{ 1 };
    while (getchar() == '\n') {
        int i;
        cin >> i;
        v.push_back(i);
    }
    for (auto& i : v) {
        cout << i;
    }
    cout << x << endl;
}