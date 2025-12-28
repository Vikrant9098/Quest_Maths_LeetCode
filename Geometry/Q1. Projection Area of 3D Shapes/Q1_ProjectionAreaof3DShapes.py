class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        n = len(grid)                      # size of grid
        
        xy = 0                              # top view area
        yz = 0                              # front view area
        zx = 0                              # side view area
        
        for i in range(n):                 # loop each row
            row_max = 0                    # max in this row (for side view)
            col_max = 0                    # max in this column (for front view)
            
            for j in range(n):             # loop each column
                if grid[i][j] > 0:         # if cell has cube(s)
                    xy += 1                # count for top view
                
                row_max = max(row_max, grid[i][j])   # update row max
                col_max = max(col_max, grid[j][i])   # update column max
            
            zx += row_max                  # add row max to side view
            yz += col_max                  # add column max to front view
        
        return xy + yz + zx                # return total area
