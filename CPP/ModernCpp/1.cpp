#include <iostream>
int main()
{
  std::cout << "打印 ASCII表:\n";
  for (char i = 32; i < 127; ++i)
  {
    std::cout << i << ' ';
    if (i % 16 == 15)
      std::cout << '\n';
  }
  std::cout << std::endl;
  system("pause");
}