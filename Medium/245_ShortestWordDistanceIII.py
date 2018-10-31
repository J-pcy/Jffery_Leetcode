"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “makes”, word2 = “coding”
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3
Note:
You may assume word1 and word2 are both in the list.
"""

class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        """
        wordPos = {}
        for i in range(len(words)):
            wordPos[words[i]] = wordPos.get(words[i], []) + [i]
        res = sys.maxsize
        p1, p2 = 0, 0
        while p1 < len(wordPos[word1]) and p2 < len(wordPos[word2]):
            if wordPos[word1][p1] == wordPos[word2][p2]:
                p1 += 1
                continue
            res = min(res, abs(wordPos[word1][p1] - wordPos[word2][p2]))
            if wordPos[word1][p1] < wordPos[word2][p2]:
                p1 += 1
            else:
                p2 += 1
        return res
        """
        """
        res = sys.maxsize
        p1, p2 = len(words), -len(words)
        for i in range(len(words)):
            if words[i] == word1:
                p1 = p2 if word1 == word2 else i
            if words[i] == word2:
                p2 = i
            res = min(res, abs(p1 - p2))
        return res
        """
        res = sys.maxsize
        idx = -1
        for i in range(len(words)):
            if words[i] == word1 or words[i] == word2:
                if idx != -1 and (words[i] != words[idx] or word1 == word2):
                    res = min(res, i - idx)
                idx = i
        return res
        