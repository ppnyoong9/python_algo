import sys
# sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 정수(N)
# 출력: 팩토리얼에서 0의 개수

def f(n):
    if n == 0 :
        return 1
    if n == 1:
        return 1
    return n*f(n-1)

n = int(input())
num = str(f(n))
ans = 0

for j in range(len(num)-1,-1,-1):
    if num[j] != "0":
        break
    else:
        ans+=1

print(ans)