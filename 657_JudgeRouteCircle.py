"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
"""

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        cnt1 = 0
        cnt2 = 0
        for i in moves:
            if i=='R':
                cnt1 += 1
            elif i=='L':
                cnt1 -= 1
            elif i=='U':
                cnt2 += 1
            elif i=='D':
                cnt2 -= 1
        return cnt1==0 and cnt2==0
        