"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        """
        res = []
        self.dfs(n, k, 1, [], res)
        return res
    
    def dfs(self, n, k, index, tmp, res):
        if len(tmp) == k:
            res.append(tmp)
            return
        for i in range(index, n + 1):
            self.dfs(n, k, i + 1, tmp + [i], res)
        """
        res = []
        tmp = [0] * k
        i = 0
        while i >= 0:
            tmp[i] += 1
            if tmp[i] > n:
                i -= 1
            elif i == k - 1:
                res.append(tmp[:])
            else:
                i += 1
                tmp[i] = tmp[i - 1]
        return res
    