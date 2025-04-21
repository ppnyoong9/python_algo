import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline



'''
17299번 오등큰수
'''

# for문 한 번만 허용
# F(Ai) 등장 횟수 고려해서 등장 횟수가 더 커야함
# F(Ai) 를 따로 저장해놓으면 되지 않을까나

# 입력: 수열 A의 크기, 수열
# 출력: 오등 큰수 출력

N = int(input())
arr = list(map(int,input()))

F = [0] * N
ans = [-1] * N
stack = []

for i in range(N):
    pass
