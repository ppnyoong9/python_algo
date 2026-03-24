import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
import heapq

# 입력: 정점의 개수(V), 간선의 개수(E), 시작 정점 번호, 간선 정보(u,v,w)
# 출력: 최단 경로의 경로값

def dijkstra(start_node):
    pq = [(0,start_node)]
    dists = [3000001] * (V+1)
    dists[start_node] = 0

    while pq:
        d, n = heapq.heappop(pq)

        # 만약 이전에 더 적은 경로로 온적이 있다면 pass
        if d > dists[n]:
            continue

        for next_d, next_n in g[n]:
            new_dist = d + next_d

            # 이전에 더 적은 경로로 온 적이 있다면 pass
            if new_dist > dists[next_n]:
                continue

            dists[next_n] = new_dist
            heapq.heappush(pq,(new_dist,next_n))

    return dists

V, E = map(int,input().split())
start_node = int(input())
g = [[] for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int,input().split())
    g[u].append((w,v))


dists = dijkstra(start_node)

for i in range(1, V+1):
    print('INF' if dists[i] == 3000001 else dists[i])