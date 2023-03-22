#include <iostream>
#include <vector>
using namespace std;

vector<vector<int32_t>> io()
{
  int32_t n, m;
  cin >> n >> m;
  vector<vector<int32_t>> v(n, vector<int32_t>(m));
  for (auto &i : v)
  {
    for (auto &j : i)
    {
      cin >> j;
    }
  }
  for (auto &i : v)
  {
    for (auto &j : i)
    {
      cout << j << ' ';
    }
    cout << endl;
  }
  return v;
}

int main()
{
  io();
}