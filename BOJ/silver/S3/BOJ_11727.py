import sys
sys.stdin = open('input.txt','r')

input = sys.stdin.readline

'''
11727번 2xN 타일링 2
'''

# 입력: 자연수(N)
# 출력: (2*N 크기의 직사각형을 채우는 방법의 수) % 10007

# 오른쪽 영역에 붙일 수 있는 거 3가지
# 2*1 타일 1개 -> n-1
# 1*2 타일 2개 -> n-2
# 2*2 타일 1개 -> n-2


def f(n):
    if n == 1:
        return 1

    if n == 2:
        return 3

    d = [0] * (n+1)
    d[1] = 1
    d[2] = 3

    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-2]

    return d[n]

n =int(input())
print(f(n)%10007)