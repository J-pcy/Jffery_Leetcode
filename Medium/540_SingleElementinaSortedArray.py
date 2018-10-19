"""
Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10
Note: Your solution should run in O(log n) time and O(1) space.
"""

class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == nums[mid + 1]:
                if (len(nums) - 1 - mid) % 2 == 1:
                    right = mid
                else:
                    left = mid + 1
            else:
                if mid == 0 or nums[mid] != nums[mid - 1]:
                    return nums[mid]
                if (len(nums) - 1 - mid) % 2 == 0:
                    right = mid
                else:
                    left = mid + 1
        return nums[left]
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == nums[mid ^ 1]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
        