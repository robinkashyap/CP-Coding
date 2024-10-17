def minStepTo1(n):
    if n == 1:
        return 0
    ans1 = float('inf')
    if n%3==0:
        ans1 = minStepTo1(n//3)
    ans2 = float('inf')
    if n%2==0:
        ans2 = minStepTo1(n//2)
    ans3 = float('inf')
    ans3 = minStepTo1(n-1)
    ans = 1 + min(ans1, ans2, ans3)
    return ans

n=int(input())
print(minStepTo1(n))

    