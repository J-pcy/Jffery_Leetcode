"""
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

 

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true

Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false

Explanation: There is no way for the ball to stop at the destination.

 

Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
"""

class Solution:
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        if len(maze) == 0 or len(maze[0]) == 0:
            return True
        self.dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dp = [[-1 for _ in range(len(maze[0]))] for _ in range(len(maze))]
        return self.helper(maze, dp, start, destination)
    
    def helper(self, maze, dp, start, destination):
        if start == destination:
            return True
        if dp[start[0]][start[1]] != -1:
            return dp[start[0]][start[1]]
        res = False
        maze[start[0]][start[1]] = -1
        for dir in self.dir:
            x = start[0]
            y = start[1]
            while x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0]) and maze[x][y] != 1:
                x += dir[0]
                y += dir[1]
            x -= dir[0]
            y -= dir[1]
            if maze[x][y] != -1:
                res |= self.helper(maze, dp, [x, y], destination)
        dp[start[0]][start[1]] = res
        return res
        