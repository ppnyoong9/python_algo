import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
2606번 바이러스
'''


# 입력: 컴퓨터의 수(n), 연결된 쌍의 수(m), 쌍 배열
# 출력: 바이러스에 걸리게 되는 컴퓨터의 수

# 1) DFS 이용
# def dfs(node):
#     global cnt
#     cnt += 1
#     visited[node] = 1
#     for next_n in graph[node]:
#         if visited[next_n] == 0:
#             dfs(next_n)
# 
# n = int(input())
# m = int(input())
# 
# graph = [[] for _ in range(n+1)]
# visited = [0] * (n+1)
# 
# for _ in range(m):
#     s, e = map(int,input().split())
#     graph[s].append(e)
#     graph[e].append(s)
# 
# cnt = 0
# dfs(1)
# print(cnt-1)

# 2) BFS 이용
def bfs(s_node):
    cnt = 0
    q = [s_node]
    while q:
        c_node = q.pop(0)

        for n_node in graph[c_node]:
            if visited[n_node]:
                continue

            visited[n_node] = 1
            q.append(n_node)

            cnt += 1

    return cnt - 1


n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

ans = bfs(1)
print(0 if ans < 0 else ans)


