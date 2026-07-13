class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "-"

        def dfs(r,c,prev,new):
            if r < 0 or r >= m or c < 0 or c >= n:
                return

            if board[r][c] != prev:
                return

            board[r][c] = new

            dfs(r+1,c,prev,new)
            dfs(r-1,c,prev,new)
            dfs(r,c+1,prev,new)
            dfs(r,c-1,prev,new)

        for i in range(m):
            if board[i][0] == '-':
                dfs(i,0,"-","O")
            if board[i][n-1] == "-":
                dfs(i,n-1,"-","O")


        for j in range(n):
            if board[0][j] == '-':
                dfs(0,j,"-","O")
            if board[m-1][j] == "-":
                dfs(m-1,j,"-","O")

         # Replace remaining '-' with 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == '-':
                    board[i][j] = 'X'

        
            