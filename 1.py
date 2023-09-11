n, s = map(int, input().split())
prices = list(map(int, input().split()))

max_price = 0
for price in prices:
    if price <= s and price > max_price:
        max_price = price

print(max_price)
