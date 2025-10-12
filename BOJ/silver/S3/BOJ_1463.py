import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
1463번 1로 만들기
'''


# 입력: 정수(N)
# 출력: 최소 연산 횟수

# 이전의 계산된 최솟값들을 이용하여 계산
# 이전 배열 값 나올때까지 -1

def f(n):

    if n == 1:
        return 0
    if n < 4:
        return 1

    d = [0] * (n + 1)

    d[1] = 0
    d[2] = 1
    d[3] = 1

    for i in range(4, n + 1):
        d[i] = d[i] = d[i - 1] + 1
        if i % 3 == 0:
            d[i] = min((d[i // 3] + 1), d[i])
        if i % 2 == 0:
            d[i] = min((d[i // 2] + 1), d[i])
    return d[n]


n = int(input())
print(f(n))
