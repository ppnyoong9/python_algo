import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 연산의 개수(N), 자연수 배열
# 출력: 배열에서 가장 큰 값, 없으면 0


# (풀이1) 직접 heap 구현
def enque(n):
    '''
    들어갈 자리(마지막 정점) 만들어주고 -> 값 삽입 -> 부모 설정 -> 부모가 있고, 만약 부모가 더 작으면 자리 교환
    중단 시점: 부모가 없거나 부모가 더 클 때 (최대힙)
    '''
    global last
    last += 1
    heap[last] = n
    c = last
    p = last // 2
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

def deque():
    '''
    일단 최대값이였던 루트 print -> 마지막 정점에 있던 친구 백업해놓고 루트에 집어넣기 마지막 루트는 -1
    -> 자식이 있다 - yes -> 오른쪽 자식이 있고 오른쪽 자식이 더 크면 오른쪽 자식과 자리 바꾸기
    ->  왼쪽 자식이 더 크면 왼쪽 자식과 자리 바꾸기
    '''
    global last
    if last == 0:
        print(0)
        return

    print(heap[1])

    heap[1] = heap[last]
    last -= 1

    p = 1
    c = p*2

    while c <= last:
        if c+1 <= last and heap[c] < heap[c+1]:
            c += 1
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p*2
        else:
            break

N = int(input())

heap = [0] * (N+1)  # 힙 배열
last = 0            # 마지막 정점

for _ in range(N):
    n = int(input())
    if n > 0:
        enque(n)
    else:
        deque()

#  ==============================================================
# (풀이2) heapq 모듈 이용
import heapq
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())

max_heap = []

for _ in range(N):
    n = int(input())
    if n > 0:
        heapq.heappush(max_heap,(-n))
    elif max_heap:
        x = heapq.heappop(max_heap)
        print(-x)
    else:
        print(0)
