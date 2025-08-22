import sys
# sys.stdin = open('input.txt','r')
input = sys.stdin.readline

'''
28702번 FizzBuzz
'''

# 입력: 세 개의 문자열
# 출력: 다음에 올 문자열 출력

# i가 3 o, 5 o = “FizzBuzz”를 출력
# i가 3 o, 5 x = “Fizz”를 출력
# i가 3 x, 5 o = "Buzz”를 출력
# i가 3 x, 5 x = i를 그대로 출력

s1 = input()
s2 = input()
s3 = input()

flag1 = 0
flag2 = 0

if s1.find('Fizz') != -1:
    print('Fizz')
else:
    if s2.isdecimal() :
        flag1 = int(s2)
    if s3.isdecimal():
        flag2 = int(s3)

if flag1:
    if flag2:
        print(flag2+1)
    else:
        print(flag1+1)

