#include <string>

using std::string;

class Solution {
public:
    string longestPalindrome(string s) {
      if (s.empty()) return "";
      if (s.length() <= 1) return s;
      unsigned max_start = 0;  // start of the longest palindrome
      unsigned max_len = 1;  // length of the longest palindrome
      for (unsigned i = 0; i < s.size(); ) 
        {
          if (s.length() - i <= max_len / 2)  // the leftover chars cannot be
                                              // longer than current palindrome
            break;

          unsigned j = i, k = i;
          while (k < s.length() - 1 && s[k+1] == s[k])  // skip duplicate chars
            ++k;
          i = k + 1;
          while (k < s.length() - 1 && j > 0 && s[k+1] == s[j-1])
            {
              ++k;  // expaand to right
              --j;  // expand to left
            }
          unsigned new_len = k - j + 1;
          if (new_len > max_len)  // update result if find a longer palindrome
            {
              max_len = new_len;
              max_start = j;
            }
        }
      return s.substr(max_start, max_len);
    }
};
