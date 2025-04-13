# import sys
#
# sys.stdin = open('input.txt', 'r')

'''
1406 에디터
'''

# 입력: 초기 문자열, 입력할 명령어의 개수(M), 명령어
# 출력: 모든 명령어를 수행하고 난 후 입력되어 있는 문자열 출력

# stack 문제 같아보인다!

# L : 커서 왼쪽으로 한 칸 옮김
# D: 커서 오른쪽으로 한 칸 옮김
# B: 커서 왼쪽에 있는 문자 삭제
# P 문자 : 커서 왼쪽에 문자 추가


'''
시간초과
'''
# in_str = input()
# M = int(input())

# stack에 기존 문자열 넣어주고 길이 구해놓기
# stack = [*in_str]
# N = len(in_str)
# cursor = N - 1
#
# for _ in range(M):
#     temp = input().split()
#     l = len(temp)
#     c = temp[0]
#
#     if c == 'L':
#         # 커서가 맨 문장의 맨 앞이면 무시
#         if cursor > -1:
#             cursor -= 1
#     elif c == 'D':
#         # 커서가 stack 범위 벗어나지 않게
#         if cursor < N:
#             cursor += 1
#     elif c == 'B':
#         # 커서가 맨 문장의 맨 앞이면 무시
#         if cursor > -1:
#             stack.pop(cursor)
#             cursor -= 1
#     else:
#         # 문자를 왼쪽 위치에 삽입
#         cursor += 1
#         stack.insert(cursor,temp[1])
#
#
# print(''.join(stack))

'''
커서는 그대로 둔 채 커서 기준 좌측, 우측 리스트에 문자를 입력하는 방식
'''

from collections import deque

in_str = input()
M = int(input())

left = deque(in_str)
right = deque()

for _ in range(M):
    temp = input().split()
    c = temp[0]

    if c == 'L' and left:
        right.appendleft(left.pop())
    elif c == 'D' and right:
        left.append(right.popleft())
    elif c == 'B' and left:
        left.pop()
    elif c == "P":
        # 문자를 왼쪽 위치에 삽입
        left.append(temp[1])

print(''.join(left + right))
