"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        """
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                i += 1
            elif nums1[i]>nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res
        """
        #return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())
        res = []
        res_dict = {}
        for i in nums1:
            if not res_dict.has_key(i):
                res_dict[i] = 1
            else:
                res_dict[i] += 1
        for j in nums2:
            if res_dict.has_key(j) and res_dict[j]>0:
                res.append(j)
                res_dict[j] -= 1
        return res
                