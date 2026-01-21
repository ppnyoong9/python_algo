import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

# 입력: 지도의 크기(N), 배열 정보
# 출력: 총 단지수, 각 단지 집 수 (오름차순)
# 집 O = 1, 집 X = 1

# DFS
def dfs(si, sj):
    stack = [[si,sj]]
    arr[si][sj] = 0
    cnt = 1

    while stack:
        i, j = stack[-1]

        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 0:
                stack.append([ni,nj])
                arr[ni][nj] = 0
                cnt += 1
                break

        # 갈 곳이 없는 좌표인 곳인 경우만 stack에서 제거
        else:
            stack.pop()
    return cnt

# BFS
def bfs(si,sj):
    q = deque([[si,sj]])
    arr[si][sj] = 0
    cnt = 1

    while q:
        i, j = q.popleft()
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni,nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 0:
                q.append([ni,nj])
                cnt += 1
                arr[ni][nj] = 0

    return cnt



N = int(input())
arr = [list(map(int,input().strip())) for _ in range(N)]
h_arr = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            continue
        cnt = bfs(i,j)
        h_arr.append(cnt)

print(len(h_arr))
h_arr.sort()
for cnt in h_arr:
    print(cnt)