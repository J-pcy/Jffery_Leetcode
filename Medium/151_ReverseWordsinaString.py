"""
Given an input string, reverse the string word by word.

Example:  

Input: "the sky is blue",
Output: "blue is sky the".
Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
Follow up: For C programmers, try to solve it in-place in O(1) space.
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        slist = s.split(' ')
        i = 0
        while i < len(slist):
            if slist[i] == '':
                slist.pop(i)
            else:
                i += 1
        slist.reverse()
        return ' '.join(slist)
        """
        slist = s.split()
        slist.reverse()
        return ' '.join(slist)
        """
        #C++ O(1) space, not work
        index, length = 0, len(s)
        i = 0
        while i < length:
            if s[i] != ' ':
                if index:
                    index += 1
                    s[index] = ' '
                j = i
                while j < length and s[j] != ' ':
                    s[index] = s[j]
                    index += 1
                    j += 1
                s[index - j + i:index] = s[index - j + i:index:-1]
                i = j
            i += 1
        s = s[::-1]
        return s[:index]
        """
        