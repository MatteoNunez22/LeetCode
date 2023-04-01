class Solution {
    public int islandPerimeter(int[][] grid) {
        int perimeter = 0;
        int rows = grid.length;
        int cols = grid[0].length;
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1) {
                    int count = 4;
                    if (i+1 < rows && grid[i+1][j] == 1) count -= 2;
                    if (j+1 < cols &&  grid[i][j+1] == 1) count -= 2;
                    perimeter += count;
                }
            }
        }
        
        return perimeter;
    }
}