import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

# 입력: 상자의 크기(M,N),토마토 배열 정보
# 출력: 토마토가 모두 익을 때까지 걸리는 최소 일수

# 1=익음, 0=안익음, -1=빈칸

def bfs(q):

    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    ans = 0

    while q:
        i,j = q.popleft()

        for di, dj in d:
            ni,nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj]==0:
                arr[ni][nj] = arr[i][j] + 1
                ans = max(ans,(arr[ni][nj] -1))
                q.append([ni,nj])

    return ans

def is_unripe():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                return True

M, N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]


# 익은 토마토들 담아서 q를 넘겨주기
q = deque([])

ripe_cnt = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append([i,j])
            ripe_cnt += 1

# 모든 토마토가 익어있는 상태면 0 출력
if ripe_cnt == M*N:
    print(0)

else:
    ans = bfs(q)

    # 토마토 모두 못익으면 -1 출력
    if is_unripe():
        print(-1)
    else:
        print(ans)