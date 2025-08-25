import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
10989번 수 정렬하기 3
배열의 메모리 초과 문제
-> dictionary 자료형 이용
-> 극단적으로 5을 5만번 저장한다고하면 
배열이 차지하는 메모리 크가와 dict 형태로 저장하는 메모리 크기가 어마어마하게 차이나게 된다
'''

# 입력: 수의 개수(N), N줄의 수
# 출력: 오름차순으로 정렬한 결과

n = int(input())
num_dict = {}
for _ in range(n):
    i = int(input())
    if num_dict.get(i):
        num_dict[i] += 1
    else:
        num_dict[i] = 1

for i in range(10001):
    while num_dict.get(i):
        print(i)
        num_dict[i] -= 1


