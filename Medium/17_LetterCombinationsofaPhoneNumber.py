"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        """
        numLetter = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        if not digits:
            return []
        res = ['']
        for digit in digits:
            res = [i + j for i in res for j in numLetter[int(digit)]]
        return res
        """
        numLetter = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        if not digits:
            return []
        res = []
        self.dfs(digits, 0, numLetter, '', res)
        return res
    
    def dfs(self, digits, index, numLetter, tmp, res):
        if index == len(digits):
            res.append(tmp)
            return
        for x in numLetter[int(digits[index])]:
            self.dfs(digits, index + 1, numLetter, tmp + x, res)
        