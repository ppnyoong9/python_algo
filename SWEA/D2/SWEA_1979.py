import sys
from re import split

sys.stdin = open('input.txt', 'r')

'''
1979. 어디에 단어가 들어갈 수 있을까 
'''

# 입력: 테스트케이스(T), 배열 크기(N), 단어의 크기(K), 배열
# 출력: 단어가 들어갈 수 있는 자리의 수

# 흰색 부분(1), 검은색 부분(0)

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가로 먼저 탐색
    for i in range(N-K):
        print(arr[i])