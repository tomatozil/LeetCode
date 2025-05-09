class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        # visited = [[False]*cols for _ in range(rows)]

        # def flow(y, x, ocean) -> int:
        #     if ocean == "p" and (y < 0 or x < 0):
        #         return 1
        #     if ocean == "a" and (y >= rows or x >= cols):
        #         return 1

        #     reach = 0
        #     for p1, p2 in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        #         ny, nx = y + p1, x + p2
        #         if ocean == "p" and (ny < 0 or nx < 0):
        #             reach += flow(ny, nx, ocean)
        #         elif ocean == "a" and (ny >= rows or nx >= cols):
        #             reach += flow(ny, nx, ocean)
        #         elif 0 <= ny < rows and 0 <= nx < cols and \
        #         heights[y][x] >= heights[ny][nx] and not visited[ny][nx]:
        #             visited[ny][nx] = True
        #             reach += flow(ny, nx, ocean)
        #             visited[ny][nx] = False

        #     return reach

        # ret = []
        # for i in range(rows):
        #     for j in range(cols):
        #         if flow(i, j, "p") > 0 and flow(i, j, "a") > 0:
        #             ret.append([i, j])

        # return ret
        
        visited_p = [[False]*cols for _ in range(rows)]
        visited_a = [[False]*cols for _ in range(rows)]

        def flow(y, x, visited):
            visited[y][x] = True
            for p1, p2 in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = y + p1, x + p2
                if 0 <= ny < rows and 0 <= nx < cols and \
                heights[y][x] <= heights[ny][nx] and not visited[ny][nx]:
                    flow(ny, nx, visited)

        for i in range(rows):
            flow(i, 0, visited_p)
            flow(i, cols-1, visited_a)
        
        for i in range(cols):
            flow(0, i, visited_p)
            flow(rows-1, i, visited_a)
        
        ret = []
        for i in range(rows):
            for j in range(cols):
                if visited_p[i][j] and visited_a[i][j]:
                    ret.append([i, j])

        return ret
        
        
