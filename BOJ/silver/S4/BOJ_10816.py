import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
10816번 숫자 카드 2
'''

# 입력: 숫자 카드의 개수(N), N개의 숫자카드, 비교 카드 수(M), M개의 비교 숫자카드
# 출력: 각 수가 적힌 M개의 숫자 카드를 몇 개 가지고 있는지 출력


n = int(input())
num_arr = list(map(int,input().split()))

m = int(input())
flag_arr = list(map(int,input().split()))

# dict 활용
num_dict = {}

for n in num_arr:
    if num_dict.get(n):
        num_dict[n] += 1
    else:
        num_dict[n] = 1

for n in flag_arr:
    if num_dict.get(n):
        print(num_dict.get(n),end=" ")
    else:
        print(0,end=" ")


