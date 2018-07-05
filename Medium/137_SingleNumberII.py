"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        bits = [0] * 33
        res = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                bits[32] += 1
                nums[i] = -nums[i]
            for j in range(32):
                bits[j] += nums[i] >> j & 0x1
        print(bits)
        for i in range(32):
            res |= bits[i] % 3 << i
        return res if bits[32] % 3 == 0 else -res
        """
        low = high = 0
        for i in range(len(nums)):
            low = low ^ nums[i] & ~high
            high = high ^ nums[i] & ~low
        return low
    