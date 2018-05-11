#include <limits>

class Solution {
public:
    int reverse(int x) {
      long long res = 0;
      while(x)
        {
          res = res * 10 + x % 10;
          x /= 10;
        }
      return (res < std::numeric_limits<int>::min() || res > std::numeric_limits<int>::max()) ? 0 : res;
    }
};
