import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

'''
11050번 이항계수
'''


# 입력: 자연수 N, 정수 K
# 출력: 이항계수

n, k = map(int,input().split())

a= 1
b= 1
ans = 1

for i in range(k):
    a *= (n-i)
    b *= (k-i)

print(a//b)