'''
1978번 소수 찾기
'''
import math

# 입력: 수의 개수(N), N개의 수
# 출력: 소수의 개수 출력

N = int(input())
arr = list(map(int,input().split()))

result = 0

for n in arr:

    if n==1: continue

    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            break
    else:
        result += 1

print(result)
