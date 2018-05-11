#include <string>
#include <vector>

using std::string;
using std::vector;


class Solution {

  /*
    Dynamic Programming.
    Define the state P[i][j] to be true if s[0..i) matches p[0..j) and false otherwise. Then the state equations are:
    P[i][j] = P[i - 1][j - 1], if p[j - 1] != '*' && (s[i - 1] == p[j - 1] || p[j - 1] == '.');
    P[i][j] = P[i][j - 2], if p[j - 1] == '*' and the pattern repeats for 0 times;
    P[i][j] = P[i - 1][j] && (s[i - 1] == p[j - 2] || p[j - 2] == '.'), if p[j - 1] == '*' and the pattern repeats for at least 1 times.
  */

public:
    bool isMatch(string s, string p) {
      unsigned m = s.length(), n = p.length();
      vector<vector<bool> > dp(m+1, vector<bool>(n+1, false));
      dp[0][0] = true;
      for (unsigned i = 0; i <= m; i++)
        for (unsigned j = 1; j <= n; j++)
          if (p[j-1] == '*')
            dp[i][j] = dp[i][j-2] || (i > 0 && (s[i-1] == p[j-2] || p[j-2] == '.') && dp[i-1][j]);
          else
            dp[i][j] = i > 0 && (s[i-1] == p[j-1] || p[j-1] == '.') && dp[i-1][j-1];
      return dp[m][n];
    }
};
