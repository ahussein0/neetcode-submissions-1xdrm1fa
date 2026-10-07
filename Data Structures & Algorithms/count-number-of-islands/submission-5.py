class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        visited = set()
        directions = [(-1,0), (1,0), (0,-1), (0, 1)]

        def dfs(r,c):
            # check if its in visited
            if (r,c) in visited:
                return
            
            # check if r and c are not out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            # check if its an island
            if grid[r][c] != "1":
                return

            visited.add((r,c))

            
            for dr, dc in directions:
                dfs(r + dr, c + dc)



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    count += 1
        return count

        