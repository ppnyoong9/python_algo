import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 정점의 개수(N), 간선 개수(M), 간선의 양 끝점(u,v)
# 출력: 연결 요소의 개수

# 그래프, (양방향) 무향 그래프
# visited 배열을 만들어서 모든 정점을 방문
# 모든 정점 방문할때까지 방문(노선 하나당 +1)

# 1. [] 인접 배열 리스트 생성 및 그래프 정보 저장
# 2. 모든 정점이 visited 될 때까지 그래프 탐색

# # (방법 1) DFS
# def dfs(n):
#     for next_node in graph[n]:
#         if visited[next_node]:
#             continue
#
#         visited[next_node] = 1
#         dfs(next_node)
#
# # (방법 2) BFS
# def bfs(n):
#     q = [n]
#
#     while q:
#         now = q.pop(0)
#
#         for next_node in graph[now]:
#             if visited[next_node]:
#                 continue
#
#             visited[next_node] = 1
#             q.append(next_node)
#
# N, M = map(int,input().split())
# graph = [[] for _ in range(N+1)]
# visited = [0] * (N+1)
# ans = 0
#
# for _ in range(M):
#     u, v = map(int,input().split())
#     graph[u].append(v)
#     graph[v].append(u)
#
# for i in range(1,N+1):
#     if visited[i] != 1:
#         visited[i] = 1
#         ans += 1
#         bfs(i)
#
# print(ans)


# (방법 3) 유니온 파인드
# make-set: 모든 정점이 자기 자신을 부모로 가지도록 설정
# union: 간선이 주어질 때마다 연결 관계에 있는 것들을 대표자로 하여금 집합으로 묶기
# 모든 간선을 처리한 후 부모가 자기 자신이 정점만 세면 된다

# 각 정점의 부모(대표자)를 자신으로 초기화
def make_set(n):
    parents = [i for i in range(n+1)]
    return parents

# 대표자 탐색
def find_set(x):
    while parents[x] != x:
        parents[x] = parents[parents[x]] # 경로 압축
        x = parents[x]
    return x

# 대표자 집합으로 묶기
def union(x,y):
    # x, y 의 대표자를 검색
    rx = find_set(x)
    ry = find_set(y)

    # 둘 부모가 다르면
    if rx != ry:
        parents[ry] = rx


N, M = map(int,input().split())
visited = [0] * (N+1)
ans = 0

parents = make_set(N)

for _ in range(M):
    u, v = map(int,input().split())
    union(u,v)

for i in range(1, N+1):
    if parents[i] == i:
        ans += 1

print(ans)