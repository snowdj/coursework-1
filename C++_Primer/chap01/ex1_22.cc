#include <iostream>
#include "../include/Sales_item.h"

int main()
{
  Sales_item sum;
  if (std::cin >> sum)
    {
      Sales_item trans;
      while (std::cin >> trans)
        {
          if (sum.isbn() == trans.isbn())
            sum += trans;
          else
            {
              std::cout << sum << std::endl;
              sum = trans;
            }
        }
      std::cout << sum << std::endl;
      return 0;
    }
  else
    {
      std::cerr << "No input data." << std::endl;
      return -1;
    }
}
