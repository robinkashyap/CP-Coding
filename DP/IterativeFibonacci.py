def fib(n):
    dp = [0 for i in range(n+1)]
    dp[1] = 1
    i = 2
    while(i<=n):
        dp[i] = dp[i-1] + dp[i-2]
        i += 1
    return dp[n]

n = int(input())
print(fib(n))
