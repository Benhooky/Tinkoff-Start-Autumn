def make_set(v, parent, bands, spirit_info):
    parent[v] = v
    bands[v] = {v}
    spirit_info[v] = (v, 1)


def find_set(v, parent):
    if v == parent[v]:
        return v
    parent[v] = find_set(parent[v], parent)
    return parent[v]


def union_sets(a, b, parent, bands, spirit_info):
    a = find_set(a, parent)
    b = find_set(b, parent)
    if a != b:
        if len(bands[a]) < len(bands[b]):
            a, b = b, a
        parent[b] = a
        bands[a].update(bands[b])
        del bands[b]
        for spirit in bands[a]:
            spirit_info[spirit] = (a, spirit_info[spirit][1] + 1)


n, m = map(int, input().split())
parent = [0] * (n + 1)
bands = {}  # Dictionary to store bands information
spirit_info = {}  # Dictionary to store spirit's information

for i in range(1, n + 1):
    make_set(i, parent, bands, spirit_info)

results = []

for _ in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, x, y = query
        union_sets(x, y, parent, bands, spirit_info)
    elif query[0] == 2:
        _, x, y = query
        results.append("YES" if find_set(x, parent) ==
                       find_set(y, parent) else "NO")
    elif query[0] == 3:
        _, x = query
        results.append(str(spirit_info[x][1]))

print('\n'.join(results))
