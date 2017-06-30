"""
Time: O(1)
Space: O(1)

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""


# table lookup O(1)
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_k = ['', 'M', 'MM', 'MMM']
        roman_h = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        roman_10 = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        roman_1 = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        return roman_k[num // 1000] + roman_h[(num % 1000) // 100] \
            + roman_10[(num % 100) // 10] + roman_1[num % 10]


# greedy O(k)
class Solution2(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        s = ''
        for i in range(len(val)):
            while num >= val[i]:
                num -= val[i]
                s += roman[i]
        return s
