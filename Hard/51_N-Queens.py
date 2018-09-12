"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""

class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        """
        res = []
        self.dfs(n, [], res)
        return res
    
    def dfs(self, n, pos, res):
        row = len(pos)
        if row == n:
            res.append(self.drawBoard(pos))
            return
        for col in range(n):
            if not self.isValid(pos, row, col):
                continue
            pos.append(col)
            self.dfs(n, pos, res)
            pos.pop()
    
    def drawBoard(self, pos):
        board = []
        for i in range(len(pos)):
            row = ['.' if pos[i] != j else 'Q' for j in range(len(pos))]
            board.append(''.join(row))
        return board
    
    def isValid(self, pos, row, col):
        for i in range(row):
            if pos[i] == col or abs(col - pos[i]) == abs(row - i):
                return False
        return True
        """
        """
        res = []
        pos = [-1] * n
        self.dfs(pos, 0, res)
        return res
    
    def dfs(self, pos, row, res):
        n = len(pos)
        if n == row:
            res.append(self.drawBoard(pos))
            return
        for col in range(n):
            if not self.isValid(pos, row, col):
                continue
            pos[row] = col
            self.dfs(pos, row + 1, res)
            pos[row] = -1
    
    def drawBoard(self, pos):
        board = []
        for i in range(len(pos)):
            row = ['Q' if pos[i] == j else '.' for j in range(len(pos))]
            board.append(''.join(row))
        return board
    
    def isValid(self, pos, row, col):
        for i in range(row):
            if pos[i] == col or abs(col - pos[i]) == abs(row - i):
                return False
        return True
        """
        res = []
        pos = [-1] * n
        row, col = 0, 0
        while True:
            col = pos[row] + 1
            while col < n:
                if self.isValid(pos, row, col):
                    pos[row] = col
                    if row == n - 1:
                        res.append(self.drawBoard(pos))
                    else:
                        row += 1
                        break
                col += 1
            if col == n:
                if row == 0:
                    break
                pos[row] = -1
                row -= 1
        return res
    
    def drawBoard(self, pos):
        res = []
        for i in range(len(pos)):
            row = ['Q' if pos[i] == j else '.' for j in range(len(pos))]
            res.append(''.join(row))
        return res
    
    def isValid(self, pos, row, col):
        for i in range(row):
            if pos[i] == col or abs(col - pos[i]) == abs(row - i):
                return False
        return True
        