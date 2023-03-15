#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  auto n = 0;
  vector<int> v;
  cin >> n;
  for (auto i = 0; i < n; i++) {
    int x;
    cin >> x;
    v.push_back(x);
  }
  sort(v.begin(), v.end());
  for (auto &i : v) {
    cout << i << ' ';
  }
  cout << endl;
  // cout << endl;
}