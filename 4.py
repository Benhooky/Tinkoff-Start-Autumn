n, m = map(int, input().split())
denominations = list(map(int, input().split()))

dp = [float('inf')] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for denom in denominations:
        if i >= denom and dp[i - denom] + 1 < dp[i]:
            dp[i] = dp[i - denom] + 1

if dp[n] == float('inf'):
    print(-1)
else:
    result = []
    while n > 0:
        for denom in denominations:
            if n >= denom and dp[n - denom] + 1 == dp[n]:
                result.append(denom)
                n -= denom
                break
    print(len(result))
    print(*result)
