"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
"""

class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        #Memory Limit Exceeded
        subsets = []
        res = []
        maxlen = 0
        self.dfs(nums, 0, [], subsets)
        for i in range(len(subsets)):
            breakFlag = False
            for j in range(len(subsets[i])):
                for k in range(j, len(subsets[i])):
                    if subsets[i][j] % subsets[i][k] != 0 and subsets[i][k] % subsets[i][j] != 0:
                        breakFlag = True
                        break
                if breakFlag:
                    break
            if not breakFlag:
                if len(subsets[i]) > maxlen:
                    maxlen = len(subsets[i])
                    res = subsets[i]
        return res
    
    def dfs(self, nums, start, tmp, subsets):
        if tmp:
            subsets.append(tmp[:])
        for i in range(start, len(nums)):
            self.dfs(nums, i + 1, tmp + [nums[i]], subsets)
        """
        """
        nums.sort()
        dp = [1] * len(nums)
        fatherIndex = [-1] * len(nums)
        mx, mxIndex = 0, -1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if 1 + dp[j] > dp[i]:
                        dp[i] = dp[j] + 1
                        fatherIndex[i] = j
            if dp[i] > mx:
                mx = dp[i]
                mxIndex = i
        res = []
        for i in range(mx):
            res.append(nums[mxIndex])
            mxIndex = fatherIndex[mxIndex]
        return res
        """
        dp = [[]]
        for n in sorted(nums):
            dp.append(max((s+[n] for s in dp if not s or n % s[-1] == 0), key=len))
        return max(dp, key=len)
        