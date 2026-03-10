import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline


# 입력: 자연수 A, B, C
# 출력: A**B % C
# (시간초과 유의)

'''
분할 정복
거듭 제곱을 나눠보자
일반적인 곱셈 연산 횟수 2^8 이라고 하면 7번
1. 2^1 * 2^1 = 2^2 (계산 1번)
2. 2^2 * 2^2 = 2^4 (계산 1번)
3. 2^4 * 2^4 = 2^8 (계산 1번)
-> 총 3번으로 가능
'''

def f(p):
    if p == 1:
        return A % C

    temp = f(p//2)
    result = (temp *temp) % C
    if p%2 == 1:
        result = result*A % C

    return result

A, B, C = map(int,input().split())
# print(pow(A,B,C))
print(f(B))
