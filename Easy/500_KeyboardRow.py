"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        res = []
        for i in words:
            tmp = [0, 0, 0]
            for j in i:
                for k in xrange(len(keyboard)):
                    if j in keyboard[k]:
                        tmp[k] = 1
            if sum(tmp)==1:
                res.append(i)
        return res
        