import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline

'''
11047번 동전 O
'''

# 입력: 동전 종류(N), 가치의 합(K), 동전의 가치(Ai)
# 출력: 동전 개수의 최솟값

# 큰 가치부터 채워 넣으면 될 듯 하다

n, k = map(int,input().split())

# 동전 가치 종류 배열 받기
coin_arr = [0] * n
for i in range(n):
    coin_arr[i] = int(input())

# 큰 수 부터 채워넣기
idx = n - 1
ans = 0
while k != 0:
    if k < coin_arr[idx]:
        idx -= 1
        continue
    else:
        s = k // coin_arr[idx]
        k -= s*coin_arr[idx]
        ans += s

print(ans)

