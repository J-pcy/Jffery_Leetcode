"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        str_dict = {}
        for i in magazine:
            if not str_dict.has_key(i):
                str_dict[i] = 1
            else:
                str_dict[i] += 1
        for j in ransomNote:
            if not str_dict.has_key(j):
                return False
            else:
                str_dict[j] -= 1
                if str_dict[j]<0:
                    return False
        return True
        