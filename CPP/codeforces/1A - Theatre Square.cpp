#include <iostream>
using namespace std;

int64_t fun(int64_t n, int64_t a)
{
  auto x = n / a;
  auto y = n % a;
  if (y != 0)
  {
    x += 1;
  }
  return x;
}

int main()
{
  int64_t n, m, a;
  cin >> n >> m >> a;
  auto y = fun(n, a);
  auto x = fun(m, a);
  cout << "需要" << x * y << "块" << endl;
  system("pause");
}
