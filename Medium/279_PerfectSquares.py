"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        res = [0] * (n + 1)
        num = 1
        squares = []
        queue = []
        while num * num <= n:
            squares.append(num * num)
            queue.append(num * num)
            res[num * num] = 1
            num += 1
        while queue:
            num1 = queue.pop(0)
            for num2 in squares:
                if num1 + num2 <= n and res[num1 + num2] == 0:
                    res[num1 + num2] = res[num1] + 1
                    queue.append(num1 + num2)
            if res[n] != 0:
                break
        return res[n]
        """
        """
        #Time Limit Exceeded
        dp = [n] * (n + 1)
        dp[0] = 0
        for i in range(n + 1):
            j = 1
            while j * j <= n - i:
                dp[i + j * j] = min(dp[i + j * j], dp[i] + 1)
                j += 1
        return dp[n]
        """
        import math
        while n % 4 == 0:
            n /= 4
        while n % 8 == 7:
            return 4
        num1 = 0
        while num1 * num1 <= n:
            num2 = int(math.sqrt(n - num1 * num1))
            if num1 * num1 + num2 * num2 == n:
                if num1 > 0 and num2 > 0:
                    return 2
                elif num1 == 0 and num2 == 0:
                    return 0
                else:
                    return 1
            num1 += 1
        return 3
    