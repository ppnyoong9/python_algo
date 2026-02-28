import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 세로(N), 가로(M), 배열
# 출력: 테트로미노 합의 최대값

# 각 칸에서 4개의 칸 돌면서 최대인거 찾으면 되지 않을까
# 근데 그렇게 되면 불필요하게 중복되는 계산도 생각해봐야함

# *** 'ㅗ' 모양은 어떻게 해야하나..? dfs로는 한 줄기로 밖에
# 시작점 기준으로 주변 칸 3개를 고르는 방식으로?

# 그러면 둘을 따로 처리해야겠다 dfs 한번 'ㅗ' 자 한번

# def dfs(i,j,cnt,v):
#     global max_v
# 
#     if cnt == 4:
#         max_v = max(max_v,v)
#         return
# 
#     for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
#         ni,nj = i + di, j+dj
#         if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
#             visited[ni][nj] = 1
#             dfs(ni,nj,cnt+1,v + arr[ni][nj])
#             visited[ni][nj] = 0
# 
# def find_additional(i,j,v):
#     global max_v
#     for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#         ni,nj = i + di, j+dj
#         if 0 <= ni < N and 0 <= nj < M:
#             # 가로줄, 세로줄
#             if dj != 0 :
#                 c1 = ni - 1
#                 c2 = ni + 1
#                 if 0 <= c1 < N and 0 <= c2 < N:
#                     max_v = max(max_v, v+arr[ni][nj]+arr[c1][nj]+arr[c2][nj])
#             elif di != 0:
#                 c1 = nj - 1
#                 c2 = nj + 1
#                 if 0 <= c1 < M and 0 <= c2 < M:
#                     max_v = max(max_v, v+arr[ni][nj]+arr[ni][c1]+arr[ni][c2])
# 
# 
# 
# N, M = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]
# visited = [[0] * M for _ in range(N)]
# 
# max_v = 0
# 
# for i in range(N):
#     for j in range(M):
#         visited[i][j] = 1
#         dfs(i,j,1,arr[i][j])
#         find_additional(i,j,arr[i][j])
#         visited[i][j] = 0
# 
# print(max_v)

"""
좀 더 보완 할 수 있는 포인트
 1. visited 따로 만들지 않고 temp로 해당 칸의 값 백업 후 arr의 값을 0으로 처리해서 방문처리 해도 된다
 2. 'ㅗ' 모양의 블록 -> dfs 에서 돌 때 3칸까지 차면 3칸에서 탐색말고 2번째 칸에서 탐색을 함으로써 탐색해볼 수 있음 
 3. arr 배열에서 제일 최대인 값을 찾아서 가지치기에 활용 가능
"""
def dfs(i,j,cnt,v):
    global ans

    # 가지 치기
    if v + (4 - cnt) * max_v < ans:
        return
    
    # 테트로미노
    if cnt == 4:
        ans = max(ans,v)
        return

    # DFS
    for di,dj in dir:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj]:
            temp = arr[ni][nj]

            # 'ㅗ' 자 모양
            if cnt == 2:
                arr[ni][nj] = 0
                dfs(i,j,cnt+1,v + temp)
                arr[ni][nj] = temp

            arr[ni][nj] = 0
            dfs(ni,nj,cnt+1, v+temp)
            arr[ni][nj] = temp


N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
max_v = max(max(row)for row in arr)
dir = [[0,1],[1,0],[0,-1],[-1,0]]
ans = 0

for i in range(N):
    for j in range(M):
        temp = arr[i][j]
        arr[i][j] = 0
        dfs(i,j,1,temp)
        arr[i][j] = temp

print(ans)