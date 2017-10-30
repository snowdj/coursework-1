"""
Julia has a string, s, consisting of one or more of the following letters: a, e, i, o, and u.
 
We define a magical subsequence of s to be a sequence of letters derived from s that contains all five vowels in order. This means a magical subsequence will have one or more a's followed by one or more e's followed by one or more i's followed by one or more o's followed by one or more u's. For example, if s = "aeeiooua", then "aeiou" and "aeeioou" are magical subsequences but "aeio" and "aeeioua" are not.
 
Complete the longestSubsequence function in your editor. It has 1 parameter: a string, s. It must return an integer denoting the length of the longest magical subsequence in s. If no magical subsequence can be constructed, return 0.
 
Input Format
The locked stub code in your editor reads a single string, s, from stdin and passes it to your function.
 
Constraints
5 < length of string s < 5 × 105
String s is composed of English vowels (i.e., a, e, i, o, and u).
 
Output Format
Your function must return an integer denoting the length of the longest magical subsequence in s (if no such subsequence exists, this value is 0). This is printed to stdout by the locked stub code in your editor.
 
Sample Input 1
aeiaaioooaauuaeiou
 
Sample Output 1
10
 
Explanation 1
In the table below, the component characters of the longest magical subsequence are red:
a	e	i	a	a	i	o	o	o	a	a	u	u	a	e	i	o	u
 
Sample Input 2
aeiaaioooaa
 
Sample Output 2
0
 
Explanation 2
String s does not contain the letter u, so it is not possible to construct a magical subsequence.
"""


# A variation from leetcode 300 Longest Increasing Subsequence

# DFS. TLE. O(2^n)
def longestSubsequence_dfs(s):
    if len(set(s)) < 5:
        return 0
    tbl_next = {'': 'a', 'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'u'}

    def dfs(i, vow):
        res = [s[j] + tail
               for j in range(i, len(s)) if s[j] in (vow, tbl_next[vow])
               for tail in dfs(j+1, s[j])
               if s[j] == 'u' or tail and tail[-1] == 'u']
        return res or ['']
    return max(len(seq) for seq in dfs(0, ''))


# DFS + DP. 13/20 cases passed, others TLE. O(n^2)
def longestSubsequence_dp(s):
    if len(set(s)) < 5:
        return 0
    start = s.find('a')
    end = start + s[start:].rfind('u')
    s = s[start:end+1]
    tbl = {'a': ['a'], 'e': ['a', 'e'], 'i': ['e', 'i'], 'o': ['i', 'o'], 'u': ['o', 'u']}
    dp = [1] + [0] * (len(s)-1)
    for i in range(len(s)):
        for j in range(i):
            if s[j] in tbl[s[i]] and dp[j] != 0:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[-1]


# Binary search O(n*lg(n)). Partially correct, 18/20 passed.
from bisect import bisect_left
def longestSubsequence(s):
    if len(set(s)) < 5:
        return 0
    first = [s.find(v) for v in 'aeio']
    last = [s.rfind(v) for v in 'eiou']
    if any(p[0] > p[1] for p in zip(first, last)):
        return 0
    tbl = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'v'}
    magic = []
    for i in range(first[0], last[-1]+1):
        pos = bisect_left(magic, tbl[s[i]])
        if pos < len(magic):
            magic[pos] = s[i]
        else:
            magic.append(s[i])
    return len(magic)
