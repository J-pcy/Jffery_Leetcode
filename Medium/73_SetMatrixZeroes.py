"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        """
        #O(mn)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        tmp = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    tmp.append([i, j])
        for zero in range(len(tmp)):
            for i in range(len(matrix)):
                matrix[i][tmp[zero][1]] = 0
            for j in range(len(matrix[0])):
                matrix[tmp[zero][0]][j] = 0
        """
        #O(m + n)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        row = [1] * len(matrix)
        col = [1] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0
        for i in range(len(row)):
                for j in range(len(col)):
                    if row[i] == 0 or col[j] == 0:
                        matrix[i][j] = 0
        """
        #O(1)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        row0 = False
        col0 = False
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                row0 = True
                break
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col0 = True
                break
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, len(matrix)):
                for j in range(1, len(matrix[0])):
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
        if row0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if col0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        """
        