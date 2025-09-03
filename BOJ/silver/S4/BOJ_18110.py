import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
18110번 solved.ac
'''

# 입력: 의견의 개수(n), 난의도 의견
# 출력: 계산한 난이도

# 문제의 난이도: 30% 절사평균

# 입력받기
n = int(input())

if n != 0:
    arr = [int(input()) for _ in range(n)]

    # 정렬
    arr.sort()

    # 절사평균이 대상이 될 의견 수
    k = int(n * 0.15 + 0.5)

    # 합 구하기
    s = 0
    if n > 2:
        for i in range(k, n - k):
            s += arr[i]
        print(int((s / (n - k * 2)+0.5)))
    else:
        for i in range(n):
            s += arr[i]
        print(int((s/n)+0.5))


else:
    print(0)
