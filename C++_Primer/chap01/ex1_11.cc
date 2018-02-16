#include <iostream>

int main()
{
  int a = 0, b = 0, start = 0, end = 0;
  std::cout << "Input two integers:" << std::endl;
  std::cin >> a >> b;
  if (a <= b)
    {
      start = a;
      end = b;
    }
  else
    {
      start = b;
      end = a;
    }
  while (start <= end)
    {
      std::cout << start << " ";
      ++start;
    }
  std::cout << std::endl;
  return 0;
}
