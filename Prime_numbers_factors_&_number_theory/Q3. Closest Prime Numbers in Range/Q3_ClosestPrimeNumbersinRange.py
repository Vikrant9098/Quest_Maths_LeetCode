class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        limit = right
        # We need primes only up to 'right'

        isPrime = [True] * (limit + 1)
        # Create an array marking all numbers as prime initially

        if limit >= 0:
            isPrime[0] = False
        # 0 is not a prime

        if limit >= 1:
            isPrime[1] = False
        # 1 is not a prime

        p = 2
        # Start checking primes from 2

        while p * p <= limit:
            # Loop until square root of limit

            if isPrime[p]:
                # If number is prime

                for multiple in range(p * p, limit + 1, p):
                    # Mark all multiples of p as not prime

                    isPrime[multiple] = False

            p += 1
            # Move to next number

        primes = []
        # List to store primes in the given range

        for i in range(left, right + 1):
            # Check numbers from left to right

            if isPrime[i]:
                primes.append(i)
                # Add prime number to list

        if len(primes) < 2:
            # If less than two primes, no pair exists

            return [-1, -1]

        minDiff = float("inf")
        # Store smallest difference found so far

        ans = [-1, -1]
        # Store final answer pair

        for i in range(len(primes) - 1):
            # Loop through consecutive primes

            diff = primes[i + 1] - primes[i]
            # Find difference between pair

            if diff < minDiff:
                # Found a smaller difference

                minDiff = diff
                ans = [primes[i], primes[i + 1]]
                # Update answer pair

        return ans
        # Return closest prime pair
