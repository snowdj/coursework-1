#include <string>
#include <unordered_map>

using std::string;
using std::unordered_map;


class Solution {
public:
    int romanToInt(string s) {
      const unordered_map<char, int> roman = {
        {'M', 1000}, {'D', 500}, {'C', 100},
        {'L', 50}, {'X', 10}, {'V', 5}, {'I', 1}};

      int n = 0;
      for (unsigned i = 0; i != s.size(); i++)
        {
          if (i == s.size() - 1 || roman[s[i]] >= roman[s[i+1]])
            n += roman[s[i]];
          else
            n -= roman[s[i]];
        }
      return n;
    }
};
