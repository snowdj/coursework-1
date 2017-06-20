"""
Time: O(n)
Space: O(n)

Given a List of words, return the words that can be typed using
letters of alphabet on only one row's of American keyboard like the
image below.

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyrows = ('asdfghjkl', 'qwertyuiop', 'zxcvbnm')
        output = []
        for w in words:
            for row in keyrows:
                if all(x.lower() in row for row in keyrows for x in w):
                    output.append(w)
                    break
        return output
