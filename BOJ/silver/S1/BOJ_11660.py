import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 크기(N), 횟수(M), 표, M개의 구간((x1,y1),(x2,y2))
# 출력: 구간합

'''
직사각형으로 생각하면
si][j] = arr[i][j] + s[i][j-1] + s[i-1][j] - s[i-1][j-1] (겹치는 부분 빼기)
'''

N, M = map(int,input().split())
s = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    row_data = input().split()
    for j in range(1,N+1):
        s[i][j] = int(row_data[j-1]) + s[i][j-1] + s[i-1][j] - s[i-1][j-1]

for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    print(s[x2][y2]-s[x1-1][y2]-s[x2][y1-1]+s[x1-1][y1-1])