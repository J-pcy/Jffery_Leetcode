"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_list = list(s)
        l, r = 0, len(s)-1
        while l<r:
            if self.isVowel(s[l]):
                if self.isVowel(s[r]):
                    str_list[l] = s[r]
                    str_list[r] = s[l]
                    l += 1
                    r -= 1
                else:
                    str_list[r] = s[r]
                    r -= 1
            else:
                str_list[l] = s[l]
                l += 1
        return ''.join(str_list)
                    
        
    def isVowel(self, string):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in vowels:
            if string==i:
                return True
        return False
        