"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        flag = 0
        len1 = len(num1)
        len2 = len(num2)
        while len1 or len2 or flag:
            digit = flag
            if len1:
                len1 -= 1
                digit += ord(num1[len1]) - ord('0')
            if len2:
                len2 -= 1
                digit += ord(num2[len2]) - ord('0')
            flag = digit // 10
            res.append(str(digit % 10))
        return ''.join(res[::-1])
            