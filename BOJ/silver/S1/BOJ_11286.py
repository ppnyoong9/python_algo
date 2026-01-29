import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
import heapq

# 입력: 연산의 개수(N), N개의 연산에 대한 정보(x)
# 출력: 아래 출력 조건 참고

# x != 0  -> 배열에 x라는 값을 추가
# x = 0  -> 배열에서 절대값이 가장 작은 값 출력 후 배열에서 제거
# 배열이 비어있는 경우 0 출력

N = int(input())
min_q = []

for _ in range(N):
    n = int(input())
    if n:
        heapq.heappush(min_q,[abs(n),n])
    else:
        if min_q:
            a, b = heapq.heappop(min_q)
            print(b)
        else:
            print(0)

