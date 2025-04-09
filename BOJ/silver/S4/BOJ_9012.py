import sys

sys.stdin = open('input.txt', 'r')

'''
9012번 괄호
'''


# 입력: 테스트케이스(T), 괄호 문자열
# 출력: 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”

# stack으로 구현해보자
# '(' 인 경우에는 stack에 push
# ')' 인 경우에는 stack에서 pop을 하여 짝을 이룰 '(' 가 있는지 확인
# ** stack에 '(' 만 들어가는 상태

# 올바른 괄호가 아닌 경우
# 1. ')' 여서 stack에서 pop을 하려는데 '(' 가 남아있지 않은 경우 (즉, stack이 빈 경우 짝이 맞지 않아 오류)
# 2. 괄호 문자열 끝까지 왔는데 stack 이 남아있는경우 ( 매칭되어야하는'(' 만 있고 더이상 ')'가 없어서 짝이 맞지 않아 오류)

''' 방법1) top 으로 stack 구현해보기'''

# def is_vaild(data):
#     # stack 생성 괄호 문자열의 길이는 2 이상 50 이하
#     top = -1
#
#     for p in data:
#         # '(' 이면 push
#         if p == '(':
#             top += 1
#         # ')'면 꺼내서 짝 이루어지는지 확인해봐야한다
#         else:
#             # stack 비어있으면 오류
#             if top == -1:
#                 return 'NO'  # 즉시 중단
#             else:
#                 # 짝 이루어지면 pop 수행
#                 top -= 1
#
#     # 다 매칭되어서(빈 stack) 올바른 괄호 문자열일 경우
#     if top == -1:
#         return 'YES'
#
#     return 'NO'
#
#
# T = int(input())
# for _ in range(T):
#     # 입력 받기
#     arr = list(input())
#     # 출력
#     print(is_vaild(arr))


'''
방법 2) list 메소드 활용하는 stack으로 접근
'''
def is_vaild(data):
    # stack 생성 괄호 문자열의 길이는 2 이상 50 이하
    stack = []

    for p in data:
        # '(' 이면 push
        if p == '(':
            stack.append('(')
        # ')'면 꺼내서 짝 이루어지는지 확인해봐야한다
        else:
            # stack 비어있으면 오류
            if not stack :
                return 'NO'  # 즉시 중단
            else:
                # 짝 이루어지면 pop 수행
                stack.pop()

    # 다 매칭되어서(빈 stack) 올바른 괄호 문자열일 경우
    if not stack:
        return 'YES'

    return 'NO'


T = int(input())
for _ in range(T):
    # 입력 받기
    arr = list(input())
    # 출력
    print(is_vaild(arr))