"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""

class Solution:
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        if len(A) == 0 or len(A[0]) == 0:
            return []
        res = []
        for i in range(len(A)):
            tmp = []
            for k in range(len(B[0])):
                mul = 0
                for j in range(len(A[0])):
                    mul += A[i][j] * B[j][k]
                tmp.append(mul)
            res.append(tmp)
        return res
        """
        """
        if len(A) == 0 or len(A[0]) == 0:
            return []
        res = []
        for i in range(len(A)):
            tmp = []
            for k in range(len(B[0])):
                mul = 0
                for j in range(len(A[0])):
                    if A[i][j] != 0 and B[j][k] != 0:
                        mul += A[i][j] * B[j][k]
                tmp.append(mul)
            res.append(tmp)
        return res
        """
        if len(A) == 0 or len(A[0]) == 0:
            return []
        res = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    continue
                for k in range(len(B[0])):
                    if B[j][k] != 0:
                        res[i][k] += A[i][j] * B[j][k]
        return res
        