"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
"""

class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        num = 1
        while n > 0:
            if self.isUgly(num):
                n -= 1
            num += 1
        return num - 1
    
    def isUgly(self, num):
        while num >= 2:
            if num % 2 == 0:
                num //= 2
            elif num % 3 == 0:
                num //= 3
            elif num % 5 == 0:
                num //= 5
            else:
                return False
        return num == 1
        """
        i2, i3, i5 = 0, 0, 0
        res = [1]
        while len(res) < n:
            m2 = res[i2] * 2
            m3 = res[i3] * 3
            m5 = res[i5] * 5
            m = min(m2, m3, m5)
            if m2 == m:
                i2 += 1
            if m3 == m:
                i3 += 1
            if m5 == m:
                i5 += 1
            res.append(m)
        return res[-1]
        