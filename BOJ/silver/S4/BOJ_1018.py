import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
1018번 체스판 다시 칠하기
'''

# 입력: 넓이(M*N), 체스판 정보
# 출력: 다시 칠해야하는 정사각형의 최소 개수

# 세로줄 * 가로줄
m, n=  map(int,input().split())
arr =  [input().strip() for _ in range(m)]

# 8*8 이니까 이 체스판이 되는 최소 횟수를 찾아야함
# 시직은 B일수도 있고, W일수도 있음
# BWBWBWBW 또는 WBWBWBWB
ans  = 64

def cal_cost(si,sj,c):
    global ans
    min_cost_a = 0
    min_cost_b = 0

    color_arr = ['BWBWBWBW','WBWBWBWB']
    
    # 시작점을 기준으로 뒤집을 때
    for i in range(8):
        c += 1
        c = c % 2
        for j in range(8):
            if color_arr[c][j] != arr[si+i][sj+j]:
                min_cost_a += 1
            if min_cost_a > ans:
                break

    ans = min(ans, min_cost_a)
    
    # 시작점 부터 뒤집을 때
    c -= 1
    for i in range(8):
        c += 1
        c = c % 2
        for j in range(8):
            if color_arr[c][j] != arr[si+i][sj+j]:
                min_cost_b += 1
            if min_cost_b > ans:
                break

    ans = min(ans,min_cost_b)

# 시작점
for i in range(m-7):
    for j in range(n-7):
        if arr[i][j] == 'B':
            cal_cost(i,j,1)
        elif arr[i][j] == "W":
            cal_cost(i,j,0)

print(ans)