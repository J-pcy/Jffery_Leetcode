"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        target_row = 0
        for i in range(len(matrix)):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                target_row = i
                break
        start = 0
        end = len(matrix[target_row]) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if matrix[target_row][mid] == target:
                return True
            if matrix[target_row][mid] > target:
                end = mid
            elif matrix[target_row][mid] < target:
                start = mid
        if matrix[target_row][start] == target or matrix[target_row][end] == target:
            return True
        return False
        """
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        start, end = 0, len(matrix) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if matrix[mid][0] > target:
                end = mid
            else:
                start = mid
        if target >= matrix[start][0] and target < matrix[end][0]:
            target_row = start
        elif target >= matrix[end][0] and target <= matrix[end][-1]:
            target_row = end
        else:
            return False
        start, end = 0, len(matrix[target_row]) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if matrix[target_row][mid] == target:
                return True
            if matrix[target_row][mid] < target:
                start = mid
            else:
                end = mid
        if matrix[target_row][start] == target or matrix[target_row][end] == target:
            return True
        return False
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if matrix[mid // n][mid % n] == target:
                return True
            if matrix[mid // n][mid % n] < target:
                start = mid
            else:
                end = mid
        if matrix[start // n][start % n] == target or matrix[end // n][end % n] == target:
            return True
        return False
    