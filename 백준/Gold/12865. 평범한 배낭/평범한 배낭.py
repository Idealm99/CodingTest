
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(k+1)]

for item in items:
    w, v = item
    for W in reversed(range(1, k+1)): # 중복 방지
        if w <= W:
            dp[W] = max(dp[W], dp[W-w] + v)
            
print(dp[k])