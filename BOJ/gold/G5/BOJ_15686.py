import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

# 입력: 도시 크기(N), 최대 치킨 집(M)
# 출력: 치킨 거리 최솟값

# 치킨 거리 = 집가 가장 가까운 치킨집 사이의 거리
# 0 =빈칸, 1=집, 2=치킨 집

'''
치킨집들을 M개 골라서
이 치킨집 목록을 한번에 넘겨서 BFS 돌리기
1(집)을 만나면 cnt 증가시키면서 만약 이전에 구한 최솟값을 넘긴다? 그럼 더 볼 것 없이 가지치기
'''

# def f(i,s,l):
#     global min_v
#     if i == M:
#         min_v = min(min_v,bfs(p))
#         return
#
#     for j in range(s, l):
#         p[i] = c_arr[j]
#         f(i+1,j+1,l)
#
#
# def bfs(a):
#     q = deque(a)
#     visited = [[-1] * N for _ in range(N)]
#     cnt = 0
#
#     for si,sj in q:
#         visited[si][sj] = 0
#
#     while q:
#         i,j = q.popleft()
#
#         if arr[i][j] == 1:
#             cnt += visited[i][j]
#             if cnt >= min_v:
#                 return 10000000
#
#         for ci,cj in [[0,1],[1,0],[0,-1],[-1,0]]:
#             ni, nj = ci+i, cj+j
#             if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == -1:
#                 visited[ni][nj] = visited[i][j] + 1
#                 q.append([ni,nj])
#
#     return cnt
#
# N, M = map(int,input().split());
# arr = [list(map(int,input().split())) for _ in range(N)]
#
# c_arr = []
#
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 2:
#             c_arr.append((i,j))
#
# p = [0] * M
#
# min_v = 10000000
#
# f(0,0,len(c_arr))
#
# print(min_v)


"""
BFS 로 푸는 것 보다 |r1-r2| + |c1-c2|로 치킨 거리가 정의되어 있는걸 활용
-> 즉, 미리 집의 좌표를 저장해두고 선택된 치킨집들과의 거리 중 최솟값 합산
"""

# 치킨집 고르기
def f(i,s,cl):
    if i == M:
        cal_distance()
        return

    for j in range(s,cl):
        selected[i] =  j
        f(i+1,j+1,cl)

def cal_distance():
    # 각 집마다 가까운 치킨 거리 계산
    global min_v
    dist_sum = 0
    for h_dist in dists_matrix:
        temp_min = float('inf')
        for idx in selected:
            temp_min = min(temp_min,h_dist[idx])

        dist_sum += temp_min

    if dist_sum >= min_v:
        return

    min_v = min(min_v,dist_sum)

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

# 집 좌표와 치킨집 좌표 저장
h_arr = []
c_arr = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            h_arr.append([i, j])
        elif arr[i][j] == 2:
            c_arr.append([i, j])

dists_matrix = []
for hi, hj in h_arr:
    temp_dist = []
    for ci, cj in c_arr:
        temp_dist.append(abs(hi-ci) + abs(hj-cj))
    dists_matrix.append(temp_dist)

min_v = float('inf')
selected = [0] * M

f(0,0,len(c_arr))

print(min_v)