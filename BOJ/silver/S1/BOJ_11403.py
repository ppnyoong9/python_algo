import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

# 입력: 정점의 개수(N), 인접 행렬
# 출력: 방향 그래프 -> 갈 수 있으면 1, 갈 수 없으면 0

# DFS
def dfs(start):
    visited = [0] * N

    s = [start]

    while s:
        now = s[-1]
        for j in range(N):
            if adj_matrix[now][j] and not visited[j]:
                # ans[j] = 1
                visited[j] = 1
                s.append(j)
                break
        else:
            s.pop()

    return visited

# BFS
def bfs(s):
    visited = [0] * N
    ans = [0] * N
    q = deque([s])

    while q:
        now = q.popleft()

        for j in range(N):
            if adj_matrix[now][j]:

                if visited[j]:
                    continue

                q.append(j)
                visited[j] = 1
                ans[j] = 1

    return ans


N = int(input())
adj_matrix = [list(map(int,input().split())) for _ in range(N)]

# for i in range(N):
#     print(*bfs(i))

for i in range(N):
    print(*dfs(i))