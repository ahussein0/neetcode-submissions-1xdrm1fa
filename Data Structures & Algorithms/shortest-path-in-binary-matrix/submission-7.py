class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)

        if grid[0][0] or grid[N-1][N-1]:
            return -1

        q = deque([(0,0,1)]) # row, col, length
        visit = {(0,0)}

        directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]

        while q:
            r,c,length = q.popleft()

            if r == N-1 and c == N-1:
                return length

            for dr,dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nc < 0 or nr > N-1 or nc > N-1 or  grid[nr][nc] == 1 or (nr,nc)  in visit:
                    continue
                visit.add((nr,nc))
                q.append((nr,nc, length + 1))
        return -1




        
        