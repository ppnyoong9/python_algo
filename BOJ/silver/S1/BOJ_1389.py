import sys
sys.stdin = open('../S2/input.txt', 'r')
input = sys.stdin.readline
from collections import deque

# 입력: 유저의 수(N), 친구 관계의 수(M), 친구 관계
# 출력:케빈 베이컨의 수가 가장 작은 사람

def bfs(start):
    dist = [-1] * (N + 1)
    q = deque([start])
    dist[start] = 0

    while q:
        n = q.popleft()

        for next_node in graph[n]:
            if dist[next_node] == -1:
                dist[next_node] = dist[n] + 1
                q.append(next_node)

    return sum(d for d in dist if d > 0)

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]


for _ in range(M):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)


min_v = 10000
ans = 0
for i in range(1, N+1):
    v = bfs(i)
    if v < min_v:
        min_v = v
        ans = i

print(ans)
