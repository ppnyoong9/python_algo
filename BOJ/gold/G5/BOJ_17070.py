import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 배열 크기(N), 배열 정보
# 출력: 파이프의 한쪽 끝을 (N,N)으로 이동시키는 방법의 수, 불가능일 시 0 출력

# 0: 빈 칸, 1: 벽
# 방향은  (0,1), (1,1), (1,0)
# 파이프는 (1, 1)와 (1, 2) 에서 시작
# 가로 (0,1),(1,1) 세로 (1,0),(1,1) 대각선 (0,1),(1,1),(1,0)
# 가로 = 0, 세로= 1, 대각선= 2 로 해서 (이전 방향, r, c) 로 저장해서 DFS?

# def dfs(sd,si,sj):
#     visited = [[False] * N for _ in range(N)]
#     stack = [(sd,si,sj)]
#     dir = [[(0,0,1),(2,1,1)],[(1,1,0),(2,1,1)],[(0,0,1),(2,1,1),(1,1,0)]]
#     cnt = 0
# 
#     while stack:
#         d,i,j = stack[-1]
#         for nd,ci,cj in dir[d]:
#             ni,nj = i+ci,j+cj
#             if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and arr[ni][nj] == 0:
#                 if ni==N-1 and nj==N-1:
#                     cnt +=1
#                     continue
# 
#                 visited[ni][nj] = True
#                 stack.append((nd,ni,nj))
#                 break
#         else:
#             stack.pop()
# 
#     return cnt
# 
# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]
# 
# print(dfs(0,0,1))


'''
미리 dir 를 놓고 하려고 했는데 이제보니 대각선일떈 3칸이 비어있어야함
if 구문으로 처리해야할 듯
그리고 가능한 경로를 다 구해야하기 때문에 visited 사용을 잘 생각해봐야..
시간 초과
'''
# def dfs(d,i,j):
#     global cnt
# 
#     # 목표 지점 도달 시
#     if i == N-1 and j == N-1:
#         cnt += 1
#         return
# 
#     # 가로로 이동 가능한 경우
#     if d == 0 or d == 2:
#         ni, nj = i, j + 1
#         if 0 <= nj < N and arr[ni][nj] == 0:
#             dfs(0,ni,nj)
#     # 세로로 이동 가능한 경우
#     if d == 1 or d == 2:
#         ni, nj = i+1, j
#         if 0<= ni < N and arr[ni][nj] == 0:
#             dfs(1, ni,nj)
# 
#     # 대각선
#     ni, nj = i+1, j+1
#     if 0<= ni < N and 0<= nj < N:
#         if arr[i][nj] == 0 and arr[ni][nj] == 0 and arr[ni][j] == 0:
#             dfs(2,ni,nj)
# 
# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]
# cnt = 0
# 
# dfs(0,0,1)
# 
# print(cnt)

'''
문제 알고리즘 분류를 보니 DP네요..
그렇다면? 해당 칸까지의 도착한 경로 수 저장
어떤 좌표 (i,j)에 도달했을 때 (가로 모양으로, 세로 모양으로, 대각선 모양으로) 도착한 경우의 수
차원 하나 늘어났다고 이렇게 헷갈리다니..
'''

N = int(input())
arr = [[0] * (N+1)] + [[0] + list(map(int,input().split())) for _ in range(N)]
dp = [[[0] * 3  for _ in range(N+1)] for _ in range(N+1)]

# 가로 방향 1, 2 에서 시작
dp[1][2][0] = 1

for i in range(1,N+1):
    for j  in range(1,N+1):
        if i==1 and j==2:
            continue

        # 현재 칸에 가로로 오는 방법
        if arr[i][j] == 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
        # 현재 칸에 세로로 오는 방법
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
        # 현재 칸에 대각선으로 오는 방법
            if arr[i-1][j] == 0 and arr[i][j-1] == 0:
                dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

print(sum(dp[N][N]))