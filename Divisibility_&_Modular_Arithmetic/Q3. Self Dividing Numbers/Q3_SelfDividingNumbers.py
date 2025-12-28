class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        result = []                             # list to store all valid numbers
        
        for num in range(left, right + 1):      # check each number in the range
            temp = num                          # copy of the number to extract digits
            isValid = True                      # flag to mark if number is self-dividing
            
            while temp > 0:                     # loop through all digits
                digit = temp % 10               # get the last digit
                
                if digit == 0 or num % digit != 0:  # digit 0 or not divisible → invalid
                    isValid = False
                    break                       # stop checking further
                
                temp //= 10                     # remove the last digit
            
            if isValid:                         # if number satisfies all conditions
                result.append(num)              # add to the output list
        
        return result                           # return final list of self-dividing numbers
