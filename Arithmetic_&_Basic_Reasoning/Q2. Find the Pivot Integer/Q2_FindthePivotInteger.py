class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        total = n * (n + 1) // 2          # total sum from 1 to n
        
        for x in range(1, n + 1):         # try each number from 1 to n
            left = x * (x + 1) // 2       # sum from 1 to x
            right = total - left + x      # sum from x to n
            
            if left == right:             # check if both sums equal
                return x                  # return pivot integer
        
        return -1                         # no pivot integer found
