"""
Time: O(n)
Space: O(1)

Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:
Given s = "internationalization", abbr = "i12iz4n":
Return true.

Example 2:
Given s = "apple", abbr = "a2e":
Return false.
"""


def validWordAbbreviation(word, abbr):
    m, n = len(word), len(abbr)
    p = cnt = 0
    for i in range(n):
        if ord('0') <= ord(abbr[i]) <= ord('9'):  # current char is a number
            if cnt == 0 and abbr[i] == '0':
                return False
            cnt = 10 * cnt + int(abbr[i])
        else:  # current char is a letter
            p, cnt = p + cnt, 0
            if p > m or word[p] != abbr[i]:
                return False
            p += 1
    return p + cnt == m


# regular expression match
# https://discuss.leetcode.com/topic/61353/simple-regex-one-liner-java-python/2
def validWordAbbreviation2(word, abbr):
    regex = re.sub('\d+', lambda m: '.' * int(m.group()), abbr)
    return bool(re.match(regex + '$', word)) and not re.search('(^|\D)0', abbr)
