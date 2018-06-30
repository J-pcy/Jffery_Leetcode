"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.res = ''
        if len(s) <= 1:
            return s
        for i in range(len(s) - 1):
            self.helper(s, i - 1, i + 1)
            self.helper(s, i, i + 1)
        return self.res
    
    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if len(s[left + 1:right]) > len(self.res):
            self.res = s[left + 1:right]
        