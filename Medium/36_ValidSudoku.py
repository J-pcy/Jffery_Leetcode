"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
"""

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        """
        for i in range(len(board)):
            tmp = [0] * len(board[0])
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    if tmp[int(board[i][j]) - 1] == 1:
                        return False
                    else:
                        tmp[int(board[i][j]) - 1] = 1
        for j in range(len(board[0])):
            tmp = [0] * len(board)
            for i in range(len(board)):
                if board[i][j] != '.':
                    if tmp[int(board[i][j]) - 1] == 1:
                        return False
                    else:
                        tmp[int(board[i][j]) - 1] = 1
        for i in range(1, len(board), 3):
            for j in range(1, len(board[0]), 3):
                tmp = [0] * 9
                for m in range(i - 1, i + 2):
                    for n in range(j - 1, j + 2):
                        if board[m][n] != '.':
                            if tmp[int(board[m][n]) - 1] == 1:
                                return False
                            else:
                                tmp[int(board[m][n]) - 1] = 1
        return True
        """
        for i in range(len(board)):
            tmp = {}
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    if board[i][j] in tmp:
                        return False
                    else:
                        tmp[board[i][j]] = 1
        for j in range(len(board[0])):
            tmp = {}
            for i in range(len(board)):
                if board[i][j] != '.':
                    if board[i][j] in tmp:
                        return False
                    else:
                        tmp[board[i][j]] = 1
        for i in range(1, len(board), 3):
            for j in range(1, len(board[0]), 3):
                tmp = {}
                for m in range(i - 1, i + 2):
                    for n in range(j - 1, j + 2):
                        if board[m][n] != '.':
                            if board[m][n] in tmp:
                                return False
                            else:
                                tmp[board[m][n]] = 1
        return True
        """
        row = [[] for _ in range(9)]
        col = [[] for _ in range(9)]
        area = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    id = i // 3 * 3 + j // 3
                    if element in row[i] or element in col[j] or element in area[id]:
                        return False
                    else:
                        row[i].append(element)
                        col[j].append(element)
                        area[id].append(element)
        return True
        """
        