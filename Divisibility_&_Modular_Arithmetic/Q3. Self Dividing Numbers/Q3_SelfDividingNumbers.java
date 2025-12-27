class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        
        List<Integer> result = new ArrayList<>();   // list to store all valid numbers
        
        for (int num = left; num <= right; num++) { // check every number in the range
            int temp = num;                         // copy of the number to extract digits
            boolean isValid = true;                 // flag to check if number is self-dividing
            
            while (temp > 0) {                      // iterate through all digits
                int digit = temp % 10;              // get last digit
                
                if (digit == 0 || num % digit != 0) { // digit 0 or not divisible → invalid
                    isValid = false;
                    break;                          // no need to check further
                }
                
                temp /= 10;                         // remove the last digit
            }
            
            if (isValid) {                          // if number passed all checks
                result.add(num);                    // add to the answer list
            }
        }
        
        return result;                               // return all self-dividing numbers
    }
}
