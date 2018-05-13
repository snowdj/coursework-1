#include <string>
#include <vector>

using std::string;
using std::vector;


class Solution {
public:
    vector<string> letterCombinations(string digits) {
      if (digits.empty()) return vector<string>();
      vector<string> res = {""};
      static const vector<string> m = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
      for (auto d: digits) 
        {
          vector<string> stk;
          string s = m[d - '0'];
          for (auto pfx: res)
            for (auto c: s)
              stk.push_back(pfx + c);
          swap(res, stk);
        }
      return res;
    }
};
