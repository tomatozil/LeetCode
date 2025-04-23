class Solution {
public:
    vector<pair<int, int>> dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    int rows, cols;
    
    int find(vector<vector<int>>& grid, vector<vector<bool>>& visited, int y, int x) {
        if (y < 0 || y >= rows || x < 0 || x >= cols)
            return 0;
        if (grid[y][x] == 0 || visited[y][x])
            return 0;
        
        visited[y][x] = true;
        int area = 1;

        for (auto [d1, d2]: dir)
            area += find(grid, visited, y+d1, x+d2);
        
        return area;
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        rows = grid.size(), cols = grid[0].size();
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));

        int max_area = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1 && !visited[i][j])
                    max_area = max(max_area, find(grid, visited, i, j));
            }
        }

        return max_area;
    }
};