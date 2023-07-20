
def longestCommonSubsequence(text1, text2):

        xy_grid = [[0 for y in range(len(text2) + 1)] for x in range(len(text1) + 1)]

        for x in range(len(text1) - 1, -1, -1):
            for y in range(len(text2) - 1, -1, -1):
                if text1[x] == text2[y]:
                    xy_grid[x][y] = 1 + xy_grid[x + 1][y + 1]
                else:
                    xy_grid[x][y] = max(xy_grid[x][y + 1], xy_grid[x + 1][y])

        return xy_grid[0][0]

'''

xy_grid = [[0 for y in range(len(text2) + 1)] for x in range(len(text1) + 1)]

This line initializes a 2D list called `xy_grid` with dimensions `len(text1) + 1` rows and `len(text2) + 1` columns. 
Each element is set to 0. This grid will be used to store the lengths of the longest common subsequence 
between `text1` and `text2`.

```python
for x in range(len(text1) - 1, -1, -1):
    for y in range(len(text2) - 1, -1, -1):
```
These nested loops iterate over `x` and `y` in reverse order, starting from the last indices and moving towards the first.
This backward iteration order is used to build up the `xy_grid` from the bottom-right corner to the top-left corner.

```python
    if text1[x] == text2[y]:
        xy_grid[x][y] = 1 + xy_grid[x + 1][y + 1]
```
If the characters at `text1[x]` and `text2[y]` are the same, it means they contribute to the common subsequence. 
In that case, the value at `xy_grid[x][y]` is set to 1 plus the value at the diagonally adjacent 
cell `xy_grid[x + 1][y + 1]`. This represents extending the common subsequence by including the current character.

```python
    else:
        xy_grid[x][y] = max(xy_grid[x][y + 1], xy_grid[x + 1][y])
```
If the characters are not the same, the value at `xy_grid[x][y]` is set to the maximum value between the cell on the 
right `xy_grid[x][y + 1]` and the cell below `xy_grid[x + 1][y]`. This allows the algorithm to consider the best possible 
length of the common subsequence by choosing the maximum between two options: either skipping a character in `text1` 
or skipping a character in `text2`.

```python
return xy_grid[0][0]
```
Finally, the function returns the value at the top-left corner of `xy_grid`, which represents the length of the longest 
common subsequence between `text1` and `text2`.
'''