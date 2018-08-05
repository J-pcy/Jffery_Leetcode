"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""

class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        """
        #Time Limit Exceeded
        res = []
        queue = [s]
        visited = [s]
        flag = False
        while queue:
            string = queue.pop(0)
            if self.isValid(string):
                res.append(string)
                flag = True
            if flag:
                continue
            for i in range(len(string)):
                if string[i] != '(' and string[i] != ')':
                    continue
                new = string[:i] + string[i + 1:]
                if new not in visited:
                    visited.append(new)
                    queue.append(new)
        return res
    
    def isValid(self, s):
        cnt = 0
        for i in range(len(s)):
            if s[i] == '(':
                cnt += 1
            elif s[i] == ')':
                cnt -= 1
                if cnt < 0:
                    return False
        return cnt == 0
        """
        """
        #bfs
        res = []
        queue = {s}
        while queue:
            valid = list(filter(self.isValid, queue))
            if valid:
                return valid
            queue = {s[:i] + s[i + 1:] for s in queue for i in range(len(s))}
        return res
    
    def isValid(self, s):
        cnt = 0
        for i in range(len(s)):
            if s[i] == '(':
                cnt += 1
            elif s[i] == ')':
                cnt -= 1
                if cnt < 0:
                    return False
        return cnt == 0
        """
        #dfs
        res = []
        cnt1 = cnt2 = 0
        for i in range(len(s)):
            if s[i] == '(':
                cnt1 += 1
            elif s[i] == ')':
                if cnt1 == 0:
                    cnt2 += 1
                else:
                    cnt1 -= 1
        self.dfs(s, 0, cnt1, cnt2, res)
        return res
    
    def dfs(self, string, start, cnt1, cnt2, res):
        if cnt1 == 0 and cnt2 == 0:
            if self.isValid(string):
                res.append(string)
                return
        for i in range(start, len(string)):
            if i != start and string[i] == string[i - 1]:
                continue
            if cnt1 > 0 and string[i] == '(':
                self.dfs(string[:i] + string[i + 1:], i, cnt1 - 1, cnt2, res)
            if cnt2 > 0 and string[i] == ')':
                self.dfs(string[:i] + string[i + 1:], i, cnt1, cnt2 - 1, res)
    
    def isValid(self, s):
        cnt = 0
        for i in range(len(s)):
            if s[i] == '(':
                cnt += 1
            elif s[i] == ')':
                cnt -= 1
                if cnt < 0:
                    return False
        return cnt == 0
        