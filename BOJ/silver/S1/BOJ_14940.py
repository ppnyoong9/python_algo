import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

# 입력: 지도의 크기(n,m), 배열
# 출력: 각 지점에서 목표지점까지의 거리

# 0은 갈 수 없는 땅, 1은 갈 수 있는 땅, 2는 목표지점


def find_target(n,m):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                return i, j

def bfs(target):
    si, sj = target
    q = deque([[si,sj]])
    dist[si][sj] = 0

    while q:
        i, j = q.popleft()

        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni,nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < m and dist[ni][nj] == -1:

                if arr[ni][nj] == 0:
                    continue

                q.append([ni,nj])
                dist[ni][nj] = dist[i][j] + 1


n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]


target = find_target(n,m)

dist = [[-1] * m for _ in range(n)]

bfs(target)

for i in range(n):
    for j in range(m):
        if dist[i][j] == -1:
            if arr[i][j] != 0:
                dist[i][j] = -1
            else:
                dist[i][j] = 0
        print(dist[i][j],end=' ')
    print('')