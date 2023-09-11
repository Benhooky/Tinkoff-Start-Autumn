n = int(input())
joe_sequence = list(map(int, input().split()))
winning_sequence = list(map(int, input().split()))

l, r = 0, n - 1

while l < n and joe_sequence[l] == winning_sequence[l]:
    l += 1

while r >= 0 and joe_sequence[r] == winning_sequence[r]:
    r -= 1

# Если l >= r, то последовательность Джо уже является выигрышной последовательностью
if l >= r:
    print("YES")
else:
    # Проверяем, можно ли отсортировать подпоследовательность от l до r в последовательности Джо
    if sorted(joe_sequence[l:r + 1]) == winning_sequence[l:r + 1]:
        print("YES")
    else:
        print("NO")
