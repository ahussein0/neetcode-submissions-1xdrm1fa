class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        visited = set()
        directions = [(-1,0) , (1,0), (0,1), (0, -1)]


        def dfs(r,c):
            if (r,c) in visited:
                return 0
            
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            
            if grid[r][c] != 1:
                return 0 

            visited.add((r,c))
            area = 1

            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area
            


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = dfs(r,c)
                    res = max(res,area)
        return res
        