from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            if ( r < 0 or r >= len(grid) or
                 c < 0 or c >= len(grid[0]) or 
                 grid[r][c] == '0' ):
                return
            
            # if we already visited, set it to '0' (water)
            grid[r][c] = '0'
            # dfs in four directions
            dfs(r + 1, c) # Explore down
            dfs(r - 1, c) # Explore up
            dfs(r, c + 1) # Explore right
            dfs(r, c - 1) # Explore left

        num_of_islands = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    dfs(x,y)
                    num_of_islands += 1

        return num_of_islands

'''
r < 0 and c < 0 = out of bonds
r >= len(grid) and c >= len(grid[0]) = out of bounds

'''
