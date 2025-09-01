import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

#  입력: 수식의 길이(N), 수식
#  출력: 괄호를 적젏히 추가해서 얻을 수 있는 결과의 최대값

# 괄호를 하나씩 다 넣어보는 방법이 있을듯

# 피연산자 1, 피연산자 2, 연산자
def cal(n1, n2, o):
    if o == "+":
        return n1+n2
    elif o == "-":
        return n1 - n2
    else:
        return n1 * n2

# i = 고려하는 수
# s = 이전 합
# n = 전체 길이
# e = 연산식
# def f(i,s,n,e):
#     if

n = int(input())
e = input()
