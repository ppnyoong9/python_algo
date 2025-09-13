import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline


'''
11723번 집합
'''

# 입력: 연산의 수(M)
# 출력: check 연산 마다 결과 출력

def f(cal,num):
    if cal == "add":
        s.add(num)
    elif cal == "remove":
        s.discard(num)
    elif cal == "toggle":
        if num in s:
            s.discard(num)
        else:
            s.add(num)
    elif cal == "check":
        print(1 if num in s else 0)


s = set()
all_s = {i for i in range(1, 21)}

n = int(input())

for i in range(n):
    temp = list(input().split())
    if len(temp) > 1:
        f(temp[0], int(temp[1]))
    else:
        if temp[0] == "all":
            if s != all_s:
                s.clear()
                s = all_s.copy()
        elif temp[0] == "empty":
            s.clear()
