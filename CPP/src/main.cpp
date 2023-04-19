#include<iostream>
#include<vector>
using namespace std;

int main() {
    auto a{ 1 };
    vector<int> v1;
    v1.push_back(a);
    for (auto& i : v1) {
        cout << i << endl;
    }
}