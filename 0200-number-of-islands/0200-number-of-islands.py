class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def lookup(y, x) -> None:
            for p1, p2 in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = y + p1, x + p2
                if 0 <= ny < rows and 0 <= nx < cols and \
                grid[ny][nx] == "1" and not visited[ny][nx]:
                    visited[ny][nx] = True
                    lookup(ny, nx)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    cnt += 1
                    lookup(i, j)

        return cnt       