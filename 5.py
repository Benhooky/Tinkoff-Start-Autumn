def find_parent(parent, v):
    if parent[v] == v:
        return v
    parent[v] = find_parent(parent, parent[v])
    return parent[v]


def union_sets(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        parent[b] = a


def count_states(n, roads, X):
    parent = [i for i in range(n)]
    states = n

    for u, v, w in roads:
        if w >= X:
            if find_parent(parent, u) != find_parent(parent, v):
                union_sets(parent, u, v)
                states -= 1

    return states


n, m = map(int, input().split())
roads = []

for _ in range(m):
    u, v, w = map(int, input().split())
    roads.append((u - 1, v - 1, w))

roads.sort(key=lambda x: x[2])  # Сортируем дороги по длине

left, right = 0, roads[-1][2] + 1  # Начальный диапазон для бинарного поиска

states_at_begin = count_states(n, roads, left)

while right - left > 1:
    mid = (left + right) // 2
    if count_states(n, roads, mid) == states_at_begin:
        left = mid
    else:
        right = mid

print(left-1)
