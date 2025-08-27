import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

# 입력: 회의 수(N), 각 회의의 시작시간과 끝나는 시간
# 출력: 최소 회의실 개수

n = int(input())
arr = [[0,0]] * n
for i in range(n):
    a, b = map(int,input().split())
    arr[i] = a,b

# 시작시간을 기준으로 정렬
arr.sort(key=lambda x:x[0])

ans = 1

q = deque()
q.append(arr[0])

for i in range(1, n):
    l = len(q)
    for j in range(l):
        ci, cj = q.popleft()
        ni, nj = arr[i]
        if cj <= ni:
            q.append([ni,nj])
            break
        else:
            q.append([ci,cj])
            if j == l-1:
                ans += 1
                q.append([ni,nj])

print(ans)

# 시간초과