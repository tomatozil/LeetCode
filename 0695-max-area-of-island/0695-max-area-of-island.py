class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        
        def find(y, x):
            if not (0 <= y < rows and 0 <= x < cols):
                return 0
            if grid[y][x] != 1 or visited[y][x]:
                return 0
            visited[y][x] = True
            area = 1

            for p1, p2 in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                area += find(y + p1, x + p2)

            return area

        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_area = max(max_area, find(i, j))

        return max_area