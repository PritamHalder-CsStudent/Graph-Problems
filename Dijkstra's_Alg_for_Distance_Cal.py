# Dijksta work on weighted undirected graph to find best route from src to destination 
#if dist[u]+w < dist[v]:
#    dist[v]=dist[u]+w

# Input: V = 3, edges[][] = [[0, 1, 1], [1, 2, 3], [0, 2, 6]], src = 2
# Output: [4, 3, 0]
# Explanation:
# For 2 to 0 minimum distance will be 4. By following path 2 -> 1 -> 0
#  2 to 1 minimum distance will be 3. By following path 2 -> 1
# For 2 to 2 minimum distance will be 0. By following path 2 -> 2




import sys
import heapq
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # converting edges into adjacency list
        adj=[[] for i in range(V)]
       
        for u,v,w in edges:
           adj[u].append((v,w))
           adj[v].append((u,w))
        
        # intialize the priority queue and distance list
        # Min-heap (priority queue) storing pairs of (distance, node)
        pq=[]
        dist=[sys.maxsize]*V
        
        dist[src]=0
        heapq.heappush(pq,(0,src))  # heapq is Python’s built-in priority queue (min-heap).storing pairs of (distance, node)
        
        while pq:
            # peak 
            d, u=heapq.heappop(pq)
            # If this distance not the latest shortest one, skip it
            if d > dist[u]:
                continue
             # Explore all neighbors of the current vertex
            for v,w in adj[u]:
                
                if dist[u]+w < dist[v]:
                    dist[v]=dist[u]+w
                    heapq.heappush(pq,(dist[v],v))
        
        return dist            
                    

'''
if d > dist[u]:
    continue
    
🧠 What does this mean?
When we pop a node from the priority queue (pq), sometimes the popped distance is not the latest shortest distance for that node.

Why?
Because multiple entries for the same node might be inserted into the heap before the shortest path is finally found.

Example scenario:

Heap Content (distance, node)
(5, 2) ← pushed earlier but not optimal
(3, 2) ← newer, better distance

Heap pop order:

First pop: (3,2) → correct shortest distance → update neighbors

Later pop: (5,2) → outdated entry ❌

Now, if we don’t skip outdated entries → we do extra work and possibly break the logic.

So this condition is like a filter 🚫:

"Ignore this record if a better path was already found."

'''               
           
        