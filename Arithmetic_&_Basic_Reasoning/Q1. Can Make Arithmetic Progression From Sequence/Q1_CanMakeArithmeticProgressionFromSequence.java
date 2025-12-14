class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        // Step 1: Sort the array
        java.util.Arrays.sort(arr);

        // Step 2: Find the common difference
        int diff = arr[1] - arr[0];

        // Step 3: Check if all consecutive differences are same
        for (int i = 2; i < arr.length; i++) {
            if (arr[i] - arr[i - 1] != diff) {
                return false;   // not an arithmetic progression
            }
        }

        return true; // valid arithmetic progression
    }
}
