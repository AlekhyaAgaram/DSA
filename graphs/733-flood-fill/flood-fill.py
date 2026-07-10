class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        start_color = image[sr][sc]
        
        if start_color == color:
            return image

        q = deque()
        q.append((sr, sc))

        image[sr][sc] = color

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if row in range(m) and col in range(n) and image[row][col] == start_color:
                    image[row][col] = color  
                    q.append((row, col))     
                    
        return image