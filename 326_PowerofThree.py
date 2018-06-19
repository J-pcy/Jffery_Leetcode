"""
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        while n>0 and n%3==0:
            n /= 3
        return n==1
        """
        import math
        return n>0 and int(math.log10(n)/math.log10(3))-math.log10(n)/math.log10(3)==0
        