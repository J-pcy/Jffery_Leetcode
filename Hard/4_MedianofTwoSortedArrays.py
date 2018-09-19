"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        """
        #O((m+n)log(m+n))
        res = []
        res += nums1 + nums2
        if len(res) == 0:
            return 0
        res.sort()
        if len(res) % 2 == 1:
            return res[len(res) // 2]
        else:
            return (res[len(res) // 2 - 1] + res[len(res) // 2]) / 2.0
        """
        """
        #O(m+n)
        res = []
        m, n = 0, 0
        while m < len(nums1) and n < len(nums2):
            if nums1[m] <= nums2[n]:
                res.append(nums1[m])
                m += 1
            else:
                res.append(nums2[n])
                n += 1
        res += nums1[m:] + nums2[n:]
        if len(res) % 2 == 1:
            return res[len(res) // 2]
        else:
            return (res[len(res) // 2 - 1] + res[len(res) // 2]) / 2.0
        """
        #O(log(m+n))
        length = len(nums1) + len(nums2)
        if length % 2 == 0:
            return (self.findKth(nums1, nums2, length // 2 + 1) + self.findKth(nums1, nums2, length // 2)) / 2.0
        return self.findKth(nums1, nums2, length // 2 + 1)
    
    def findKth(self, nums1, nums2, k):
        if len(nums1) == 0:
            return nums2[k - 1]
        if len(nums2) == 0:
            return nums1[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        num1 = nums1[k // 2 - 1] if len(nums1) >= k // 2 else None
        num2 = nums2[k // 2 - 1] if len(nums2) >= k // 2 else None
        if num2 is None or (num1 is not None and num1 < num2):
            return self.findKth(nums1[k // 2:], nums2, k - k // 2)
        return self.findKth(nums1, nums2[k // 2:], k - k // 2)
        