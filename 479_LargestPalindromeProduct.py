"""
Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

Example:

Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:

The range of n is [1,8].
"""

class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1: return 9
        if n==2: return 987
        for i in xrange(2, 9*10**(n-1)):
            high=(10**n)-i
            low=int(str(high)[::-1])
            if i**2-4*low < 0: continue
            if (i**2-4*low)**.5 == int((i**2-4*low)**.5):
                return (low+10**n*(10**n-i))%1337
                