import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
7068번 덩치
'''

# 입력: 전체 사람의 수 (N), 각 사람의 몸무게와 키 (x, y)
# 출력: 덩치 등수

n = int(input())
w_arr = [0] * n
h_arr = [0] * n
rank = [1] * n

for i in range(n):
    w_arr[i], h_arr[i] = map(int,input().split())

for i in range(n):
    for j in range(n):
        if i==j: continue
        if w_arr[j] < w_arr[i] and h_arr[j] < h_arr[i]:
            rank[j] += 1


print(*rank)

