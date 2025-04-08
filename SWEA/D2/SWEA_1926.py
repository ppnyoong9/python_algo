import sys

sys.stdin = open('input.txt', 'r')

'''
1926. 간단한 369게임
'''


def change(num):
    cnt = 0
    cnt += num.count('3')
    cnt += num.count('6')
    cnt += num.count('9')

    if cnt:
       return '-' * cnt

    return num


# 입력: 정수(N)
# 출력: 3, 6, 9 게임 규칙에 맞게 출력


N = int(input())

for i in range(1, N + 1):
    print(change(str(i)),end=' ')
