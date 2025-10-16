import math
import sys
# sys.stdin = open('input.txt','r')

input = sys.stdin.readline

'''
17626번 Four Squares
'''

# 입력: 자연수(N)
# 출력: n을 만들 수 있는 제곱수의 합의 최소 개수


#  4개 미만이니까 4개 조합 안에 넣어봐야하나?
def f(n, k):
    print(k)
    # 1일 경우 고려
    if arr[k] == n:
        return 1

    # 2일 경우 고려
    for i in range(k,0,-1):
        for j in range(k,0,-1):
            if arr[i]+arr[j] == n:
                return 2
    
    # 3일 경우 고려
    for i in range(k,0,-1):
        for j in range(k,0,-1):
            # 초과되면 고려 x -> 가지치기 한 번
            if arr[i] + arr[j] > n:
                continue

            for p in range(k,0,-1):
                if arr[i] + arr[j] + arr[p] == n:
                    return 3

    return 4

n = int(input())

k = int(math.sqrt(n))

arr = [i**2 for i in range(k+1)]

print(f(n,k))
