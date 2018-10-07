"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        """
        _s = []
        _t = []
        for s in S:
            if s == '#':
                if _s:
                    _s.pop()
            else:
                _s.append(s)
        for t in T:
            if t == '#':
                if _t:
                    _t.pop()
            else:
                _t.append(t)
        return _s == _t
        """
        scnt, tcnt = 0, 0
        si, ti = len(S) - 1, len(T) - 1
        while si >= 0 or ti >= 0:
            while si >= 0:
                if S[si] == '#':
                    scnt += 1
                    si -= 1
                elif scnt > 0:
                    scnt -= 1
                    si -= 1
                else:
                    break
            while ti >= 0:
                if T[ti] == '#':
                    tcnt += 1
                    ti -= 1
                elif tcnt > 0:
                    tcnt -= 1
                    ti -= 1
                else:
                    break
            if si >= 0 and ti >= 0 and S[si] != T[ti]:
                return False
            if si >= 0 and ti < 0 or si < 0 and ti >= 0:
                return False
            si -= 1
            ti -= 1
        return True