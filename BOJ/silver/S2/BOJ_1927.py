import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 연산의 개수(N), N개의 연산에 대한 정보(x)
# 출력: 아래 출력 조건 참고

# x > 1  -> 배열에 x라는 값을 추가
# x = 0  -> 배열에서 가장 작은 값 출력 후 배열에서 제거
# 배열이 비어있는 경우 0 출력

# (풀이1) 직접 최소힙 enque, deque 구현해보기
# 최소힙 문제 -> 최소힙 enque, deque
# 최소힙 = 부모 < 자식 (부모 노드는 키 값이 가장 작음)
# enque
def enq(k):
    global last     # 마지막 정점
    last += 1       # 마지막 정점 추가
    heap[last] = k  # 마지막 정점에 k 추가

    c = last    # 부모의 키 값과 비교
    p = c // 2  # 완전이진트리에서 부모 정점

    while p and heap[p] > heap[c]:              # 부모가 있고, 부모 > 자식 이면
        heap[p], heap[c] = heap[c], heap[p]     # 교환
        c = p                                   # 현재 부모를 자식으로
        p = c//2                                # 부모의 부모로 다시 비교

# deque
def deq(k):
    global last
    temp = heap[1]          # 삭제 대상(루트=최소힙이므로 제일 작은값) 꺼내서 보관
    print(temp)             # 제일 작은 값 출력
    heap[1]= heap[last]     # 마지막 노드 값을 루트에 복사
    last -= 1               # 빈 마지막 노드 삭제
    p = 1                   # 루트에 옮긴 값을 자식과 비교
    c = p * 2               # 왼쪽 자식

    while c <= last :                               # 자식이 하나라도 있을때
        if  c+1 <= last and heap[c+1] < heap[c]:    # 오른쪽 자식이 있고 오른쪽 자식이 더 작으면
            c += 1                                  # 비교 대상을 오른쪽 자식으로 정함

        if heap[c] < heap[p]:                       # 자식이 더 작으면
            heap[c] ,heap[p] = heap[p], heap[c]     # 교환 ㄱㄱ
            p = c                                   # 자식을 새로운 부모로
            c = c*2                                 # 왼쪽 자식 번호를 계산해서 다음 비교 준비
        else:           # 부모가 더 작으면
            break       # 비교 중단

# 힙 배열 만들어놓기
n = int(input())
heap = [0] * (n+1)
last = 0

for i in range(n):
    x = int(input())
    if x > 0:
        enq(x)
    else:
        if last == 0:
            print(0)
        else:
            deq(x)

# ====================================================================================

# (풀이 2) heapq 모듈 이용
import heapq

n = int(input())
min_heap = []

for _ in range(n):
    k = int(input())
    if k == 0:
        if min_heap:
            p = heapq.heappop(min_heap)
            print(p)
        else:
            print(0)

    else:
        heapq.heappush(min_heap,k)

