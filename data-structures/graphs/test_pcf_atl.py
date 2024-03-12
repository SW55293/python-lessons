from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pcf = set()
        atl = set()

        # r = row coordinate, c = col coordinate
        def dfs(r, c, visited, prevHeight):
            if (
                (r, c) in visited
                or r < 0
                or c < 0
                or r == rows
                or c == cols
                or heights[r][c] < prevHeight
            ): return

            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        
        for c in range(cols):
            dfs(0, c, pcf, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        
        for r in range(rows):
            dfs(r, 0, pcf, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pcf and (r, c) in atl:
                    res.append([r, c])
        return res
    

heights = [
    [1,2,2,3],
    [3,2,3,4],
    [2,4,5,3]]

sol = Solution()
sol.pacificAtlantic(heights)
print(sol)


# r + 1 = going to the right
# r - 1 = going to the left
# c + 1 = going up
# c - 1 = going down