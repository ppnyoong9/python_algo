import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline

'''
11399번 ATM
'''

# 입력: 사람 수(N), 인출하는데 걸리는 시간(Pi)
# 출력: 돈을 인출하는데 필요한 시간의 합의 최솟값

n = int(input())
arr = list(map(int,input().split()))

# 오름차순 정렬
arr.sort()

sum = 0
ans = 0

for k in arr:
    sum += k
    ans += sum

print(ans)