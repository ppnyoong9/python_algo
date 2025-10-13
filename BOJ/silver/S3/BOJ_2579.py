import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
2579번 계단 오르기
'''


# 입력: 계단의 개수(n), 점수 배열(ai)
# 출력: 총 점수의 최대값

def f(n):
    if n < 3:
        s = 0
        for i in range(n):
            s += arr[i]
        return s

    if n == 3:
        return max(arr[2] + arr[1], arr[2] + arr[0])

    d[0] = arr[0]
    d[1] = d[0] + arr[1]
    d[2] = max(arr[2]+arr[0], arr[2]+arr[1])

    for i in range(3, n):
        d[i] = max((arr[i] + d[i - 2]), arr[i] + arr[i-1] + d[i - 3])
    return d[n - 1]


n = int(input())
arr = [int(input()) for i in range(n)]
d = [0] * n

print(f(n))
