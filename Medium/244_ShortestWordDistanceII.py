"""
Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""

"""
class WordDistance:
    def __init__(self, words):
        self.wordPos = {}
        for i in range(len(words)):
            if words[i] not in self.wordPos:
                self.wordPos[words[i]] = [i]
            else:
                self.wordPos[words[i]].append(i)

    def shortest(self, word1, word2):
        res = sys.maxsize
        for i in self.wordPos[word1]:
            for j in self.wordPos[word2]:
                res = min(res, abs(i - j))
        return res
"""

class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.wordPos = {}
        for i in range(len(words)):
            if words[i] not in self.wordPos:
                self.wordPos[words[i]] = [i]
            else:
                self.wordPos[words[i]].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = sys.maxsize
        p1, p2 = 0, 0
        while p1 < len(self.wordPos[word1]) and p2 < len(self.wordPos[word2]):
            res = min(res, abs(self.wordPos[word2][p2] - self.wordPos[word1][p1]))
            if self.wordPos[word1][p1] < self.wordPos[word2][p2]:
                p1 += 1
            else:
                p2 += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)