"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """
        red = white = blue = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                red += 1
            if nums[i] == 1:
                white += 1
            if nums[i] == 2:
                blue += 1
        for i in range(red):
            nums[i] = 0
        for i in range(red, red + white):
            nums[i] = 1
        for i in range(red + white, red + white + blue):
            nums[i] = 2
        """
        """
        cnt = [0] * 3
        for i in range(len(nums)):
            cnt[nums[i]] += 1
        index = 0
        for i in range(3):
            for j in range(cnt[i]):
                nums[index] = i
                index += 1
        """
        """
        red, blue = 0, len(nums) - 1
        index = 0
        while index <= blue:
            if nums[index] == 0:
                nums[red], nums[index] = nums[index], nums[red]
                red += 1
            elif nums[index] == 2:
                nums[blue], nums[index] = nums[index], nums[blue]
                index -= 1
                blue -= 1
            index += 1
        """
        red = white = blue = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                red += 1
                white += 1
                blue += 1
                nums[blue] = 2
                nums[white] = 1
                nums[red] = 0
            elif nums[i] == 1:
                white += 1
                blue += 1
                nums[blue] = 2
                nums[white] = 1
            else:
                blue += 1
                nums[blue] = 2
                