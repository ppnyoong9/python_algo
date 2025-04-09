import sys

sys.stdin = open('input.txt', 'r')

'''
10828번 스택
'''


def is_valid(t):
    if t == -1:
        return False

    return True


# 입력: 명령 수(N), 수행할 명령
# 출력: 출력해야할 명령이 주어질 때마다 출력

# push: 스택에 데이터 넣기
# pop: 스택에서 데이터를 빼기
# size: 스택에 들어있는 정수의 개수 출력
# empty: 스택이 비어있으면 1, 아니면 0을 출력
# top: 스택의 가장 위에 있는 정수 (없을 시 -1 출력)

# top을 이용해서 구현해보자

N = int(input())
stack = [0] * (N+1)
top = -1

for _ in range(N):
    # 명령어 받기
    command_str = list(input().split())
    c = command_str[0]
    # 뒤에 값이 있는 경우는 push 하나
    if c == 'push':
        top += 1
        stack[top] = command_str[1]
    elif c == 'pop':
        if is_valid(top):
            print(stack[top])
            top -= 1
        else:
            print('-1')
    elif c == 'size':
        print(top + 1 if is_valid(top) else '0')
    elif c == 'empty':
        print('0' if is_valid(top) else '1')
    else:
        print(stack[top] if is_valid(top) else '-1')


'''
방법 2 ) stack 리스트로 구현 및 리스트 메서드 이용
'''
# N = int(input())
# stack=[]
# for _ in range(N):
# 
#     # 명령어 받기
#     command_str = list(input().split())
# 
#     # 명령어
#     command = command_str[0]
# 
#     # 뒤에 값이 있는 경우는 push 하나
#     if len(command_str) > 1:
#         v = command_str[1]
#         if command == 'push':
#             stack.append(v)
#     else:
#         if command == 'pop':
#             if len(stack):
#                 print(stack.pop())
#             else:
#                 print(-1)
#         elif command == 'size':
#             print(len(stack))
#         elif command == 'empty':
#             if stack:
#                 print(0)
#             else:
#                 print(1)
#         elif command == 'top':
#             if stack:
#                 print(stack[-1])
#             else:
#                 print(-1)
