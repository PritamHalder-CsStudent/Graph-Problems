# Infosys Interview 

# Find the number of path from root to end which sum of all path node is divisible by K . 
# In this given problems Edges , K and value of nodes given using an array name Values . 
# The Edges also contain (0,0) edges which have to ignored ...

# Example test case:
'''
Edges  = [(1,2), (1,3), (2,4), (2,5), (0,0)]
Values = [1, 4, 6, 7, 3]
K = 2
'''

from collections import defaultdict


def dfs(graph,curr,parent,node_valueMap,curr_sum,k):
    curr_sum=(curr_sum + node_valueMap[curr])%k
    count=0
    is_leaf=True
    for neighbor in graph[curr]:
        if neighbor!=parent:
            is_leaf=False
            count+=dfs(graph,neighbor,curr,node_valueMap,curr_sum,k)
            
    if is_leaf and curr_sum==0:
        return 1
    
    return count




def count_paths_divisible_by_k(edges, values, k):
    graph = defaultdict(list) # using this inbuild method index error will not occure 
    for u,v in edges:
        if u==0 and v==0:
            continue
        graph[u].append(v)
        graph[v].append(u)
    
    node_valueMap={}
    for i in range(1,len(values)+1):
        node_valueMap[i]=values[i-1]
    
        
    curr=1
    parent=-1
    curr_sum=0
    
    return dfs(graph,curr,parent,node_valueMap,curr_sum,k)



Edges  = [(1,2), (1,3), (2,4), (2,5), (0,0)]
Values = [1, 4, 6, 7, 3]
K = 2 

ans=count_paths_divisible_by_k(Edges, Values, K)
print("num of path is:",ans)


'''
when i declear graph as graph=[[] for i in edges] this will show error(Index error) at line grap[v].appen(u)
edges is a list of tuples
len(edges) = number of edges (here ≈ 5)
But node numbers are 1, 2, 3, 4, 5

but graph only has indices 0..4

** Correct Way: Size graph by NUMBER OF NODES

You must size graph based on the maximum node number, not number of edges.

    max_node = 0
    for u, v in edges:
        max_node = max(max_node, u, v)

    # Create graph
    graph = [[] for _ in range(max_node + 1)]
    
 
if i want to store this path using a list then how to do 

def dfs(graph, node, parent, nodeValue, curr_sum, k, path, all_paths):
    curr_sum += nodeValue[node]
    path.append(node)

    is_leaf = True
    count = 0

    for nei in graph[node]:
        if nei != parent:
            is_leaf = False
            count += dfs(graph, nei, node, nodeValue, curr_sum, k, path, all_paths)

    if is_leaf:
        if curr_sum % k == 0:
            all_paths.append(path[:])   # store COPY
            return 1

    path.pop()   # backtrack
    return count   


def count_paths_divisible_by_k(edges, values, k):
    graph = defaultdict(list) # using this inbuild method index error will not occure 
    for u,v in edges:
        if u==0 and v==0:
            continue
        graph[u].append(v)
        graph[v].append(u)
    
    node_valueMap={}
    for i in range(1,len(values)+1):
        node_valueMap[i]=values[i-1]
    
        
    curr=1
    parent=-1
    curr_sum=0
    all_paths = []
    path = []

    ans = dfs(graph, 1, -1,node_valueMap, 0, k, path, all_paths)

    return ans, all_paths
    
    
    
    
*** if i use visited array then 
def dfs(node, curr_sum):
    visited[node] = True
    curr_sum += nodeValue[node]

    for nei in graph[node]:
        if not visited[nei]:
            dfs(nei, curr_sum)

    visited[node] = False   # backtrack
    







'''        
