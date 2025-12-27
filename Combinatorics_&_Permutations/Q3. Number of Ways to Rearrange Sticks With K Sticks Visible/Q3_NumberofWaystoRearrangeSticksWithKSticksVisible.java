class Solution {
    static final int MOD = 1_000_000_007;
    // Modulo value for the answer

    public int rearrangeSticks(int n, int k) {
        long[][] dp = new long[n + 1][k + 1];
        // dp[i][j] = number of ways to arrange i sticks with j visible sticks

        dp[1][1] = 1; // base case: only one stick and it's visible

        for (int i = 2; i <= n; i++) {
            // Loop for total sticks from 2 to n

            for (int j = 1; j <= k; j++) {
                // Loop for number of visible sticks

                long visible = dp[i - 1][j - 1];
                // Case 1: tallest stick is visible → increases visible count by 1

                long hidden = (dp[i - 1][j] * (i - 1)) % MOD;
                // Case 2: tallest stick is hidden → can be placed in (i-1) places

                dp[i][j] = (visible + hidden) % MOD;
                // Total ways = visible case + hidden case
            }
        }

        return (int) dp[n][k];
        // Return the final answer for n sticks and k visible sticks
    }
}
