import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] closestPrimes(int left, int right) {

        int limit = Math.max(right, 1000000);
        // Take max range so sieve can cover at least 'right'

        boolean[] isPrime = new boolean[limit + 1];
        // Boolean array to mark prime numbers

        Arrays.fill(isPrime, true);
        // Initially assume all numbers are prime

        isPrime[0] = false;
        isPrime[1] = false;
        // 0 and 1 are not primes

        for (int num = 2; num * num <= limit; num++) {
            // Loop through numbers up to sqrt(limit)

            if (isPrime[num]) {
                // If number is still marked prime

                for (int multiple = num * num; multiple <= limit; multiple += num) {
                    // Mark all multiples as not prime

                    isPrime[multiple] = false;
                }
            }
        }

        List<Integer> primes = new ArrayList<>();
        // List to store primes in the range

        for (int i = left; i <= right; i++) {
            // Loop through the range [left, right]

            if (isPrime[i]) {
                primes.add(i);
                // Add prime to list
            }
        }

        if (primes.size() < 2) {
            // If less than two primes exist, no pair possible

            return new int[]{-1, -1};
        }

        int minDiff = Integer.MAX_VALUE;
        // Track smallest difference between primes

        int[] result = new int[2];
        // Store closest prime pair

        for (int i = 0; i < primes.size() - 1; i++) {
            // Check each consecutive pair

            int diff = primes.get(i + 1) - primes.get(i);
            // Difference between pair

            if (diff < minDiff) {
                // If we found a smaller difference

                minDiff = diff;
                result[0] = primes.get(i);
                result[1] = primes.get(i + 1);
                // Update closest pair
            }
        }

        return result;
        // Return final closest pair
    }
}
