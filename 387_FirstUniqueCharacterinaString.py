"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict = {}
        for i in s:
            if not s_dict.has_key(i):
                s_dict[i] = 1
            else:
                s_dict[i] += 1
        for j in xrange(len(s)):
            if s_dict[s[j]]==1:
                return j
        return -1
        