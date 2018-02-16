#include <iostream>
#include "../include/Sales_item.h"

int main()
{
  Sales_item prev_item, curr_item;
  if (std::cin >> prev_item)
    {
      int cnt = 1;
      while (std::cin >> curr_item)
        {
          if (curr_item.isbn() == prev_item.isbn())
            ++cnt;
          else
            {
              std::cout << prev_item << ": total " << cnt << " times."
                        << std::endl;
              prev_item = curr_item;
              cnt = 1;
            }
        }
      std::cout << std::endl << prev_item << ": total " << cnt << " times."
                << std::endl;  // Output for the last item.
      return 0;
    }
  else
    {
      std::cerr << "No input data." << std::endl;
      return -1;
    }
}
