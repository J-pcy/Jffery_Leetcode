"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        res = []
        nums.sort()
        visited = [False] * len(nums)
        self.dfs(nums, 0, [], visited, res)
        return res
    def dfs(self, nums, start, tmp, visited, res):
        res.append(tmp)
        for i in range(start, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue
            visited[i] = True
            self.dfs(nums, i + 1, tmp + [nums[i]], visited, res)
            visited[i] = False
        """
        """
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res
    def dfs(self, nums, start, tmp, res):
        res.append(tmp)
        for i in range(start, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and i > start:
                continue
            self.dfs(nums, i + 1, tmp + [nums[i]], res)
        """
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != last:
                last = nums[i]
                size = len(res)
            for j in range(len(res) - size, len(res)):
                res.append(res[j] + [nums[i]])
        return res
        