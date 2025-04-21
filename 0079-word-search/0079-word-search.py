class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        n = len(word)
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def find(i, j, index) -> bool:
            if board[i][j] != word[index]:
                return False

            if index == n - 1:
                return True

            visited[i][j] = True
            for p1, p2 in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ni, nj = i + p1, j + p2
                if 0 <= ni < rows and 0 <= nj < cols and not visited[ni][nj]:
                    if find(ni, nj, index+1):
                        return True
            
            visited[i][j] = False
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if find(i, j, 0):
                        return True
        
        return False