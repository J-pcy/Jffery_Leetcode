"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
"""

"""
class NumArray:
    def __init__(self, nums):
        self.nums = nums

    def update(self, i, val):
        self.nums[i] = val

    def sumRange(self, i, j):
        return sum(self.nums[i: j + 1])
"""
"""
#Time Limit Exceeded
class NumArray:
    def __init__(self, nums):
        if len(nums) > 0:
            self.sum = []
            self.nums = nums
            self.sum.append(nums[0])
            for i in range(1, len(nums)):
                self.sum.append(self.sum[i - 1] + nums[i])

    def update(self, i, val):
        for index in range(i, len(self.nums)):
            self.sum[index] = self.sum[index] - self.nums[i] + val
        self.nums[i] = val

    def sumRange(self, i, j):
        return self.sum[j] - self.sum[i - 1] if i > 0 else self.sum[j]
"""
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.num = [0] * (len(nums) + 1)
        self.bit = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.update(i, nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.num[i + 1]
        index = i + 1
        while index < len(self.num):
            self.bit[index] += diff
            index += index & -index
        self.num[i + 1] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.getSum(j + 1) - self.getSum(i)
    
    def getSum(self, i):
        res = 0
        index = i
        while index > 0:
            res += self.bit[index]
            index -= index & -index
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)