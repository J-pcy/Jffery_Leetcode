"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        """
        if len(word) == 0:
            return True
        if len(board) == 0 or len(board[0]) == 0:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, 0, i, j):
                    return True
        return False
    def dfs(self, board, word, index, x, y):
        dir_x = [-1, 1, 0, 0]
        dir_y = [0, 0, -1, 1]
        if word[index] != board[x][y]:
            return False
        else:
            if index == len(word) - 1:
                return True
            board[x][y] = None
            for i in range(4):
                if self.inbound(board, x + dir_x[i], y + dir_y[i]):
                    if self.dfs(board, word, index + 1, x + dir_x[i], y + dir_y[i]):
                        return True
            board[x][y] = word[index]
            
    def inbound(self, board, x, y):
        return x >= 0 and x < len(board) and y >= 0 and y < len(board[0])
        """
        if len(word) == 0:
            return True
        if len(board) == 0 or len(board[0]) == 0:
            return False
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, 0, i, j, visited):
                    return True
        return False
    
    def dfs(self, board, word, index, x, y, visited):
        dir_x = [-1, 1, 0, 0]
        dir_y = [0, 0, -1, 1]
        if word[index] != board[x][y]:
            return False
        else:
            if index == len(word) - 1:
                return True
            visited[x][y] =  True
            for i in range(4):
                new_x = x + dir_x[i]
                new_y = y + dir_y[i]
                if self.inbound(board, new_x, new_y) and not visited[new_x][new_y]:
                    if self.dfs(board, word, index + 1, new_x, new_y, visited):
                        return True
            visited[x][y] = False
    
    def inbound(self, board, x, y):
        return x >= 0 and x < len(board) and y >= 0 and y < len(board[0])
        