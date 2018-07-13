"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        res = []
        used = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        m = n = 0
        while len(res) < len(matrix) * len(matrix[0]):
            while m < len(matrix[0]) and used[n][m] == 0:
                res.append(matrix[n][m])
                used[n][m] = 1
                m += 1
            m -= 1
            n += 1
            while n < len(matrix) and used[n][m] == 0:
                res.append(matrix[n][m])
                used[n][m] = 1
                n += 1
            n -= 1
            m -= 1
            while m >= 0 and used[n][m] == 0:
                res.append(matrix[n][m])
                used[n][m] = 1
                m -= 1
            m += 1
            n -= 1
            while n >= 0 and used[n][m] == 0:
                res.append(matrix[n][m])
                used[n][m] = 1
                n -= 1
            n += 1
            m += 1
        return res
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        res = []
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
        