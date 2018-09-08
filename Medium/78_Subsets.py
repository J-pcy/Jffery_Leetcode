"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, startindex, tmp, res):
        res.append(tmp)
        for i in range(startindex, len(nums)):
            self.dfs(nums, i + 1, tmp + [nums[i]], res)
        """
        """
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, index, tmp, res):
        if index == len(nums):
            res.append(tmp)
            return
        self.dfs(nums, index + 1, tmp, res)
        self.dfs(nums, index + 1, tmp + [nums[index]], res)
        """
        """
        res = []
        queue = [[]]
        nums.sort()
        while queue:
            tmp = queue.pop(0)
            res.append(tmp)
            for i in range(len(nums)):
                if len(tmp) == 0 or tmp[-1] < nums[i]:
                    tmp.append(nums[i])
                    queue.append(tmp[:])
                    tmp.pop()
        return res
        """
        res = [[]]
        for num in nums:
            res += [item + [num] for item in res]
        return res
        