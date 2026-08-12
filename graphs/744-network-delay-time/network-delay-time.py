class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]

        for u, v, wt in times:
            adj[u].append((v, wt))

        dist = [float('inf')]*(n+1)
        dist[k] = 0

        pq = [(0,k)]

        while pq:
            d,node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for v, wt in adj[node]:
                if d + wt < dist[v]:
                    dist[v] = d + wt
                    heapq.heappush(pq, (d + wt, v))
        # If any node is unreachable
        if float('inf') in dist[1:]:
            return -1
        # Maximum shortest distance
        return max(dist[1:])
