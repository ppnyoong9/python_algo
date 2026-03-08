import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 배열 원소 개수(N), 수열 길이(M), 배열
# 출력: N개의 자연수 중 M개를 고른 수열 (중복 x, 오름차순)

def f(i,s):
    if i == M:
        print(*c)
        return

    pre = 0

    for j in range(s, N):
        if arr[j] != pre:
            c[i] = arr[j]
            pre = arr[j]
            f(i+1,j)

N, M = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()

c = [0] * M

f(0,0)