N, M = map(int, input().split())

INF = float('inf')

size = N
dist = [[INF] * size for _ in range(size)]

# from pprint import pprint
# pprint(dist)

for i in range(size):
    dist[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())

    if c < dist[a][b]:
        dist[a][b] = dist[b][a] = c

    for k in range(size):
        for i in range(size):
            if dist[i][k] == INF:
                continue
            for j in range(size):
                if dist[k][j] == INF:
                    continue

                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]





K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    if dist[a][b] == INF:
        print(0)
    else:
        print(dist[a][b])