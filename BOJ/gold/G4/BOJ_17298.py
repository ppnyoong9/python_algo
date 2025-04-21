import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
17298. 오큰수
'''

# Ai의 오른쪽에 있으면서 Ai보다 큰 수 중 가장 왼쪽에 있는 수
# 1,000,000 -> 10^6 으로
# 1초(대략 10^8) 이내에 풀어야
# 반복문 1개까지만 safe
# 따라서 일단 stack 을 -1로 생성해놓고, 각 수를 돌면서 이전 요소보다 더 크다고 판단되는 경우 자신이 오큰수라고 주장해야함(?)

# stack 연산 -> 삽입, 삭제 O(1)

# 입력: 수열 A의 크기, 수열 A의 원소
# 출력: 오큰수 출력

N = int(input())
arr = list(map(int, input().split()))

# 오큰수 저장 (처음에는 오큰수가 없는 -1 로 초기값 설정)
ans = [-1] * N
# 오큰수가 아닌 수의 인덱스 저장
stack = []

for i in range(N):
    while stack and arr[stack[-1]] < arr[i]:
        idx = stack.pop()
        ans[idx] = arr[i]
    stack.append(i)

print(*ans)