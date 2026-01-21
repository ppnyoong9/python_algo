import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from collections import deque

# 입력: 수빈이의 위치(N), 동생이 있는 위치(K)
# 출력: 동생을 찾는 가장 빠른 시간


# 그래프 BFS 로 풀자 dist
# 최대 정점 100000으로 잡자
# def bfs(start, end):
#     q = deque([start])
#     dist = [-1] * 100001
#     dist[start] = 0
#
#     while q:
#         n = q.popleft()
#
#         # 도착했을 시
#         if n == end:
#             return dist[end]
#
#         # 세가지 선택지 q에 넣기
#         for next_node in (n+1, n-1, n*2):
#             if 0<= next_node < 100001 and dist[next_node] == -1:
#                 dist[next_node] = dist[n] + 1
#                 q.append(next_node)
#
#
# N, M = map(int,input().split())
# print(bfs(N,M))


# 찾아보니 그리디로도 풀 수 있는 듯 하다
# 단, 동생 입장에서 생각해야한다 (와!)
# 동생 입장에서 간다고 생각하면 선택지가 +1 , -1, //2 가 된다
# 만약 동생이 작을 경우 +1 로 다가가는 방법밖에는 없다
# 만약 2로 나눠질 수 있다면 2로 나누는게 유리 아니라면 +1 , -1 고려
def f(n, m):
    if n >= m:
        return n-m
    if m ==1:
        return 1
    if m % 2 == 1:
        return min(f(n, m + 1), f(n, m - 1)) + 1
    return min(m-n, f(n,m//2) + 1)
    

N, M = map(int,input().split())
print(f(N,M))