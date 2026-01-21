import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

# 입력: 미로 크기(N*M), 미로 정보 
# 출력: 지나야 하는 최소 칸 수

# BFS
def bfs(si,sj,ei,ej):
    dist = [[0] * M for _ in range(N)]
    q = deque([(si,sj)])
    dist[si][sj] = 1

    while q:
        i,j = q.popleft()
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and dist[ni][nj] == 0:
                dist[ni][nj] = dist[i][j] + 1
                if ni == ei and nj == ej:
                    return dist[ni][nj]
                q.append([ni,nj])


N, M = map(int,input().split())
arr = [list(map(int,input().strip())) for _ in range(N)]

print(bfs(0,0,N-1,M-1))