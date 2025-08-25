import sys
sys.stdin = open('input.txt','r')

'''
2231번 분해합
'''

# 분해합= N과 N의 각 자리수의 합 (245일때 256(245+2+4+5))
# 생성자 = 어떤 자연수 M의 분해합이 N인 경우 M을 N의 생성자라고 함 (245가 256의 생성자)

# 입력: 자연수(N)
# 출력: N의 가장 작은 생성자

N = int(input())

result = N

for i in range(N-1,0,-1):
    temp = i
    str_i = str(i)
    for l in range(len(str_i)):
        temp += int(str_i[l])
    if N == temp:
        result = min(result,i)

if result == N:
    result = 0

print(result)