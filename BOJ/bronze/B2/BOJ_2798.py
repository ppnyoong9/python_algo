import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

'''
2798번 블랙잭 문제
'''

# 입력: 카드의 개수(N), 합 최대(M), 카드에 쓰여는 수 배열
# 출력: 최대(M)을 넘지 않으면서 최대한 가까운 3장의 합

def func(i,s):
    if  s > M:
        return

    if i==N and s<=M:
        return s


# 정렬을 해서 큰 수부터 보면서 쳐내면 되지 않을까?
N, M = map(int,input().split())
card_arr = list(map(int,input().split()))

card_arr.sort(reverse=True)

result = 0

p = [0] * N


