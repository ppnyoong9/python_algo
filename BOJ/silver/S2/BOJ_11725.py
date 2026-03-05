import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

# 입력: 노드의 개수(N), 정점 정보
# 출력: 각 노드의 부모 노드 번호

# def bfs():
#     q = deque([1])
#     visited = [False] * (N+1)
#     visited[1] = True
# 
#     while q:
#         n = q.popleft()
# 
#         for next_n in g[n]:
#             if not visited[next_n]:
#                 visited[next_n] = True
#                 q.append(next_n)
# 
#                 # 루트 노트 1
#                 if n == 1:
#                     d[next_n] = n
#                 # 만약 next_n이 이미 부모가 있으면 next_n이 부모
#                 elif d.get(next_n):
#                     d[n] = next_n
#                 else:
#                     d[next_n] = n
# 
# N = int(input())
# 
# g = [[] for _ in range(N+1)]
# d = {}
# 
# for _ in range(N-1):
#     s, e = map(int,input().split())
#     g[s].append(e)
#     g[e].append(s)
# 
# bfs()
# 
# for i in range(2,N+1):
#     print(d[i])


"""
개선 포인트
1. visited 배열 쓸 필요 없이 부모 노드 저장할 배열을 0으로 만들어서 체크하면 된다
2. 아직 방문하지 않은 노드라면 현재 노드가 부모가 됨
"""

N = int(input())

g = [[] for _ in range(N+1)]
p = [0] * (N+1)

for _ in range(N-1):
    s, e = map(int,input().split())
    g[s].append(e)
    g[e].append(s)


q = deque([1])

while q:
    n = q.popleft()

    for next_n in g[n]:
        if p[next_n] == 0:
            p[next_n] = n
            q.append(next_n)

for i in range(2,N+1):
    print(p[i])