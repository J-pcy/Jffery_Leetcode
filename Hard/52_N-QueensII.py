"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

class Solution:
    res = 0
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        pos = [-1] * n
        self.dfs(pos, 0)
        return self.res
    
    def dfs(self, pos, row):
        n = len(pos)
        if row == n:
            self.res += 1
            return
        for col in range(n):
            if not self.isValid(pos, row, col):
                continue
            pos[row] = col
            self.dfs(pos, row + 1)
            pos[row] = -1
    
    def isValid(self, pos, row, col):
        for i in range(row):
            if pos[i] == col or abs(col - pos[i]) == abs(row - i):
                return False
        return True
        