"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #return list(set(nums1) & set(nums2))
        """
        res = []
        for i in nums1:
            if i not in res and i in nums2:
                    res.append(i)
        return res
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
                if nums1[i] not in res:
                    res.append(nums1[i])
                i += 1
                j += 1
        return res
        