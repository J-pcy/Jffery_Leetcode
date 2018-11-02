"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
"""

class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        """
        return self.helper(n, n)
    
    def helper(self, m, n):
        if m == 0:
            return ['']
        if m == 1:
            return ['0', '1', '8']
        tmp = self.helper(m - 2, n)
        res = []
        for t in tmp:
            if m != n:
                res.append('0' + t + '0')
            res.append('1' + t + '1')
            res.append('6' + t + '9')
            res.append('8' + t + '8')
            res.append('9' + t + '6')
        return res
        """
        t0 = ['']
        t1 = ['0', '1', '8']
        res = t0
        if n % 2 == 1:
            res = t1
        for i in range(n % 2 + 2, n + 1, 2):
            tmp = []
            for r in res:
                if i != n:
                    tmp.append('0' + r + '0')
                tmp.append('1' + r + '1')
                tmp.append('6' + r + '9')
                tmp.append('8' + r + '8')
                tmp.append('9' + r + '6')
            res = tmp
        return res
        