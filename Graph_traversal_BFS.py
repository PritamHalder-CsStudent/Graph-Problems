# BFS- Breath First Search 
# In Bfs traversal visit the node which is close to currNode 
# Bfs use queue data structure FIFO manner 

# Input: adj[][] = [[2, 3, 1], [0], [0, 4], [0], [2]] adjacency list
#output : [0, 2, 3, 1, 4]


from collections import deque
class Solution:
    def bfs(self, adj):
        currNode=0
        q=deque()
        q.append(currNode)
        res=[]
        visited=set()
        visited.add(currNode)   # mark visited when pushing into queue
        while q:
            node=q.popleft()
            res.append(node)
        
            for adj_node in adj[node]:
                if adj_node not in visited:  # check the adj_node that present in visited 
                    visited.add(adj_node) 
                    q.append(adj_node)
        
        return res   