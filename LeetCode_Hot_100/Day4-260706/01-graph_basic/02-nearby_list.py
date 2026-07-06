n, m = map(int, input().split())

input_edges = [list(map(int, input().split())) for _ in range(m)]

nearby_list = [[] for _ in range(n+1)]
for u, v in input_edges:
    if v not in nearby_list[u]:
        nearby_list[u].append(v)

    if u not in nearby_list[v]:
        nearby_list[v].append(u)  # 如果是有向图，则不需要这行代码


for y in range(1, n+1):
    print(nearby_list[y])
