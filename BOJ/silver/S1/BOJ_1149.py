import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 집의 수(N), 각 집의 칠 비용 배열(R, G, B)
# 모든 집을 칠하는 비용의 최솟값


"""
시간초과 백트래킹
"""
# 서로 인접하는 집들은 색이 같지 않아야한다
# 이전 row와 col 이 겹치지 않아야함

# 중단 조건: i == N
# 가지치기 = 이미 이전 값을 넘어버렸을때

# def f(i, v, pre):
#     global min_v
#
#     if v >= min_v:
#         return
#
#     if i == N:
#         min_v = min(min_v,v)
#         return
#
#     for j in range(3):
#         if j == pre:
#             continue
#         else:
#             f(i+1, v+arr[i][j], j)
#
# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]
#
# min_v = 1000000
#
# f(0,0,-1)
#
# print(min_v)

"""
각 칸을 돌면서 최소 비용을 저장해야하나
마지막 집에서 최소인 비용을 찾으면 될 것 같다
"""
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]

# 1번째 집 먼처 채우기
for i in range(3):
    dp[0][i] = arr[0][i]

# 각 집을 j 번쨰 색으로 칠했을떄 최소비용
for i in range(1, N):
    dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = arr[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = arr[i][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[N-1]))