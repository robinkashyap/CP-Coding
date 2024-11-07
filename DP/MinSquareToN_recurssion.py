import sys

def minNoOfSquare(n):
    if n == 0:
        return 0
    ans = sys.maxsize
    i = 1
    while(i*i<=n):
        cur_ans = 1 + minNoOfSquare(n-i*i)
        ans = min(cur_ans,ans)
        i += 1
    return ans

print(minNoOfSquare(7))