"""
Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 10^4. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example 1:

Input:
org: [1,2,3], seqs: [[1,2],[1,3]]

Output:
false

Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
Example 2:

Input:
org: [1,2,3], seqs: [[1,2]]

Output:
false

Explanation:
The reconstructed sequence can only be [1,2].
Example 3:

Input:
org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]

Output:
true

Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
Example 4:

Input:
org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]

Output:
true
UPDATE (2017/1/8):
The seqs parameter had been changed to a list of list of strings (instead of a 2d array of strings). Please reload the code definition to get the latest changes.
"""

class Solution:
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        if not org and seqs or not seqs and org:
            return False
        n = len(org)
        adjGraph = {}
        indegrees = [0] * (n + 1)
        for seq in seqs:
            for i in range(len(seq)):
                if seq[i] not in adjGraph:
                    adjGraph[seq[i]] = []
                if i < len(seq) - 1:
                    if seq[i + 1] < 1 or seq[i + 1] > n:
                        return False
                    adjGraph[seq[i]].append(seq[i + 1])
                    indegrees[seq[i + 1]] += 1
        if len(adjGraph) != n:
            return False
        que = collections.deque()
        for i in range(1, n + 1):
            if indegrees[i] == 0:
                que.append(i)
        index = 0
        while que:
            if len(que) != 1:
                return False
            node = que.popleft()
            if org[index] != node:
                return False
            for nextNode in adjGraph[node]:
                indegrees[nextNode] -= 1
                if indegrees[nextNode] == 0:
                    que.append(nextNode)
            index += 1
        return index == n
        