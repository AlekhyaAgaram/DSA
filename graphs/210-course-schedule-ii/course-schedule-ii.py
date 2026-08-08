class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses

        adj = [[] for _ in range(n)]
        inDegree = [0]*n

        for dest, src in prerequisites:
            adj[src].append(dest)
            inDegree[dest] += 1

        q = deque()
        order = [0]*n
        index = 0

        for i in range(n):
            if inDegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            order[index] = node
            index += 1
            for i in adj[node]:
                inDegree[i] -= 1
                if inDegree[i] == 0:
                    q.append(i)

        if index != n:
            return []
        return order
