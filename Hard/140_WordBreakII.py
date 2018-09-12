"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        """
        #Time Limit Exceeded
        res = []
        if not s or not wordDict:
            return res
        self.dfs(s, wordDict, [], res)
        return res
    
    def dfs(self, s, wordDict, tmp, res):
        if s in wordDict:
            res.append((' ').join(tmp + [s]))
        for i in range(len(s)):
            if s[:i + 1] in wordDict:
                self.dfs(s[i + 1:], wordDict, tmp + [s[:i + 1]], res)
        """
        """
        return self.dfs(s, wordDict, {})
    
    def dfs(self, s, wordDict, wordBreak):
        if s in wordBreak:
            return wordBreak[s]
        if not s:
            return []
        res = []
        for i in range(len(s) - 1):
            if s[:i + 1] in wordDict:
                partitions = self.dfs(s[i + 1:], wordDict, wordBreak)
                for partition in partitions:
                    res.append(s[:i + 1] + ' ' + partition)
        if s in wordDict:
            res.append(s)
        wordBreak[s] = res
        return res
        """
        return self.dfs(s, wordDict, {})
    
    def dfs(self, s, wordDict, wordBreak):
        if s in wordBreak:
            return wordBreak[s]
        if not s:
            return []
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(s)
            else:
                partitions = self.dfs(s[len(word):], wordDict, wordBreak)
                for partition in partitions:
                    res.append(word + ' ' + partition)
        wordBreak[s] = res
        return res
        