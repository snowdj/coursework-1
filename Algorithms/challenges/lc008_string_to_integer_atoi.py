"""
Time: O(n)
Space: O(n)

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.


Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
"""


# O(1) space
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0

        # skip whitespaces at the beginning
        while i < len(s) and s[i] == ' ':
            i += 1

        # process the first sign character and determine sign
        sign = 1
        if i < len(s) and s[i] in ('+', '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # process digits
        x = 0
        while i < len(s) and s[i].isdigit():
            x = x*10 + ord(s[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * x, 2**31-1))


# Regex, and cheating using int()
class Solution2(object):
    def myAtoi(self, s):
        s = re.findall('^[\+\-0]*\d+', s.strip())
        try:
            return max(-2**31, min(int(''.join(s)), 2**31-1))
        except:
            return 0
