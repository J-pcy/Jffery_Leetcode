"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        odd_num = 0
        s_dict = {}
        for i in s:
            if not s_dict.has_key(i):
                s_dict[i] = 1
            else:
                s_dict[i] += 1
        for value in s_dict.values():
            if value%2==1:
                odd_num += 1
        if odd_num >1:
            return False
        else:
            return True
            