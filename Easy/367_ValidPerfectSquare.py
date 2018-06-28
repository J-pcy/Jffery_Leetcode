"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        """
        if num==1:
            return True
        x = num/2
        t = x*x
        while t>num:
            x /= 2
            t = x*x
        for i in xrange(x, x*2+1):
            if i*i==num:
                return True
        return False
        """
        """
        l, r = 0, num
        while l <= r:
            mid = l + (r-l)/2
            if mid*mid==num:
                return True
            elif mid*mid<num:
                l = mid+1
            elif mid*mid>num:
                r = mid-1
        return False
        """
        x = num
        while x*x>num:
            x = (x+num/x)/2
        return x*x==num
    