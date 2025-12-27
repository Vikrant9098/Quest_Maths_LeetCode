class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        
        if k % 2 == 0 or k % 5 == 0:    # if k is even or divisible by 5, no such number exists
            return -1
        
        rem = 0                         # remainder when building the number digit by digit
        length = 0                      # length of the repunit number
        
        while True:                     # keep building until we find a divisible number
            rem = (rem * 10 + 1) % k    # add a '1' digit and take mod k
            length += 1                 # increase length
            
            if rem == 0:                # if remainder becomes 0, divisible by k
                return length           # return the length (answer)
