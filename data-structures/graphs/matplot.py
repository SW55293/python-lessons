from typing import List
import matplotlib.pyplot as plt
import numpy as np

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        self.pcf = set()
        self.atl = set()

        def dfs(r, c, visited, prevHeight):
            if ((r, c) in visited or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevHeight):
                return

            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, self.pcf, heights[0][c])
            dfs(rows - 1, c, self.atl, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, self.pcf, heights[r][0])
            dfs(r, cols - 1, self.atl, heights[r][cols - 1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in self.pcf and (r, c) in self.atl:
                    res.append([r, c])
        return res

heights = [
    [1,2,2,3],
    [3,2,3,4],
    [2,4,5,3]
]

sol = Solution()
result = sol.pacificAtlantic(heights)

# Create a color map
# cmap = plt.cm.get_cmap('terrain')  # Or choose a different colormap
cmap = plt.cm.colormaps['terrain']
# Mark cells based on reachability
grid = np.zeros((len(heights), len(heights[0])))
for r, c in sol.pcf:
    grid[r, c] = 1
for r, c in sol.atl:
    grid[r, c] = 2
for r, c in sol.pcf & sol.atl:
    grid[r, c] = 3

# Plot the grid
plt.imshow(grid, cmap=cmap, interpolation='nearest')
plt.colorbar(label='Ocean Reachability')
plt.title('Pacific-Atlantic Water Flow')
plt.show()

print(result)
