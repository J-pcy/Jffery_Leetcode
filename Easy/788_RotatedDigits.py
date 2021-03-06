"""
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].
"""

class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        """
        list1 = [2, 5, 6, 9]
        list2 = [0, 1, 8]
        res = 0
        for i in range(1, N + 1):
            flag1 = 0
            flag2 = 0
            while i:
                if i % 10 in list1:
                    flag1 = 1
                if i % 10 not in list1 and i % 10 not in list2:
                    flag2 = 1
                    break
                i = i // 10
            if flag1 and not flag2:
                res += 1
        return res
        """
        set1 = set([0, 1, 8])
        set2 = set([0, 1, 2, 5, 6, 8, 9])
        res = 0
        for i in range(1, N + 1):
            s = set(int(x) for x in str(i))
            if s.issubset(set2) and not s.issubset(set1):
                res += 1
        return res
        