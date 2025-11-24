# Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, 
# check whether it contains any cycle or not.
# The graph is represented as a 2D vector edges[][], where each entry edges[i] = [u, v] 
# denotes an edge from verticex u to v.

# Input: V = 4, edges[][] = [[0, 1], [1, 2], [2, 0], [2, 3]]
#Output: true
# Explanation: The diagram clearly shows a cycle 0 → 1 → 2 → 0

# Approach:
# 1. Using visited and pathvisited array we can esaily check the directed graph contain cycle or not 
# 2. DFS approach we solve it 

class Solution:
    def DetectCycle(self,adj,curr,visited,pathvisited):
        visited[curr]=True
        pathvisited[curr]=True
        
       # traverse for all adjacent nodes
        for adj_node in adj[curr]:
            if visited[adj_node]==False: # when the node is not visited 
                if self. DetectCycle(adj,adj_node,visited,pathvisited):
                    return True
            # if the node has been previously visited but it has to be visited on the same path    
            elif pathvisited[adj_node]==True:   # when the same path we back to starting node then we can say cycle present
                return True
                
                
        pathvisited[curr]=False        # when i go back from recursion the pathvisited becomes False (backtracking)
        return False
        
        
    def isCyclic(self, V, edges):
        # convert edges into adjaceny list
        adj=[[] for i in range(V)]
        for u,v in edges:
            adj[u].append(v)
            
        # Initialize the visited and pathvisited array
        visited=[False]*V
        pathvisited=[False]*V
       
        
        # call for all nodes in the graphs 
        for node in range(V):
            if visited[node]==False:
                if self. DetectCycle(adj,node,visited,pathvisited):
                    return True
        
        return False            
                