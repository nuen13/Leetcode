"""
Docstring for leetcode.Programming 1.695

##### ------ 695.MAX AREA OF ISLAND------ ######

Given 2D Array `grid` 
- "1" island
- "0" water
RETURN the highest area of isnad
- search all island 
- print the blob with most "1"

"""


## ----- INPUT 
# grid (m x n) -> the map (list of int)
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# output = 6 

## ----- OUTPUT
# maxArea -> (int)




## ----- PROCESS
def maxAreaOfIsland(grid):

    rows = len(grid)
    cols = len(grid[0])

    maxArea = 0 

    if not grid:
        return maxArea
    
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:

            return 0 
        
        grid[r][c] = 0 
        curArea = 1 + dfs(r + 1, c) +dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
    
        return curArea
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
            
                curArea = dfs(r, c,)
                maxArea = max(maxArea, curArea)
        

    return maxArea

## ----- RETURN 
# print(maxAreaOfIsland(grid))
print(maxAreaOfIsland(grid))

    

    





