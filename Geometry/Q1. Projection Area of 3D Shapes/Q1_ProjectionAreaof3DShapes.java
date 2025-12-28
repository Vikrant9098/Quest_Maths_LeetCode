class Solution {
    public int projectionArea(int[][] grid) {
        int n = grid.length;              // get the size of the grid
        
        int xy = 0;                       // area from top view
        int yz = 0;                       // area from front view
        int zx = 0;                       // area from side view
        
        for (int i = 0; i < n; i++) {     // loop each row
            int rowMax = 0;               // max value in this row (for zx)
            int colMax = 0;               // max value in this column (for yz)
            
            for (int j = 0; j < n; j++) { // loop each column
               
                if (grid[i][j] > 0)       // if cell has cube(s)
                    xy++;                 // count it for top view
                
                rowMax = Math.max(rowMax, grid[i][j]); // update row max
                
                colMax = Math.max(colMax, grid[j][i]); // update column max
            }
            
            zx += rowMax;                 // add row max to side view area
            yz += colMax;                 // add column max to front view area
        }
        
        return xy + yz + zx;              // total projection area
    }
}
