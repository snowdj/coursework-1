#include <string>
#include <vector>

using std::string;
using std::vector;


class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
      string prefix = "";
      for (unsigned i = 0; strs.size() > 0; prefix += strs[0][i], i++)
        for (unsigned j = 0; j != strs.size(); j++)
          if (i >= strs[j].size() || (j > 0 && strs[j][i] != strs[j-1][i]))
            return prefix;
      return prefix;
    }
};
