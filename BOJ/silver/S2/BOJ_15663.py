import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 입력 배열 길이(N), 수열 길이(M), 배열
# 출력: N개의 자연수 중에서 M개를 고른 수열(중복 x, 순서 o)

'''
시간 초과
아무래도 in 연산자로 하나하나 다 보면서 슬라이싱 까지 쓰면.. 그치..
'''
# def f(i):
#     if i == M:
#         if p[:] not in ans:
#             ans.append(p[:])
#             print(* p)
#         return
#
#     for j in range(N):
#         if not used[j]:
#             used[j] = True
#             p[i] = arr[j]
#             f(i+1)
#             used[j] = False
#
# N, M = map(int,input().split())
# arr = list(map(int,input().split()))
#
# arr.sort()
#
# p = [0] * M
# used = [False] * (N+1)
#
# ans = []
#
# f(0)

'''
보니까 중복되는게 sort 하고 난 이후라 바로 이전에만 나오는데
이전것만 체크하면서 중복인지 보면 될 것 같다

'''
def f(i):
    if i == M:
        print(* p)
        return

    pre = 0

    for j in range(N):
        if not used[j] and arr[j] != pre:
            used[j] = True
            p[i] = arr[j]
            f(i+1)
            used[j] = False
            pre = arr[j]


N, M = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()

p = [0] * M
used = [False] * (N+1)

f(0)

