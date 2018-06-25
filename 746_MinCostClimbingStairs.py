"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
"""

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        """
        res_list = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            res_list.append(cost[i] + min(res_list[i-1], res_list[i-2]))
        return min(res_list[-1], res_list[-2])
        """
        """
        dp0, dp1, dp2 = 0, 0, 0
        for i in range(2, len(cost) + 1):
            dp2 = min(dp0 + cost[i - 2], dp1 + cost[i - 1])
            dp0, dp1 = dp1, dp2
        return dp2
        """
        dp0, dp1 = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp2 = cost[i] + min(dp0, dp1)
            dp0, dp1 = dp1, dp2
        return min(dp1, dp0)
        