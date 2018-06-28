"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        res = []
        index = 0
        while index<len(nums):
            if nums[index]!=nums[nums[index]-1]:
                tmp = nums[index]
                nums[index] = nums[nums[index]-1]
                nums[tmp-1] = tmp
                index -= 1
            index += 1
        for i in xrange(len(nums)):
            if nums[i]!=i+1:
                res.append(i+1)
        return res
        """
        res = []
        for i in xrange(len(nums)):
            index = abs(nums[i])-1
            nums[index] = -abs(nums[index])
        for i in xrange(len(nums)):
            if nums[i]>0:
                res.append(i+1)
        return res
    