import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline



'''
1935번 후위 표기식2
'''

# stack 을 이용
# 피연산자면 stack 에 집어넣기
# 연산자를 만났을 때 stack 에 있는 피연산자 2개를 꺼내서 계산한 후 stack 에 다시 집어넣기

# 일단 피연산자를 바꾸는 작업부터
# 26 크기의 리스트를 만들어서 들어오는 대응값을 저장해둔 후
# 계산 시 ord['피연산자'] - 65 해주면 될 것 같다

# 입력: 피연산자 개수(N), 후위 표기식
# 출력: 계산 결과를 소숫점 둘째 자리까지 출력


def postfix_calculate(data):
    # 피연산자를 저장할 stack
    stack = []

    for d in data:
        if d.isalpha():
            stack.append(operand[ord(d)-65])
        else:
            # 먼저 꺼내는 게 오른쪽 값
            right = stack.pop()
            left = stack.pop()
            if d == '+':
                stack.append(left + right)
            elif d == '-':
                stack.append(left-right)
            elif d == '*':
                stack.append(left*right)
            elif d == '/':
                stack.append(left/right)

    return stack[-1]

# 입력 받기
N = int(input().strip())
postfix = input().strip()

# 피연산자 대응 값을 저장할 리스트
operand = [0] * 26

# 대응하는 값 정리
for i in range(N):
    operand[i] = int(input())

ans = postfix_calculate(postfix)

print(f'{ans:.2f}')

