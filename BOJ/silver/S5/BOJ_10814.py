import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
10814번 나이순 정렬
'''

# 입력: 회원의 수(N), 각 회원의 나이와 이름
# 출력: 회원은 나이순, 가입 순으로 출력

n = int(input())
arr = []

# 나이, 이름 받기
for i in range(n):
    age, name = input().split()
    arr.append([int(age), name])

# 나이 기준 정렬
arr.sort(key=lambda x: x[0])

# 출력
for i in range(n):
    print(f"{arr[i][0]} {arr[i][1]}")
