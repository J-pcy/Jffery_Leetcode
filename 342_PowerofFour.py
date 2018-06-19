"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

Credits:
Special thanks to @yukuairoy for adding this problem and creating all test cases.
"""

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        """
        while num>0 and num%4==0:
            num /= 4
        return num==1
        """
        import math
        return num>0 and int(math.log10(num)/math.log10(4))-math.log10(num)/math.log10(4)==0