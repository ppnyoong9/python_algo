import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
1003번 피보나치 함수
'''


# 입력: 테스트 케이스(T), 자연수 또는 0(N)
# 출력: 0이 출력되는 횟수, 1이 출력되는 횟수

def fibo(n):
    for i in range(2, n + 1):
        cnt_arr[i][0] = cnt_arr[i - 1][0] + cnt_arr[i - 2][0]
        cnt_arr[i][1] = cnt_arr[i - 1][1] + cnt_arr[i - 2][1]
    return cnt_arr[n][0], cnt_arr[n][1]


cnt_arr = [[0] * 2 for _ in range(41)]
cnt_arr[0] = [1, 0]
cnt_arr[1] = [0, 1]

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    print(*fibo(n))

