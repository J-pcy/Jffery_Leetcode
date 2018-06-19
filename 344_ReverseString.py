"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        res = ""
        for i in xrange(len(s)-1, -1, -1):
            res = res + s[i]
        return res
        """
        """
        return s[::-1]
        """
        s = list(s)
        for i in xrange(0, len(s)/2):
            tmp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = tmp
        return ''.join(s)
    