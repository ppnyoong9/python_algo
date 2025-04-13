from collections import deque

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


'''
10866번 덱
'''

# 입력: 명령어 수(N), N개의 명령
# 출력: 출력해야하는 명령마다 출력


N = int(input())
q = deque()


for _ in range(N):
    cmd = input().split()
    c = cmd[0]

    if c == 'push_front':
        q.appendleft(cmd[1])
    elif c == 'push_back':
        q.append(cmd[1])
    elif c == 'pop_front':
        print(q.popleft() if q else -1)
    elif c == 'pop_back':
        print(q.pop() if q else -1)
    elif c == 'size':
        print(len(q))
    elif c == 'empty':
        print(0 if q else 1)
    elif c == 'front':
        print(q[0] if q else -1)
    elif c == 'back':
        print(q[-1] if q else -1)
