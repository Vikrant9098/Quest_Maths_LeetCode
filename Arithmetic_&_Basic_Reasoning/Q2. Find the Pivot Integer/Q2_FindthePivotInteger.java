class Solution {
    public int pivotInteger(int n) {
        
        int total = n * (n + 1) / 2;    // total sum from 1 to n using formula
        
        for (int x = 1; x <= n; x++) {  // try each number from 1 to n
            int left = x * (x + 1) / 2; // sum from 1 to x
            int right = total - left + x; // sum from x to n (right side sum)
            
            if (left == right) {        // check if both sums are equal
                return x;               // x is the pivot integer
            }
        }
        
        return -1;                      // no pivot integer found
    }
}
