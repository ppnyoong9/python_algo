import math
import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
1929번 소수 구하기
'''

# 입력: 자연수(M), 자연수(N)
# 출력: M이상 N이하의 소수 모두 출력

m, n = map(int,input().split())

# 가운데 약수를 기준으로 대칭 형태 보이므로 제곱근까지만 확인해서 나누어 떨어지는게 있는지 확인
for i in range(m, n+1):
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            break
    else:
        if i != 1:
            print(i)