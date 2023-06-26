def pacificAtlantic(self, heights):
    # Get the number of rows and columns in the matrix
    rows = len(heights)
    cols = len(heights[0])

    # Create sets to store cells reachable from the Pacific and Atlantic oceans
    pacific = set()
    atlantic = set()

    def dfs(r, c, visited, prev_height):
        # Helper function for depth-first search (DFS)
        # r, c: current row and column
        # visited: set to keep track of visited cells
        # prev_height: height of the previous cell in the DFS path
        
        # Check if the cell is already visited or out of bounds or has a height lower than the previous cell
        if ((r, c) in visited or
            r not in range(rows) or
            c not in range(cols) or
            heights[r][c] < prev_height):
            return

        # Mark the cell as visited
        visited.add((r,c))
        
        # Recursively call DFS on the adjacent cells in all four directions
        dfs(r + 1, c, visited, heights[r][c])
        dfs(r - 1, c, visited, heights[r][c])
        dfs(r, c + 1, visited, heights[r][c])
        dfs(r, c - 1, visited, heights[r][c])

    # Traverse the cells in the first and last rows, and call DFS from each cell
    for c in range(cols):
        dfs(0, c, pacific, heights[0][c])  # Call DFS from the cells in the first row
        dfs(rows - 1, c, atlantic, heights[rows-1][c])  # Call DFS from the cells in the last row

    # Traverse the cells in the first and last columns, and call DFS from each cell
    for r in range(rows):
        dfs(r, 0, pacific, heights[r][0])  # Call DFS from the cells in the first column
        dfs(r, cols-1, atlantic, heights[r][cols-1])  # Call DFS from the cells in the last column

    # Return the intersection of cells reachable from both oceans
    return pacific & atlantic
