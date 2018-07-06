"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        if len(nums) == 0:
            return nums
        res = [[nums[0]]]
        for i in range(1, len(nums)):
            for j in range(len(res)):
                for k in range(len(res[0]) + 1):
                    tmp = []
                    for l in range(len(res[0])):
                        tmp.append(res[0][l])
                    tmp.insert(k, nums[i])
                    res.append(tmp)
                res.pop(0)
        return res
        """
        res = []
        self.dfs(res, [], nums, 0, len(nums))
        return res
    def dfs(self, res, tmp, nums, tmplen, numslen):
        if tmplen == numslen:
            res.append(tmp)
        for i in range(len(nums)):
            self.dfs(res, tmp + [nums[i]], nums[:i] + nums[i + 1:], tmplen + 1, numslen)
        