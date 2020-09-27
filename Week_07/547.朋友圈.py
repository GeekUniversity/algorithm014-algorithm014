class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        grid = M
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        cnt = 0

        def dfs(i, j):
            grid[i][j] = 2
            for y in range(col):
                tmp_i = i
                tmp_j = y
                if grid[tmp_i][tmp_j] == 1:
                    grid[tmp_i][tmp_j] = 2
                    dfs(tmp_j, tmp_i)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    dfs(i, j)
                    cnt += 1
        return cnt
