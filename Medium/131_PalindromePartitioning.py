"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        """
        res = []
        self.helper(s, [], res)
        return res
    
    def helper(self, s, tmp, res):
        if len(s) == 0:
            res.append(tmp[:])
            return
        for i in range(len(s)):
            if s[:i + 1] == s[:i + 1][::-1]:
                self.helper(s[i + 1:], tmp + [s[:i + 1]], res)
        """
        res = []
        self.helper(s, [], res)
        return res
    
    def helper(self, s, tmp, res):
        if not s:
            res.append(tmp[:])
            return
        for i in range(len(s)):
            if self.isPalindrome(s[:i + 1]):
                self.helper(s[i + 1:], tmp + [s[:i + 1]], res)
    
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        