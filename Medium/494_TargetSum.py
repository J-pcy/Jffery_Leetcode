"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:

The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""

class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        """
        #Time Limit Exceeded
        self.res = 0
        self.helper(nums, 0, S)
        return self.res
    def helper(self, nums, start, target):
        if start == len(nums):
            if target == 0:
                self.res += 1
            return
        self.helper(nums, start + 1, target + nums[start])
        self.helper(nums, start + 1, target - nums[start])
        """
        """
        dp = [{} for _ in range(len(nums))]
        return self.helper(nums, 0, S, dp)
    def helper(self, nums, start, target, dp):
        if start == len(nums):
            return target == 0
        if target in dp[start]:
            return dp[start][target]
        cnt1 = self.helper(nums, start + 1, target + nums[start], dp)
        cnt2 = self.helper(nums, start + 1, target - nums[start], dp)
        dp[start][target] = cnt1 + cnt2
        return cnt1 + cnt2
        """
        """
        dp = [{} for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        for i in range(len(nums)):
            for key in dp[i].keys():
                dp[i + 1][key + nums[i]] = dp[i + 1].get(key + nums[i], 0) + dp[i][key]
                dp[i + 1][key - nums[i]] = dp[i + 1].get(key - nums[i], 0) + dp[i][key]
        if S in dp[len(nums)]:
            return dp[len(nums)][S]
        else:
            return 0
        """
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic
        return dic.get(S, 0)
        