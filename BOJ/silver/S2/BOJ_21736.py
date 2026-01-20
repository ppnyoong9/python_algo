import sys
from collections import deque

sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 캠퍼스의 크기(N*M), 캠퍼스 배열
# 출력: 만날 수 있는 사람의 수

# O는 빈 공간, X는 벽, I는 도연이, P는 사람

# DFS, BFS 둘 다 이용 가능할 것 같은데
# 도연이 좌표만 구해놓고 다 탐색하면서 'P' 만나면 count 해주면 된다

# (방법 1) DFS
# 시작점 방문
# 정점에 인접한 정점를 스택에 넣고 방문
# 가다가 못가겠으면 stack에서 pop 하여 해당 정점 방문
# 종료조건: P 도착, 스택 공백 = 더이상 갈 곳이 없는 경우
def dfs(start):
    si,sj = start
    stack = [[si,sj]]
    visited[si][sj] = 1
    cnt = 0
    
    while stack:
        i,j = stack.pop()

        # 사람이면
        if arr[i][j] == 'P':
            cnt += 1

        visited[i][j] = 1

        # 우하상좌
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni = i + di
            nj = j + dj
            # 배열 범위 내에 있고, 방문하지 않았으며, 벽이 아닌 경우
            if 0 <= ni < N and  0 <= nj < M and visited[ni][nj] != 1:
                if arr[ni][nj] != 'X':
                    visited[ni][nj] = 1
                    stack.append([ni,nj])

    return cnt

# (방법 2) BFS
def bfs(start):
    si,sj = start
    q = deque([(si,sj)])
    visited[si][sj] = 1
    cnt = 0
    
    while q:
        i,j = q.popleft()

        if arr[i][j] == 'P':
            cnt +=1

        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] != 1 and arr[ni][nj] != 'X':
                visited[ni][nj] = 1
                q.append((ni,nj))
            
    return cnt

N,M = map(int,input().split())
arr = [list(input().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
start = []

# 도연이(I) 위치 찾기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I':
            start = [i,j]
            break

ans = bfs(start)
print(ans if ans > 0  else 'TT')