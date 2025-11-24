# DSA - Depth first search 
# Depth first search go to depth of the tree and
# explore all the node using stack data structure using  LIFO method 

# Take graph(undirected) input using adjacency list: adj[][] = [[2, 3, 1], [0], [0, 4], [0], [2]]
# output of DFS traversal: [0, 2, 4, 3, 1]


class Solution:
    def callDfs(self,adj,currNode,res,visited):
        visited[currNode]=True
        res.append(currNode)
        for adj_node in adj[currNode]:    # take connected node to the currNode 
            if not visited[adj_node]:
                self.callDfs(adj,adj_node,res,visited)  # recursive call for 
                
    def dfs(self, adj):
        n=len(adj)             # give number of node present in the adjacency list
        currNode=0
        res=[]                 # result array to store output  
        visited=[False]*n      # create a visited array to check visited or not 
        
        # this is for disconnected graph
        for i in range(n):    
            if not visited[i]:    
                self.callDfs(adj,i,res,visited)    
        return res
    


# we can work on DFS using visited set 
class Solution:
    def callDfs(self, adj, currNode, res, visited):
        visited.add(currNode)
        res.append(currNode)

        for adj_node in adj[currNode]:
            if adj_node not in visited:
                self.callDfs(adj, adj_node, res, visited)

    def dfs(self, adj):
        visited = set()  # declear visited as set 
        res = []
        self.callDfs(adj, 0, res, visited)
        return res    
    