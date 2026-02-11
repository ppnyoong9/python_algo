import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
import heapq

# 입력: 테스트 데이터(T), 연산의 개수(k), 연산 정보
# 출력: Q 최댓값, 최솟값

# I = 삽입
# D 1 = 최대값 삭제
# D -1 = 최솟값 삭제

T = int(input())

for tc in range(T):
    k = int(input())

    min_h = []
    max_h = []

    is_remove = [True] * k

    for i in range(k):
        e, n = input().split()
        n = int(n)

        if e == 'I':
            heapq.heappush(min_h,(n, i))
            heapq.heappush(max_h,(-n, i))
            is_remove[i] = False

        # 최댓값 삭제
        elif  n == 1:

            # 현재 최대/최소 힙이 나뉘어져 있으므로 동기화를 위해 제거된 것들 상대에서도 제거
            while max_h and is_remove[max_h[0][1]]:
                heapq.heappop(max_h)

            if max_h:
                is_remove[max_h[0][1]] = True
                heapq.heappop(max_h)

        # 최솟값 삭제
        else:
            while min_h and is_remove[min_h[0][1]]:
                heapq.heappop(min_h)

            if min_h:
                is_remove[min_h[0][1]] = True
                heapq.heappop(min_h)


    while max_h and is_remove[max_h[0][1]]:
        heapq.heappop(max_h)

    while min_h and is_remove[min_h[0][1]]:
        heapq.heappop(min_h)

    if not max_h:
        print('EMPTY')
    else:
        print(-max_h[0][0], min_h[0][0])
