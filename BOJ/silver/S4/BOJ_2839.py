import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
2839번 설탕배달
'''

# 입력: 무게(N)
# 출력: 봉지의 최소 개수

# 봉지 = 3kg/5kg 2가지

n = int(input())
ans = 0

while n % 5 != 0:
    if n < 5:
        break
    n -=  3
    ans +=1

if n % 5 == 0:
    ans += n//5
    n -=(n//5)*5

if n%3 == 0:
    ans += n//3
else:
    ans = -1

print(ans)