
class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]



obj = Solution()


print("Input: 2")
print("Output:", obj.climbStairs(2))

print("Input: 3")
print("Output:", obj.climbStairs(3))

print("Input: 5")
print("Output:", obj.climbStairs(5))
