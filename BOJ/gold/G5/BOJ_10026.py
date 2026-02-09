import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

# 입력: 배열크기(N), 색 배열 정보
# 출력: 적록색약 x, 적록색양 o -> 각 조건에 해당하는 구역 수

# n이 100이니까 visited 걸어놓고 다 돌아보면 되지 않을까?
# dfs, bfs 둘 다 가능할 듯

def dfs(si,sj,c):
    s = [[si,sj]]
    visited[si][sj] = True

    while s:
        i,j = s[-1]
        for di, dj in d:
            ni,nj = i+di,j+dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] == c:
                visited[ni][nj] = True
                s.append([ni,nj])
                break
        else:
            s.pop()

def bfs(si,sj,c):
    q = deque([[si,sj]])
    visited[si][sj] = True

    while q:
        i,j = q.popleft()

        for di,dj in d:
            ni,nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] == c:
                visited[ni][nj] = True
                q.append([ni,nj])

N = int(input())
arr = [list(input().strip()) for _ in range(N)]
d = [[0,1],[1,0],[0,-1],[-1,0]]

# 적록색약 x
e_cnt = 0
visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            c = arr[i][j]
            # bfs(i,j,c)
            dfs(i,j,c)
            e_cnt += 1


# 적록색약 o (R, G 치환)
rg_cnt = 0
visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            c = arr[i][j]
            # bfs(i,j,c)
            dfs(i,j,c)
            rg_cnt += 1

print(e_cnt, rg_cnt)