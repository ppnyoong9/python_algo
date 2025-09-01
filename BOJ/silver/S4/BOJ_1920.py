import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
1920번 수 찾기
'''

# 입력: 자연수(N), 기준이 되는 N개의 정수, 자연수(M), 찾을 대상인 M개의 정수
# 출력: 존재하면 1, 존재하지 않으면 0

n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))

num_dict = {}

for i in range(n):
    num_dict[arr1[i]] = 1

for i in range(m):
    if num_dict.get(arr2[i]):
        print(1)
    else:
        print(0)
        

