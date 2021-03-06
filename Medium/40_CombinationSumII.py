"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """
        self.res = []
        candidates.sort()
        self.dfs(candidates, [], target, 0)
        return self.res
    
    def dfs(self, candidates, tmp, target, index):
        if target == 0:
            return self.res.append(tmp)
        for i in range(index, len(candidates)):
            if target < candidates[i]:
                return
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates, tmp + [candidates[i]], target - candidates[i], i + 1)
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
    
    def dfs(self, candidates, target, start, tmp, res):
        if target == 0:
            res.append(tmp[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            self.dfs(candidates, target - candidates[i], i + 1, tmp + [candidates[i]], res)
        