class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        mp = []
        for i in range(len(equations)):
            for j in range(2):
                if equations[i][j] not in mp:
                    mp.append(equations[i][j])

        n = len(mp)
        
        matrix = [[0] * len(mp) for _ in range(len(mp))]
        for i in range(len(mp)):
            for j in range(len(mp)):
                if i == j:
                    matrix[i][j] = 1.0
                else:
                    matrix[i][j] = -1.0

        for i in range(len(equations)):
            r = mp.index(equations[i][0])
            c = mp.index(equations[i][1])

            matrix[r][c] = values[i]
            matrix[c][r] = 1.0/values[i]

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] != -1.0 and matrix[k][j] != -1.0 and matrix[i][j] == -1.0:
                        matrix[i][j] = matrix[i][k] * matrix[k][j]

        res = []

        for u, v in queries:
            if u in mp and v in mp:
                r = mp.index(u)
                c = mp.index(v)
                res.append(matrix[r][c])
            else:
                res.append(-1.0)
            
        return res


