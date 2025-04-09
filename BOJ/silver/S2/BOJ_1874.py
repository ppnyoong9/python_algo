import sys

sys.stdin = open('input.txt', 'r')

'''
1874번 스택 수열
'''

# 입력: 스택 범위(N), n개의 줄에 걸친 정수
# 출력: 스택에서 push, pop을 하면서 오류없이 꺼낼 수 있으면 push 연산은 '+', pop 연산은 '-' 출력
# 불가능한 경우 NO 출력

# 입력 받은 수 > stack[top] : push 연산
# 입력 받은 수 < stack[top] : pop 연산
# stack에서 pop을 하려고 하는데 더 작은 숫자가 나오면 불가능

'''
stack top으로 구현
'''
N = int(input())

# 스택 생성
stack = [0] * (N+1)
top = 0
# 1부터 N까지 stack에서 pop한 이력이 있는지 여부를 체크할 리스트
used = [0] * (N+1)

ans = ''

for _ in range(N):
    num = int(input())

    if ans == 'NO':
        break

    # 입력 받은 수 > stack[top] : push 연산
    while num > stack[top]:
        top += 1
        stack[top] = top
        ans += '+'

    # 입력 받은 수 < stack[top] : pop 연산
    while num < stack[top]:
        if used[top] == 1:
            ans = 'NO'
            break
        used[top] = 1
        top -= 1
        ans += '-'

    if num==stack[top]:
        used[top] = 1
        top -= 1
        ans += '-'

print(ans)
