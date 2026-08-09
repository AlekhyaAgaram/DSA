class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # 1. Build Adjacency List: src -> [(neighbor, price)]
        adj = [[] for _ in range(n)]
        for u, v, w in flights:
            adj[u].append((v, w))

        dist = [float('inf')]*n
        dist[src] = 0

        q = deque([(0,src,0)])

        while q:
            stops,node,cost = q.popleft()

            if stops > k :
                continue
            
            for neighbor, price in adj[node]:
                new_cost = cost + price

                if new_cost < dist[neighbor]:
                    dist[neighbor] = new_cost
                    q.append((stops + 1, neighbor, new_cost))

        if dist[dst] == float('inf'):
            return -1
        return dist[dst]
