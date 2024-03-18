from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        columns = len(heights[0])
        pcf = set()
        atl = set()

        # r = row coordinate, c = col coordinate
        def dfs(r, c, visited, prevHeight):

            # print('visited = ', type(visited))
            # print('heights = ', heights[r][c])
            # print(f'[r][c] = [{r}][{c}]')
            # print()
            if (
                    (r, c) in visited
                    or heights[r][c] < prevHeight
                    or r < 0
                    or c < 0
                    or r == rows
                    or c == columns
                    
            ): return
            # print(f"Cell: ({r}, {c}), Height: {heights[r][c]}")
            heights[r][c] #used to keep track of the value in the cell while debugging
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for cl in range(columns):
            dfs(0, cl, pcf, heights[0][cl])  # Top edge -> Pacific
            dfs(rows - 1, cl, atl, heights[rows - 1][cl])  # Bottom edge -> Atlantic

        for rw in range(rows):
            dfs(rw, 0, pcf, heights[rw][0])  # Left edge -> Pacific
            dfs(rw, columns - 1, atl, heights[rw][columns - 1])  # Right edge -> Atlantic

        res = []
        for r in range(rows):
            for c in range(columns):
                if (r, c) in pcf and (r, c) in atl:
                    res.append([r, c])
                    print(f"Cell: ({r}, {c}), Height: {heights[r][c]}")  # Print coordinates and height
        return res


heights = [
    [1, 2, 2, 3],
    [3, 2, 3, 4],
    [2, 4, 5, 3]]

sol = Solution()
sol.pacificAtlantic(heights)
print(sol)
