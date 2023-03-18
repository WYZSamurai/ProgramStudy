#include <iostream>
#include <string>
using namespace std;

struct s {
  int a;
  string str;
};

int main() {
  auto a = 10;
  cout << a << endl;
  s s1 = {12, "deded"};
  cout << s1.a << ' ' << s1.str << endl;
}