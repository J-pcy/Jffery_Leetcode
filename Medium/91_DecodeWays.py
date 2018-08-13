"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        if len(s) == 0 or len(s) > 0 and s[0] == '0':
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            else:
                dp[i] = 0
            if i > 1 and int(s[i - 2:i]) <= 26 and int(s[i - 2:i - 1]) > 0:
                dp[i] += dp[i - 2]
        return dp[-1]
        """
        if len(s) == 0 or len(s) > 0 and s[0] == '0':
            return 0
        dp1 = 1
        for i in range(1, len(s) + 1):
            if s[i - 1] != '0':
                dp = dp1
            else:
                dp = 0
            if i > 1 and int(s[i - 2:i]) <= 26 and int(s[i - 2:i - 1]) > 0:
                dp += dp2
            dp2 = dp1
            dp1 = dp
        return dp
        