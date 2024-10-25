# Time Complexity - O(n)
# Space Complexity - O(n)

import sys
def minStep(n,dp):
    if n == 1:
        return 0
    ans1,ans2,ans3 = sys.maxsize,sys.maxsize,sys.maxsize
    if n%3 == 0:
        if dp[n//3] == -1:
            ans1 = minStep(n//3,dp)
            dp[n//3] = ans1
        else:
            ans1 = dp[n//3]
    if n%2 == 0:
        if dp[n//2] == -1:
            ans2 = minStep(n//2,dp)
            dp[n//2] = ans2
        else:
            ans2 = dp[n//2]
    if dp[n-1] == -1:
        ans3 = minStep(n-1,dp)
        dp[n-1] = ans3
    else:
        ans3 = dp[n-1]

    ans = 1 + min(ans1,ans2,ans3)
    dp[n] = ans
    return ans
    



n = int(input())
dp =[-1 for i in range(n+1)]
print(minStep(n,dp))