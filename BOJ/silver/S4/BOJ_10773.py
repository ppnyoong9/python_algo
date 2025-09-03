import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
10773번 제로
'''

# 입력: 정수(K), K개의 정수
# 출력: 수의 합

# 0 일 경우 가장 최근에 쓴 수를 지워야 한다
# 스택 이용

k = int(input())
s = [0] * k
top = -1

for i in range(k):
    n = int(input())
    # 0이면 꺼내기
    if n == 0:
        top -= 1
    # 아니면 집어넣기
    else:
        top += 1
        s[top] = n

ans = 0
for i in range(top+1):
    ans += s[i]

print(ans)