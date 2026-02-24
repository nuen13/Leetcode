"""
Docstring for leetcode.Programming 1.733
"""

##### ----- 733. FLOOD FILL ------ #####

# Given image where image[i][j] -> pixel
# given 3 int 
# sr, sc -> starting pixel 
# color -> the number that image[sr, sc] will change into 

# -> change all number that equal and adjacent to the starting number to color 

## ----- INPUT 
## image -> (grid of int)
## sr -> starting row (int)
## sc -> starting col (int)
## color -> number to change into (int)

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2


## OUTPUT --- 
## image


## PROCESS
def floodFill(image, sr, sc, color):

    

    staringPoint = image[sr][sc]
    rows = len(image)
    cols = len(image[0])
    
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != staringPoint:
            return
        
        if image[r][c] == staringPoint:
            image[r][c] = color 

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        
    dfs(sr, sc)
    print(image)

floodFill(image, sr, sc, color)
    
    
    
    
    

