"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""

class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        import math
        res = math.ceil(len(B) / len(A))
        if self.isSubstring(A * res, B):
            return res
        elif self.isSubstring(A * (res + 1), B):
            return res + 1
        else:
            return -1
    
    def isSubstring(self, a, b):
        for i in range(len(a) - len(b) + 1):
            if a[i] == b[0]:
                if a[i:i+len(b)] ==  b:
                    return True
        return False
        """
        #can not ac
        lenA = len(A)
        lenB = len(B)
        for i in range(lenA):
            j = 0
            while j < lenB and A[(i + j) % lenA] == B[j]:
                j += 1
            if j == lenB:
                return (i + j - 1) // lenA + 1
        return -1
        """
        