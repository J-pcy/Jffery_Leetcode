"""
Implement pow(x, n), which calculates x raised to the power n (x^n).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
"""

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        """
        #Time Limit Exceeded
        res = 1
        if n == 0 and x != 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        for i in range(n):
            res *= x
        return res
        """
        """
        res = 1
        if n == 0 and x != 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        base = x
        while n:
            if n % 2 == 1:
                res *= base
            base *= base
            n //= 2
        return res
        """
        if n < 0:
            x = 1 / x
            n = -n
        res = self.power(x, n)
        return res
    
    def power(self, x, n):
        if n == 0:
            return 1
        if n % 2 == 0:
            tmp = self.power(x, n // 2)
            return tmp * tmp
        else:
            tmp = self.power(x, n // 2)
            return tmp * tmp * x
        