# Detect cycle in a undirected cycle 
# Here, we use DFS method to find a cycle 

# if neighbour node(adjacent) not equal to parent node then we can tell cycle is present 


class Solution:
    def detectCycle(self,adj,curr,parent,visited):
        visited.add(curr)
        for adj_node in adj[curr]:
            if adj_node not in visited:
                visited.add(adj_node)
                if self.detectCycle(adj,adj_node,curr,visited): #
                    return True
            elif adj_node !=parent:
                return True       # cycle found
        
        return False
        
        
def isCycle(self, V, edges):
    # convert edges into adjacency list 
	adj = [[] for i in range(V)]
		
	for u, v in edges:
		adj[u].append(v)
		adj[v].append(u)
		
	curr = 0  # starting currend node 
	parent = -1 # current node parent
	visited = set()
		
	for node in range(V):
		if node not in visited:
			if self.detectCycle(adj, node, parent, visited):
				return True
	return False            
		            