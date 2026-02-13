import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 범위(N), 배열 길이(M)
# 출력: 수열 (중복 허용 조합, 오름차순)

def f(i,s):
    if i == M:
        print(*comb)
        return

    for j in range(s, N):
        comb[i] = arr[j]
        f(i+1, j)

N, M = map(int,input().split())
arr = [i for i in range(1, N+1)]
comb = [0] * M

f(0,0)