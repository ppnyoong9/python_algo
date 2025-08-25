import sys
# sys.stdin = open('input.txt','r')
input = sys.stdin.readline

'''
1259번 팰린드롬수
'''

# 입력: 정수 ,0(엔드포인트)
# 출력: 팰린드롬수면 'yes', 아니면 'no'

while True:
    a = input()
    if a.strip() == '0':
        break
    else:
        print('yes') if a.strip()==a[::-1].strip() else print('no')