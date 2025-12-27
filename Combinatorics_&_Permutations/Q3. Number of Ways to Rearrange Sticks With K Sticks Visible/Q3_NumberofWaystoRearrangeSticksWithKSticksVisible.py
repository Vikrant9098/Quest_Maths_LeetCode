class Solution(object):
    def rearrangeSticks(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        # Mod value for the answer

        dp = [[0] * (k + 1) for _ in range(n + 1)]
        # dp[i][j] = number of ways to arrange i sticks with j visible

        dp[1][1] = 1
        # Base case: 1 stick → 1 way and it's visible

        for i in range(2, n + 1):
            # Loop through total number of sticks

            for j in range(1, k + 1):
                # Loop through number of visible sticks

                visible = dp[i - 1][j - 1]
                # Case 1: tallest stick is visible → adds 1 visible count

                hidden = dp[i - 1][j] * (i - 1)
                # Case 2: tallest stick is hidden → can be placed in (i-1) positions

                dp[i][j] = (visible + hidden) % MOD
                # Total ways = visible + hidden, take modulo

        return dp[n][k]
        # Return result for n sticks with k visible
