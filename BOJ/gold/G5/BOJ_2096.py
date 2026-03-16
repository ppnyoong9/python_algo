import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 열 수(N), N*3의 배열 정보
# 출력: 최대 점수와 최소 점수

# dp 최대, 최소 둘 다 저장해가면 될 듯
# col = 0 이면 0,1
# col = 1 이면 셋 다 가능 0,1,2
# col = 2 이면 1,2

'''
메모리 초과
'''
# N = int(input())
#
# max_dp = [[0] * 3 for _ in range(N)]
# min_dp = [[0] * 3 for _ in range(N)]
#
# # 첫 항
# first_line = list(map(int,input().split()))
# for i in range(3):
#     max_dp[0][i] = first_line[i]
#     min_dp[0][i] = first_line[i]
#
# for j in range(1, N):
#
#     a, b, c = map(int,input().split())
#
#     max_dp[j][0] = a + max(max_dp[j-1][0],max_dp[j-1][1])
#     min_dp[j][0] = a + min(min_dp[j-1][0],min_dp[j-1][1])
#
#     max_dp[j][1] = b + max(max_dp[j-1][0],max_dp[j-1][1],max_dp[j-1][2])
#     min_dp[j][1] = b + min(min_dp[j-1][0],min_dp[j-1][1],min_dp[j-1][2])
#
#     max_dp[j][2] = c + max(max_dp[j-1][1],max_dp[j-1][2])
#     min_dp[j][2] = c + min(min_dp[j-1][1],min_dp[j-1][2])
#
# print(max(max_dp[N-1]),min(min_dp[N-1]))

'''
1차원 배열로 row 에서 max,min 찾기
'''

N = int(input())
max_dp = [0] * 3
min_dp = [0] * 3

# 첫 항
first_line = list(map(int,input().split()))
for i in range(3):
    max_dp[i] = first_line[i]
    min_dp[i] = first_line[i]

for i in range(1,N):
    a,b,c = map(int,input().split())
    temp_max = [a,b,c]
    temp_min = [a,b,c]

    temp_max[0] += max(max_dp[0],max_dp[1])
    temp_min[0] += min(min_dp[0],min_dp[1])

    temp_max[1] += max(max_dp)
    temp_min[1] += min(min_dp)

    temp_max[2] += max(max_dp[1],max_dp[2])
    temp_min[2] += min(min_dp[1],min_dp[2])

    max_dp = temp_max
    min_dp = temp_min


print(max(max_dp),min(min_dp))