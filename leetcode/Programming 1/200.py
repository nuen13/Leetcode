"""
Docstring for leetcode.Programming 1.200

###### ----- 200.NUMBER OF ISLAND ------ #####

- given a 2D list m x n 
- "1" -> land 
- "0" -> water 
- count how many island 
- "1" only connected in 4 direction (up, down, left, right)

"""


## ------ INPUT 
# grid -> list of int
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","1"]
]

## ----- OUTPUT 
# numIsland -> number of island (int)
numIsland = 0 

## ------ PROCESS

def numIslands(grid):
    numIsland = 0 

    rows = len(grid)
    cols = len(grid[0])
    if not grid:
            return numIsland

    def checkSurroudningArea(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
            return 
        
        grid[r][c] = "0"
        checkSurroudningArea(r , c + 1)
        checkSurroudningArea(r, c - 1)
        checkSurroudningArea(r + 1, c)
        checkSurroudningArea(r - 1, c )
        
       
        
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                numIsland += 1 
                checkSurroudningArea(r, c)
            


    return numIsland 

## ----- OUTPUT
print(numIslands(grid))

