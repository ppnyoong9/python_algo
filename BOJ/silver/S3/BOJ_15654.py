import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 자연수 개수(N), 뽑을 개수(M), N개의 수
# 출력: N개의 자연수 중에서 M개를 고른 수열(오름차순, 중복 x)

# 정렬을 하고 조합 뽑기
# 보니까 1,7 이랑 7,1 같이 뽑혀서 조합이 아니고 순열이라고 봐야할듯

def f(i):
    if  i == M:
        print(*p)
        return

    for j in range(N):
        if not used[j]:
            used[j] = 1
            p[i] = arr[j]
            f(i+1)
            used[j] = 0


N, M = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()

p = [0] * M
used = [0] * N

f(0)