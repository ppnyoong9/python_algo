import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
'''
2609번 최대공약수와 최소공배수
'''

# 입력: 자연수 2개
# 출력: 최대 공약수와 최소 공배수

a,b = map(int,input().split())
x= 0
y= 0
gcd = 1
lcm = 1

if(a>b):
    x=a
    y=b
else:
    x=b
    y=a

while y!=0:
    x=x%y
    x,y = y,x

gcd = x

lcm = a*b // gcd

print(gcd)
print(lcm)