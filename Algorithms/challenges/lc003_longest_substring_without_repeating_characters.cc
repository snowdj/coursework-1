#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>

using std::string;

class Solution {
public:
  int lengthOfLongestSubstring(string s) {
      int i = -1;
      std::unordered_map<char, int> m;
      unsigned maxlen = 0;
      for (unsigned j = 0; j != s.length(); j++)
        {
          if (m.find(s[j]) != m.end())
            i = std::max(m[s[j]], i);
          m[s[j]] = j;
          maxlen = std::max(maxlen, j - i);
        }
      return maxlen;
    }
};


class Solution2 {
public:
  int lengthOfLongestSubstring(string s) {
    int i = -1;
    std::vector<int> m(256, -1);
    unsigned maxlen = 0;
    for (unsigned j = 0; j != s.length(); j++)
      {
        i = std::max(m[s[j]], i);
        m[s[j]] = j;
        maxlen = std::max(maxlen, j - i);
      }
    return maxlen;
  }
};
