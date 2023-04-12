#include<iostream>
#include<string>
#include<vector>
constexpr int size{ 10 }; // modern C++

using std::cout, std::cin, std::endl;
using std::vector;

int main() {
    vector<int> v;
    // C++20 新的通用初始化
    int x{ 1 };
    cout << x + size << endl;
}