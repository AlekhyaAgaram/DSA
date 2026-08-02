class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        adj = [[] for _ in range(n)]

        for a,b in prerequisites:
            adj[a].append(b)

        #state 0=not visited, 1=visiting, 2= visited
        state = [0]*n

        def dfs(node):
            if state[node] == 1:#cycle found
                return False
            if state[node] == 2:#state already visited
                return True

            state[node] = 1 #mark curr node being explored

            for neigh in adj[node]:
                if not dfs(neigh):#if cycle founf
                    return False
                    
            state[node] = 2 #mark curr node cycle done
            return True

        for i in range(n):
            if state[i] == 0:
                if not dfs(i):
                    return False

        return True

        