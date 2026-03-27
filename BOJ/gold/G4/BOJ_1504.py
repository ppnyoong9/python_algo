import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
import heapq

# 입력: 정점의 개수(N), 간선의 개수(E), 양방향 간선 정보(a,b,c) -> c는 거리, 반드시 거쳐야 하는 정점(v1,v2)
# 출력: 두 개의 정점을 지나는 최단 경로의 길이 (없을 떄 -1)

# 최단경로 다익스트라

# def dikstra(start_node,end_node):
#     pq = [(0,start_node)]
#     dists = [float('inf')] * (N+1)
#     dists[start_node] = 0
#
#     if start_node == end_node:
#         return 0
#
#     while pq:
#         d, n = heapq.heappop(pq)
#
#         if n == end_node:
#             return d
#
#         # 이전보다 더 적은 경로로 온 적이 있다면 pass
#         if dists[n] < d:
#             continue
#
#         for next_d, next_n in g[n]:
#             new_d = d + next_d
#
#             if dists[next_n] < new_d:
#                 continue
#
#             dists[next_n] = new_d
#             heapq.heappush(pq,(new_d, next_n))
#
#     return float('inf')
#
# N, E = map(int,input().split())
# g = [[] for _ in range(N+1)]
#
# for _ in range(E):
#     a,b,c = map(int,input().split())
#     g[a].append((c,b))
#     g[b].append((c,a))
#
# v1, v2 = map(int,input().split())
#
# #경로는 2가지 1 - v1 - v2 - n / 1 - v2 - v1 - n
# p1 = dikstra(1, v1) + dikstra(v1, v2) + dikstra(v2, N)
# p2 = dikstra(1, v2) + dikstra(v2, v1) + dikstra(v1, N)
#
# max_n = float('inf')
#
# if p1 == max_n and p2 == max_n:
#     print(-1)
# else:
#     print(min(p1,p2))

'''
dikstra(1) -> 1에서 v1까지, 1에서 v2까지 거리 알 수 있음
dikstra(v1) -> v1에서 v2까지, v1 에서 N까지의 거리 확보
dikstra(v2) -> v2에서 v1까지, v2 에서 N까지의 거리 확보
dists 자체를 return 받아서 인덱스로 처리하면 된다
'''

def dikstra(start_node):
    pq = [(0,start_node)]
    dists = [float('inf')] * (N+1)
    dists[start_node] = 0

    while pq:
        d, n = heapq.heappop(pq)

        # 이전보다 더 적은 경로로 온 적이 있다면 pass
        if dists[n] < d:
            continue

        for next_d, next_n in g[n]:
            new_d = d + next_d

            if dists[next_n] < new_d:
                continue

            dists[next_n] = new_d
            heapq.heappush(pq,(new_d, next_n))

    return dists

N, E = map(int,input().split())
g = [[] for _ in range(N+1)]

for _ in range(E):
    a,b,c = map(int,input().split())
    g[a].append((c,b))
    g[b].append((c,a))

v1, v2 = map(int,input().split())

d_1 =  dikstra(1)
d_v1 = dikstra(v1)
d_v2 = dikstra(v2)

p1 = d_1[v1] + d_v1[v2] + d_v2[N]
p2 = d_1[v2] + d_v2[v1] + d_v1[N]

ans = min(p1,p2)
print(ans if ans != float('inf') else -1)


