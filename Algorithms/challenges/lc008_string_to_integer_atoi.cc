#include <string>
#include <climits>

using std::string;


class Solution {
public:
    int myAtoi(string str) {
      long long res = 0;
      int sign = 1;

      auto i = str.find_first_not_of(' ');
      if (i == string::npos) return 0;
      if (str[i] == '-' || str[i] == '+')
        sign = (str[i++] == '-') ? -1 : 1;

      while (i < str.size() && '0' <= str[i] && str[i] <= '9')
        {
          res = res * 10 + (str[i++] - '0');
          if (res * sign > INT_MAX) return INT_MAX;
          if (res * sign < INT_MIN) return INT_MIN;
        }
      return sign * res;
    }
};
