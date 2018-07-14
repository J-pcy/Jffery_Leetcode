"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for i in range(n)] for j in range(n)]
        i = 1
        left, right, top, bottom = 0, n - 1, 0, n - 1
        row = col = 0
        while i <= n * n:
            while i <= n * n and col <= right:
                res[row][col] = i
                i += 1
                col += 1
            top += 1
            col -= 1
            row += 1
            while i <= n * n and row <= bottom:
                res[row][col] = i
                i += 1
                row += 1
            right -= 1
            row -= 1
            col -= 1
            while i <= n * n and col >= left:
                res[row][col] = i
                i += 1
                col -= 1
            bottom -= 1
            col += 1
            row -= 1
            while i <= n * n and row >= top:
                res[row][col] = i
                i += 1
                row -= 1
            left += 1
            row += 1
            col += 1
        return res
        