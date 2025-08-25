import sys

# sys.stdin = open('input.txt','r')
input = sys.stdin.readline

'''
14626번 ISBN
'''

# 입력: ISBN 13자리 숫자
# 출력: 훼손된 숫자

isbn = input().strip()
ans = 0

# 훼손된 숫자 찾기
fix_n = isbn.find('*')
last_n = isbn[-1]

# 홀수일때 가중치 3
s = 0
for i in range(12):
    # 훼손된 부분 스킴
    if i == fix_n:
        continue
    if i % 2 == 0:
        s += int(isbn[i])
    else:
        s += (int(isbn[i]) * 3)

m = 10 - int(last_n)
if m == 10:
    m = 0
for i in range(1, 11):
    temp = 0
    if fix_n % 2 == 0:
        temp = s + i
    else:
        temp = s + 3 * i
    if temp % 10 == m:
        ans = i
        break

if ans == 10:
    ans = 0

print(ans)

