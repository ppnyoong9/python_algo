import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

# 입력: 노드의 개수(N), 간선 정보(부모, 자식, 가중치)
# 출력: 트리의 지름 (가장 긴 경로)

# 1에서 가장 멀리 있는 노드를 찾기
# 가장 멀리 떨어진 노드를 시작점으로 다시 멀리있는 노드 찾기

'''
dfs 
'''
def dfs(start_node):
    s = [[start_node,0]]
    visited = [False] * (N+1)
    visited[start_node] = True
    end_node = 0
    end_weight = 0

    while s:
        now_n, now_w = s[-1]
        for next_n, next_w in g[now_n]:
            if not visited[next_n]:
                visited[next_n] = True
                s.append((next_n, next_w + now_w))
                break
        else:
            s.pop()
            if now_w > end_weight:
                end_node = now_n
                end_weight = now_w

    return end_node, end_weight

def bfs(start_node):
    q = deque([start_node])
    dist = [-1] * (N+1)
    dist[start_node] = 0

    max_d = 0
    max_n = start_node

    while q:
        now_n = q.popleft()
        for next_n, next_w in g[now_n]:
            if dist[next_n] == -1:
                dist[next_n] = dist[now_n] + next_w
                q.append(next_n)

                if dist[next_n] > max_d:
                    max_d = dist[next_n]
                    max_n = next_n

    return max_n, max_d


N = int(input())
g = [[] for _ in range(N+1)]

for _ in range(N-1):
    s, e, w = map(int,input().split())
    g[s].append((e,w))
    g[e].append((s,w))

# far_n, far_w = dfs(1)
# n, w = dfs(far_n)

far_n, far_w = bfs(1)
n, w = bfs(far_n)

print(w)

