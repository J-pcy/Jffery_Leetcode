"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        """
        if len(triangle) == 0 or len(triangle[0]) == 0:
            return 0
        pathsum = []
        pathsum.append([triangle[0][0]])
        for i in range(1, len(triangle)):
            tmp = []
            for j in range(len(triangle[i])):
                if j == 0:
                    tmp.append(pathsum[i - 1][j] + triangle[i][j])
                elif j == len(triangle[i]) - 1:
                    tmp.append(pathsum[i - 1][j - 1] + triangle[i][j])
                else:
                    tmp.append(min(pathsum[i - 1][j - 1], pathsum[i - 1][j]) + triangle[i][j])
            pathsum.append(tmp)
        return min(pathsum[-1])
        """
        if len(triangle) == 0 or len(triangle[0]) == 0:
            return 0
        pathsum = [x for x in triangle[-1]]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                pathsum[j] = min(pathsum[j], pathsum[j + 1]) + triangle[i][j]
        return pathsum[0]
        