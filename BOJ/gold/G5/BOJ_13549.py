import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

# 입력: 현재 위치(N), 타겟 위치(K)
# 출력: 타겟으로 가는 가장 빠른 시간

# 걷는다면 X-1, X+1 -> 1초
# 순간이동 2*x -> 0초
# 16 8 4 5

# 둘 드는 비용이 달라서 BFS는 안되고 그리디로 풀어야 할 듯
# 거꾸로 찾아가면 //2 유리 아니라면 -1 , +1

# def f(n, m):
#     # 타겟이 더 작을경우 다가가는 수밖에 없음, 또한 찾았을 경우 return
#     if n >= m:
#         return n-m
#     # 테스트케이스 0,1
#     if m ==1:
#         return 1
#     if m % 2 == 0:
#         return min(m-n, f(n,m//2))
#     return min(f(n,m+1), f(n,m-1)) + 1
#
#
# N, K = map(int,input().split())
# print(f(N,K))

'''
BFS 도 되네..? 비용이 달라서 안될줄 알았는데..
다만 비용이 0인 *2 가 최적의 루트이기 떄문에
무조건 *2 를 먼저 방문하도록 appendleft를 해줘야한다

*** 테스트케이스 4 6 (3 -> 6 = 1번)
최단거리를 생각해봐야함
일단 *2로 가서 방문 처리 했는데 어라라? -1로 가는게 더 빨랐을 수도 있음
따라서 visited 비용을 따져봐야함 (기록 된 비용 > 방문할 시  비용 -> 이전보다 지금 방문이 최적이면 여기로 가야함)
'''

# N,K = map(int,input().split())
#
# visited = [0] * (100001)
#
# visited[N] = 1
# q = deque([N])
#
# while q:
#     cur = q.popleft()
#
#     if cur == K:
#         print(visited[cur]-1)
#         break
#
#     next_node = cur * 2
#     if 0 <= next_node < 100001 and (not visited[next_node] or visited[next_node] > visited[cur]):
#         q.appendleft(next_node)
#         visited[next_node] = visited[cur]
#
#
#     for next_node in (cur+1, cur-1):
#         if 0 <= next_node < 100001 and (not visited[next_node] or visited[next_node] > visited[cur]+1):
#             q.append(next_node)
#             visited[next_node] = visited[cur] + 1

'''
다익스트라 -> 최단경로 로도 풀 수 있네용
가중치의 최대는 대강 100001 로 잡으면 될 듯
'''

import heapq

def dijkstra(start,end):
    pq = [(0,start)]            # (누적 가중치, 노드)
    dists =  [100001] * 100001  # 각 정점까지의 최단거리를 저장할 리스트
    dists[start] = 0            # 시작점의 가중치 0

    while pq:
        w,n = heapq.heappop(pq)

        # 이미 더 작은 가중치로 온 적 이 있다면 pass
        if dists[n] < w:
            continue

        for next_w, next_n in [[0,n*2],[1,n+1],[1,n-1]]:

            if next_n < 0  or next_n  > 100000:
                continue

            # 다음 노드로 가기 위한 누적 가중치
            new_w = w + next_w

            # 이미 같은 가중치거나, 더 작은 가중치로 온 적이 있으면 pass
            if dists[next_n] <= new_w:
                continue

            dists[next_n] = new_w
            heapq.heappush(pq,(new_w,next_n))

    return dists[end]

N,K = map(int,input().split())
print(dijkstra(N,K))
