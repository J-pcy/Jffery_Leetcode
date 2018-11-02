"""
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Example 1:

Input: 1
Output: []
Example 2:

Input: 37
Output:[]
Example 3:

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Example 4:

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
"""

class Solution:
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        """
        #Time Limit Exceeded
        res = []
        self.helper(n, 2, [], res)
        return res
    def helper(self, n, start, tmp, res):
        if n == 1:
            if len(tmp) > 1:
                res.append(tmp)
        else:
            for i in range(start, n + 1):
                if n % i == 0:
                    self.helper(n // i, i, tmp + [i], res)
        """
        """
        res = []
        self.helper(n, 2, [], res)
        return res
    def helper(self, n, start, tmp, res):
        for i in range(start, int(math.sqrt(n)) + 1):
            if n % i == 0:
                res.append(tmp + [i, n // i])
                self.helper(n // i, i, tmp + [i], res)
        """
        stack = [(n, 2, [])]
        res = []
        while stack:
            num, i, tmp = stack.pop()
            while i * i <= num:
                if num % i == 0:
                    res.append(tmp + [i, num // i])
                    stack.append((num // i, i, tmp + [i]))
                i += 1
        return res
        