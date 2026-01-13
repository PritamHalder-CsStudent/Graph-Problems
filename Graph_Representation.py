
# Approach 1:

# Adjacency Matrix : A 2d array where 
# matrix[i][j] = 1  → edge from i to j
# matrix[i][j] = 0  → no edge

# Example : Graph
#   0----2
#   |
#   1 

# then, Adjacency matrix look like :
graph1 = [
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 0]
] 

# Traversal (DFS):

def dfs(graph1, curr, visited):
        visited[curr] = True
        for adj in range(len(graph1)):
            if graph1[curr][adj] == 1 and not visited[adj]:
                dfs(graph1, adj, visited)


n=len(graph1)
visited = [False] * n
for i in range(n):
    if not visited[i]:
        dfs(graph1, i, visited)


# 2. Adjacency List (Most Common):

# Each node stores a list of neighbors.

graph2 = {
    0: [1, 2],
    1: [0],
    2: [0]
}
#Or using list:
graph2 = [
    [1, 2],
    [0],
    [0]
]

# Traversal (DFS):
def dfs(graph2, curr, visited):
        visited[curr] = True
        for adj in graph2[curr] :
            if not visited[adj]:    # if visited[adj]==False then do
                dfs(graph2, adj, visited)




# Approach 2:

# We can represent Graph for best way using adjacency list 
V=4  # no of Vertices
E=4  # no of edges 
edges = [(0,1), (0,2), (1,2), (2,3)]
# Graph look like :
#       0
#      / \
#     1 _ 2
#           \
#            3

# the graph is undirected 
#using given edges we can create adjacency list
# using defaultdict there will no create any node index error, that is one  happen with me at an exam

from collections import defaultdict 
def createAdjlist(V,edges):
    graph=defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

print(createAdjlist(V,edges))    

# Adjacencylist is:[ [1, 2], [0, 2], [0, 1, 3],  [2]   ]
#                   node 0   node 1   node 3    node 4



# For directed graph 
'''
adj=[[]for i in range(V)]
for u,v in edges:
    adj[u].append(v)
     
'''


# Adjacency List for Undirected and Weighted graph: 
'''
adj = [[] for _ in range(V)]
adj[u].append((v, w))
adj[v].append((u, w))
'''

# Adjacency List for directed and Weighted graph:
'''
adj = [[] for _ in range(V)]
adj[u].append((v, w))

''' 

