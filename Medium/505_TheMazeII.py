"""
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

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

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1

Explanation: There is no way for the ball to stop at the destination.

 

Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
"""

class Solution:
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        """
        import Queue
        dists = [[sys.maxsize for _ in range(len(maze[0]))] for _ in range(len(maze))]
        dircs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        que = Queue.Queue()
        que.put(start)
        dists[start[0]][start[1]] = 0
        while not que.empty():
            node = que.get()
            for dirc in dircs:
                x = node[0]
                y = node[1]
                dist = dists[x][y]
                while x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0]) and maze[x][y] != 1:
                    x += dirc[0]
                    y += dirc[1]
                    dist += 1
                x -= dirc[0]
                y -= dirc[1]
                dist -= 1
                if dist < dists[x][y]:
                    dists[x][y] = dist
                    if x != destination[0] or y != destination[1]:
                        que.put([x, y])
        return dists[destination[0]][destination[1]] if dists[destination[0]][destination[1]] != sys.maxsize else -1
        """
        """
        [sx, sy] = start
        [ex, ey] = destination
        if not any(maze):
            return -1
        m, n = len(maze), len(maze[0])
        visited = {(sx, sy) : 0}
        q = collections.deque([(0, sx, sy)])
        while q:
            (pd, px, py) = q.popleft()
            for dx, dy in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
                d, x, y = pd, px, py
                while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] == 0:
                    x, y, d = x + dx, y + dy, d + 1
                if (x, y) not in visited or visited[(x, y)] > d:
                    visited[(x, y)] = d
                    if (x, y) == (ex, ey):
                        continue
                    q.append((d, x, y))
        return visited.get((ex, ey), -1)
        """
        dest = tuple(destination)
        m = len(maze)
        n = len(maze[0])
        visited = {}
        q = []
        heapq.heappush(q, (0, tuple(start)))
        while q:
            length, cur = heapq.heappop(q)
            if cur in visited and visited[cur] <= length:
                continue
            visited[cur] = length
            if cur == dest:
                return length
            for dirc in [(-1, 0), (1, 0), (0,-1), (0,1)]:
                x = cur[0]
                y = cur[1]
                dist = 0
                while 0 <= x + dirc[0] < len(maze) and 0 <= y + dirc[1] < len(maze[0]) and maze[x + dirc[0]][y + dirc[1]] == 0:
                    x += dirc[0]
                    y += dirc[1]
                    dist += 1
                l, np = dist, (x, y)
                heapq.heappush(q, (length + l, np))
        return -1
        