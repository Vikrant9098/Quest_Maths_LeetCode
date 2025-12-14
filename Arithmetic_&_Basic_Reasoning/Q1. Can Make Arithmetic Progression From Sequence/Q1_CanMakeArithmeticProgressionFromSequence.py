class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        arr.sort()                     # sort the array to check differences in order
        
        diff = arr[1] - arr[0]         # find the common difference from first two elements
        
        for i in range(2, len(arr)):   # loop through the rest of the elements
            if arr[i] - arr[i - 1] != diff:   # if any difference does not match
                return False           # then it's not an arithmetic progression
        
        return True                    # all differences matched, so return true
