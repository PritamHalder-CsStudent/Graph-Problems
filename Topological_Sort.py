# Topological sort perform on Directed Acyclic Graph (DAG)
# Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices
# such that for every directed edge u -> v, vertex u comes before v in the ordering.

# Examples:

# Input: V = 4, E = 3, edges[][] = [[3, 0], [1, 0], [2, 0]]
# Output: true

# Explanation: The output true denotes that the order is valid. 
# Few valid Topological orders for the given graph are:
# [3, 2, 1, 0]
# [1, 2, 3, 0]
# [2, 3, 1, 0]

# Approach:
# Using stack data structure , we store the node at stack after when call return 

class Solution:
    def dfs(self,adj,node,visited,stack):
        visited[node]=1
        # call for node adjacent node (neighobur node call)
        for adj_node in adj[node]:
            if visited[adj_node]!=1:
                self.dfs(adj,adj_node,visited,stack)
        stack.append(node)
    
            
    def topoSort(self, V, edges):
        # convert edges into adjaceny list 
        adj=[[] for i in range(V)]
        for u,v in edges:
            adj[u].append(v)
        
        visited=[0]*V
        stack=[]
        ans=[]
        # call dfs for all nodes that are not visited
        for node in range(V):
            if visited[node]!=1:
                self.dfs(adj,node,visited,stack)
        
        while stack:
            ans.append(stack[-1])
            stack.pop()
        
        return ans    
            
        