from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        columns = len(heights[0])
        pcf = set()
        atl = set()
        order = []  # Add a list to track the visitation order and heights

        def dfs(r, c, visited, prevHeight, order):
            if (
                (r, c) in visited
                or r < 0
                or c < 0
                or r >= rows
                or c >= columns
                or heights[r][c] < prevHeight
            ):
                return

            visited.add((r, c))
            order.append((r, c, heights[r][c]))  # Track visitation order and height
            dfs(r + 1, c, visited, heights[r][c], order)
            dfs(r - 1, c, visited, heights[r][c], order)
            dfs(r, c + 1, visited, heights[r][c], order)
            dfs(r, c - 1, visited, heights[r][c], order)

        order_pcf = []
        order_atl = []
        for cl in range(columns):
            dfs(0, cl, pcf, heights[0][cl], order_pcf)
            dfs(rows - 1, cl, atl, heights[rows - 1][cl], order_atl)

        for rw in range(rows):
            dfs(rw, 0, pcf, heights[rw][0], order_pcf)
            dfs(rw, columns - 1, atl, heights[rw][columns - 1], order_atl)

        # Now order_pcf and order_atl contain the visitation order and heights for each ocean
        print("Pacific visitation order and heights:", order_pcf)
        print("Atlantic visitation order and heights:", order_atl)

        res = []
        for r in range(rows):
            for c in range(columns):
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