import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
import heapq

# 입력: 도시의 개수(N), 버스의 개수(M), 버스 정보(출발지 - 도착지 - 비용), 출발점과 도착점
# 출력: 출발지에서 도착지로 가는데 드는 최소 비용

# 다익스트라, 한 정점에서 다른 정점까지의 최단 거리
# 시작 정점에서 거리가 최소(누적거리)인 정점을 선택해 나가면서 최단 경로 구하기

# dist의 최대값은 100000*100000 으로 맞추자

def dijkstra(start_node,end_node):
    pq = [(0,start_node)]       # (누적거리, 노드 번호)
    dists = [100000**2] * (N+1) # 각 정점까지의 최단 거리를 저장
    dists[start_node] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        # 목적지에 도달했다면 즉시 반환
        if node == end_node:
            return dists[end_node]

        # 이전에 더 적은 비용으로 온 전적이 있다면 pass
        if dists[node] < dist:
            continue

        for next_dist, next_node in g[node]:
            new_dist = dist + next_dist

            # 이미 같은 비용이거나, 더 적은 비용으로 온 적이 있다면 pas
            if dists[next_node] <= new_dist:
                continue

            dists[next_node] = new_dist
            heapq.heappush(pq,(new_dist,next_node))

    return dists[end_node]

N = int(input())
M = int(input())

g = [[] for _ in range(N+1)]

for _ in range(M):
    # 출발, 도착, 가중치
    s,e,w = map(int,input().split())
    g[s].append((w,e))

start, end = map(int,input().split())

print(dijkstra(start,end))