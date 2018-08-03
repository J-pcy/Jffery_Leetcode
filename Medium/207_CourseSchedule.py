"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        """
        indegrees = [0] * numCourses
        edges = [[] for i in range(numCourses)]
        for i in range(len(prerequisites)):
            indegrees[prerequisites[i][0]] += 1
            edges[prerequisites[i][1]].append(prerequisites[i][0])
        queue = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        cnt = 0
        while queue:
            course = queue.pop(0)
            cnt += 1
            for i in range(len(edges[course])):
                indegrees[edges[course][i]] -= 1
                if indegrees[edges[course][i]] == 0:
                    queue.append(edges[course][i])
        return cnt == numCourses
        """
        visited = [0] * numCourses
        edges = [[] for i in range(numCourses)]
        for i in range(len(prerequisites)):
            edges[prerequisites[i][1]].append(prerequisites[i][0])
        for i in range(numCourses):
            if not self.dfs(edges, visited, i):
                return False
        return True
    def dfs(self, graph, visited, index):
        if visited[index] == 1:
            return False
        if visited[index] == -1:
            return True
        visited[index] = 1
        for i in graph[index]:
            if not self.dfs(graph, visited, i):
                return False
        visited[index] = -1
        return True
        