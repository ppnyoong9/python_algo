import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 테스트케이스(T), 문자열의 길이(L)
# 출력: 길이가 L인 괄호 문자열의 개수를 1000000007로 나눈 나머지

t = int(input())
for tc in range(t):
    l = input()
    ans= 0

    #

    # 출력
    print(ans % 1000000007)

