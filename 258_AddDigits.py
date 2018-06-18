"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        """
        while num>9:
            num_new = num
            num = 0
            while num_new:
                num += num_new%10
                num_new /= 10
        return num
        """
        if num==0:
            return 0
        return num%9 if (num%9)!=0 else 9
    