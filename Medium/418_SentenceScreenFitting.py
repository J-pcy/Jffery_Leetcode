"""
Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output: 
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output: 
2

Explanation:
a-bcd- 
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output: 
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.
"""

class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        se = ' '.join(sentence) + ' '
        length = len(se)
        res = 0
        for i in range(rows):
            res += cols
            if se[res % length] == ' ':
                res += 1
            else:
                while res > 0 and se[(res - 1) % length] != ' ':
                    res -= 1
        return res // length
        """
        #Time Limit Exceeded
        se = ' '.join(sentence) + ' '
        length = len(se)
        n = len(sentence)
        res, idx = 0, 0
        for i in range(rows):
            restCols = cols
            while restCols > 0:
                if restCols >= len(sentence[idx]):
                    restCols -= len(sentence[idx])
                    if restCols > 0:
                        restCols -= 1
                    idx += 1
                    if idx >= n:
                        res += 1 + restCols // length
                        restCols %= length
                        idx = 0
                else:
                    break
        return res
        """
        