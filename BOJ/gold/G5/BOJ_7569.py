import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

# 입력: 상자의 크기와 개수(M,N,H),토마토 배열 정보
# 출력: 토마토가 모두 익을 때까지 걸리는 최소 일수

# 1=익음, 0=안익음, -1=빈칸

def bfs(q):
    d = [[0,0,1],[0,1,0],[0,0,-1],[0,-1,0],[1,0,0],[-1,0,0]]
    ans = 0

    while q:
        h, i, j = q.popleft()

        for dh, di,dj in d:
            nh = h + dh
            ni = i + di
            nj = j + dj
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and arr[nh][ni][nj] == 0:
                arr[nh][ni][nj] = arr[h][i][j] + 1
                ans = max(ans,arr[nh][ni][nj] - 1)
                q.append([nh,ni,nj])

    return ans

def find_unripe():
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 0:
                    return True
    return False

M,N,H = map(int,input().split())
arr = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[-1] * M for _ in range(N)] for _ in range(H)]

q = deque()
ripe_cnt = 0

for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                q.append([h,i,j])
                ripe_cnt +=1

if ripe_cnt == N*M*H:
    print(0)

else:
    ans = (bfs(q))
    if find_unripe():
        print(-1)
    else:
        print(ans)
