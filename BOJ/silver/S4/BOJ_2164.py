from collections import deque

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
2164번 카드2
'''

# 입력: 정수(N)
# 출력: 제일 마지막에 남게 되는 카드

n = int(input())
q = deque()

# 카드 배열 생성
for i in range(n):
    q.append(i+1)

# 1장일때는 무조건 1
if len(q) == 1:
    print(1)
else:
    while True:
        q.popleft()
        front = q.popleft()
        if len(q) == 0:
            print(front)
            break
        q.append(front)

