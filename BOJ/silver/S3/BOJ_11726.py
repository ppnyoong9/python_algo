import sys
sys.stdin = open('input.txt','r')

input = sys.stdin.readline

'''
11726번 2xN 타일링
'''

# 입력: 자연수(N)
# 출력: (2*N 크기의 직사각형을 채우는 방법의 수) % 10007

# dp 문제
# 세로가 2로 고정되어 있음을 유의
# 블럭 마지막에 붙일수 있는 경우 2가지
# 2*1 한 블럭을 붙이던지 -> n-1 에 붙이기
# 1*2 블럭 2개를 상하로 붙여서 붙이던지 -> n-2에 붙이기

# 따라서 점화식은 d[n] = d[n-1] + d[n-2]

def f(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    d = [0] * (n+1)
    d[1] = 1
    d[2] = 2

    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]

    return d[n]

n =int(input())
print(f(n)%10007)