# We can represent Graph for best way using adjacency list 
V=4
E=4
edges = [[0, 1], [0, 2], [1, 2], [2, 3]] 
# the graph is undirected 
#using given edges we can create adjacency list 
def createAdjlist(V,edges):
    adj=[[] for i in range(V)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj

print(createAdjlist(V,edges))    

# Adjacencylist is:[ [1, 2], [0, 2], [0, 1, 3],  [2]   ]
#                   node 0   node 1   node 3    node 4



# For directed graph 
'''
adj=[[]for i in range(V)]
for u,v in edges:
    adj[u].append(v)
     
'''

