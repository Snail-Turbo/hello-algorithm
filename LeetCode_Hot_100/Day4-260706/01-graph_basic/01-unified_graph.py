n, m = map(int, input().split())

input_edges = [list(map(int, input().split())) for _ in range(m)]

edges = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    edges[i][i] = 1  # 将对角线元素设为1，为了：表示节点到自身的边

for u, v in input_edges:
    edges[u][v] = 1
    edges[v][u] = 1  # 如果是有向图，则不需要这行代码

for y in range(1, n+1):
    print(edges[y][1:])

"""
5 6
4 1
2 3
2 5
3 5
4 3
1 2
"""
