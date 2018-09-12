"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        """
        #greedy
        scur, pcur, sstar, pstar = 0, 0, 0, -1
        while scur < len(s):
            if pcur < len(p) and (s[scur] == p[pcur] or p[pcur] == '?'):
                scur += 1
                pcur += 1
            elif pcur < len(p) and p[pcur] == '*':
                pstar = pcur
                sstar = scur
                pcur += 1
            elif pstar != -1:
                pcur = pstar + 1
                sstar += 1
                scur = sstar
            else:
                return False
        while pcur < len(p) and p[pcur] == '*':
            pcur += 1
        return pcur == len(p)
        """
        """
        #memo search
        return self.memodfs(s, 0, p, 0, {})
    
    def memodfs(self, s, sstart, p, pstart, memo):
        if (sstart, pstart) in memo:
            return memo[(sstart, pstart)]
        if len(s) == sstart:
            for i in range(pstart, len(p)):
                if p[i] != '*':
                    return False
            return True
        if len(p) == pstart:
            return False
        if p[pstart] != '*':
            match = (s[sstart] == p[pstart] or p[pstart] == '?') and self.memodfs(s, sstart + 1, p, pstart + 1, memo)
        else:
            match = self.memodfs(s, sstart + 1, p, pstart, memo) or self.memodfs(s, sstart, p, pstart + 1, memo)
        memo[(sstart, pstart)] = match
        return match
        """
        #dp
        slen = len(s)
        plen = len(p)
        dp = [[False for i in range(plen + 1)] for j in range(slen + 1)]
        dp[0][0] = True
        for j in range(1, plen + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        for i in range(1, slen + 1):
            for j in range(1, plen + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '?')
        return dp[-1][-1]
        