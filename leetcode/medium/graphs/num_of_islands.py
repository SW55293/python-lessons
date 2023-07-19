def numIslands(grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        column = len(grid[0])

        islands = 0

        

        def dfs(r, c):
            if r < 0 or r == row or c < 0 or c == column:
                return
            if grid[r][c] != '1':
                return

            grid[r][c] = '2'  # Mark '2' as visited
            # the rows only move up or down, think of each rows as 1 entity
            # the columns can only move left and right
            dfs(r + 1, c) #up
            dfs(r - 1, c) #down
            dfs(r, c + 1) #left
            dfs(r, c - 1) #right


        for x in range(row):
            for y in range(column):
                if grid[x][y] == '1':
                    dfs(x, y)
                    islands += 1

        return islands
