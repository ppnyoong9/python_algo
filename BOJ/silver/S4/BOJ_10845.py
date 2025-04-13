import sys

sys.stdin = open('input.txt', 'r')

# input = sys.stdin.readline

'''
10845번 큐
'''


# 입력: 명령의 수(N), N개의 명령어
# 출력: 출력해야하는 명령이 주어질 때마다 출력

N = int(input())

# 큐 생성
q = [0] * (N + 1)
front = rear = -1

for _ in range(N):
    cmd = input().split()
    c = cmd[0]

    if c == 'push':
        # enque
        rear +=1
        q[rear] = cmd[1]
    elif c=='pop':
        if front == rear:
            print(-1)
        else:
            front +=1
            print(q[front])
    elif c=='size':
        print(rear - front)
    elif c=='empty':
        print(1 if rear==front else 0)
    elif c=='front':
        print(-1 if front == rear else q[front+1])
    elif c=='back':
        print(-1 if front==rear else q[rear])
