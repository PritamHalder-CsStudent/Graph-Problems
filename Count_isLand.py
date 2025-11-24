
# An island is either surrounded by water or the boundary of a grid 
# and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

# Examples:
# L -Land 
# w- water

# Input: grid[][] = 
#               [['L', 'L', 'W', 'W', 'W'], 
#                ['W', 'L', 'W', 'W', 'L'], 
#                ['L', 'W', 'W', 'L', 'L'], 
#                ['W', 'W', 'W', 'W', 'W'], 
#                ['L', 'W', 'L', 'L', 'W']]   

# Output: 4

class Solution:
    def countLand(self,grid,i,j,row,col):
        if i<0 or i>=row or j<0 or j>=col:
            return 
        if grid[i][j]!='L':
            return 
        
        grid[i][j]='v'  # marked as island visited 
        
        # vertically check
        self.countLand(grid,i-1,j,row,col)
        self.countLand(grid,i+1,j,row,col)
        
        #horizontally
        self.countLand(grid,i,j-1,row,col)
        self.countLand(grid,i,j+1,row,col)
        
        #diagonali check
        self.countLand(grid,i-1,j+1,row,col)
        self.countLand(grid,i+1,j-1,row,col)
        self.countLand(grid,i-1,j-1,row,col)
        self.countLand(grid,i+1,j+1,row,col)
        
        
    def numIslands(self, grid):
        row=len(grid)
        if row <=0:
            return 0
        col=len(grid[0])
        count=0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='L':
                    self.countLand(grid,i,j,row,col) # call the function 
                    count+=1
        
        return count                
       
       

 