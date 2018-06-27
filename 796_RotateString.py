"""
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.
"""

class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        """
        alist = list(A)
        blist = list(B)
        length = len(alist)
        if length != len(blist):
            return False
        while length >= 0:
            flag = 0
            for i in range(len(alist)):
                if alist[i] != blist[i]:
                    flag = 1
                    break
            if flag == 0:
                return True
            alist.append(alist.pop(0))
            length -= 1
        return False
        """
        if len(A) != len(B):
            return False
        if A == B:
            return True
        for i in range(len(A)):
            if A[i:] + A[:i] == B:
                return True
        return False
                