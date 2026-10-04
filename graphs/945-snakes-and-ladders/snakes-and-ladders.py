class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        target = n*n

        arr = [0]
        flag = True
        for r in range(n-1,-1,-1):
            if flag:
                row_val = board[r]
            else:
                row_val = board[r][::-1]
            arr.extend(row_val)
            flag = not flag

        
        visited = {1}
        q = deque([1])
        moves = 0

        while q:
            for _ in range((len(q))):
                curr = q.popleft()
                if curr == target:
                    return moves

                for i in range(1,7):
                    nxt = curr + i
                    if nxt > target:
                        break

                    if arr[nxt] != -1:
                        dest = arr[nxt]
                    else:
                        dest = nxt
                    if dest not in visited:
                        visited.add(dest)
                        q.append(dest)
            moves += 1
        return -1
        
                
