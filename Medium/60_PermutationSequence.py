"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""

class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        """
        #Time Limit Exceeded
        num = "123456789"
        self.cnt = 0
        self.res = ''
        self.dfs("", num[:n], 0, n, k)
        return self.res
    def dfs(self, tmp, nums, tmplen, numslen, k):
        if tmplen == numslen:
            self.cnt += 1
            if self.cnt == k:
                self.res = tmp
        for i in range(len(nums)):
            self.dfs(tmp + nums[i], nums[:i] + nums[i + 1:], tmplen + 1, numslen, k)
        """
        """
        num = "123456789"
        nums = list(num[:n])
        fact = 1
        x = n - 1
        for i in range(1, n):
            fact *= i
        res = []
        k -= 1
        while x > 0:
            res.append(nums[k // fact])
            nums.pop(k // fact)
            k %= fact
            fact //= x
            x -= 1
        res.append(nums[0])
        return ''.join(res)
        """
        num = "123456789"
        nums = list(num[:n])
        fact = [1]
        for i in range(1, n):
            fact.append(fact[i - 1] * i)
        res = []
        k -= 1
        for i in range(n - 1, -1, -1):
            res.append(nums[k // fact[i]])
            nums.pop(k // fact[i])
            k %= fact[i]
        return ''.join(res)
        