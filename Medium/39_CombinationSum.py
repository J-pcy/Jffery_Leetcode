"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """
        candidates, res, stack, lenth = sorted(set(candidates)), [], [(0, [], target)], len(candidates)
        while stack:
            i, temp, tar=stack.pop()
            while i < lenth and tar > 0:
                if candidates[i]==tar: 
                    res += temp + [candidates[i]],
                stack += (i, temp + [candidates[i]], tar - candidates[i]),
                i += 1
        return res
        """
        self.res = []
        candidates.sort()
        self.dfs(candidates, [], target, 0)
        return self.res
    
    def dfs(self, candidates, tmp, target, index):
        if target == 0:
            self.res.append(tmp)
        for i in range(index, len(candidates)):
            if candidates[i] > target:
                return
            self.dfs(candidates, tmp + [candidates[i]], target - candidates[i], i)
        