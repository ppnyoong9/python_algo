import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
1260번 DFS와 BFS
'''


# 입력: 정점의 개수(N), 간선의 개수(M), 탐색을 시작할 정점의 번호(V)
# 출력: DFS를 수행한 결과, BFS를 수행한 결과

# V부터 방문된 점을 순서대로 출력
# 방문할 수 있는 점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문

# DFS: 깊이 우선 탐색 -> 갈 수 있는 곳까지 가보는 탐색, stack 으로 구현
# BSF: 넓이 우선 탐색 -> 정점에서 인근한 정점들부터 탐색, queue 로 구현

# 인접리스트로 간선 정보를 받아보자

# def dfs(start):
#     result = []  # start: 출발지점, n: 마지막정점
#     visisted = [0] * (N + 1)  # 방문 표시
#
#     stack = [start]  # 시작정점 넣어놓고 시작
#
#     while stack:
#
#         n = stack.pop()  # stack에서 꺼내기
#
#         # 이미 방문한 정점이면 뒷걸음치기 (더이상 진행 x)
#         if visisted[n] == 1:
#             continue
#
#         visisted[n] = 1  # 방문표시
#
#         result.append(n)
#
#
#         # 인접 행렬 돌면서 확인
#         for w in reversed(adj_list[n]):
#             if visisted[w] == 0:  # 아지막 방문 안한 정점이면
#                 stack.append(w)  # stack에 추가
#
#
#     return result


def dfs(node):
    visited[node] = 1
    result.append(node)

    for n in adj_list[node]:
        if not visited[n]:
            dfs(n)


def bfs(start):
    result = []
    visited = [0] * (N + 1)
    # 시작점 넣어주기
    q = [start]
    visited[start] = 1

    while q:

        n = q.pop(0)
        result.append(n)

        # 인접한 정점 다 넣어주기
        for w in adj_list[n]:
            # 이미 방문한 정점이면 넣지 말아야한다!
            if visited[w]:
                continue
            # 아직 방문 안했으면 방문표시 하고 q에 넣기
            visited[w] = 1
            q.append(w)

    return result


# 정점의 개수(N), 간선의 개수(M), 탐색을 시작할 정점의 번호(V)
N, M, V = map(int, input().split())

# 인접 간선 정보 리스트
adj_list = [[] for _ in range(N + 1)]

# 간선 정보 받기 (양방향)
for _ in range(M):
    s, e = map(int, input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)

# 정점 낮은 곳 부터 가야하므로 정렬 고
for i in range(1, N + 1):
    adj_list[i].sort()

# dfs 재귀를 위한 방문배열
visited = [0] * (N+1)
result = []
dfs(V)
print(*result)
print(*bfs(V))
