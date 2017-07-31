"""
Time: O(n)
Space: O(1)

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""


# O(1) space
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        l, r = 0, n-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True


# O(n) space
class Solution2(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(set(s)) == 1:
            return True
        s = re.findall('[a-zA-Z0-9]', s.lower())
        return ''.join(reversed(s)) == ''.join(s)


# O(n) space
class Solution3:
    def isPalindrome(self, s):
        newS = [i.lower() for i in s if i.isalnum()]
        return newS == newS[::-1]
        #return newS[:len(newS)/2] == newS[(len(newS)+1)/2:][::-1]  # This one is better, but too long
