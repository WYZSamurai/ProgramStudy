#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> fun() {
  int m, n;
  cin >> m >> n;
  vector<vector<int>> v(m, vector<int>(n));
  for (auto &i : v) {
    for (auto &j : i) {
      cin >> j;
    }
  }
  return v;
}

int main() {
  vector<vector<int>> v = fun();
  for (auto &i : v) {
    for (auto &j : i) {
      cout << j << ' ';
    }
    cout << endl;
  }
}