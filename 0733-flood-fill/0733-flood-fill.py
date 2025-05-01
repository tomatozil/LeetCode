class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        visited = [[0]*cols for _ in range(rows)]
        q = []
        
        image[sr][sc] = color
        q.append((sr, sc))
        visited[sr][sc] = 1
        while q:
            r, c = q[0]
            q.pop(0)

            for p1, p2 in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nr, nc = r + p1, c + p2
                if 0 <= nr < rows and 0 <= nc < cols and \
                not visited[nr][nc] and image[nr][nc] == starting:
                    image[nr][nc] = color
                    visited[nr][nc] = 1
                    q.append((nr, nc))
        
        return image