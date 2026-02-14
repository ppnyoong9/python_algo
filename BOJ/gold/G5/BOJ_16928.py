import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

# 입력: 사다리 수(N), 뱀의 수(M), 사다리 배열
# 출력: 주사위 횟수 최솟값

# BFS로 갈 수 있는 곳 탐색
# 사다리와 뱀 정보 저장 (딕셔너리)
# 사다리면 타고 가고 뱀이면 pass
# **** 사다리만 타고자 하면 안된다
# 사다리만 골라서 타는게 이득인 것 같아 보이지만 오히려 뱀을 타고 후퇴해서 더 좋은 사다리를 만날 수도 있기 때문에 모든 경우를 다 생각해서 길을 찾아가야함


def bfs():
    q = deque([1])
    visited = [-1] * 101
    visited[1] = 0

    while q:
        now = q.popleft()

        for i in range(1, 7):
            next = now + i

            # 범위 벗어나면 pass
            if next > 100:
                continue

            # 사다리나 뱀이 있으면 타기
            if d.get(next):
                next = d.get(next)

            if visited[next] == -1 :

                if next >= 100:
                    return visited[now] + 1

                visited[next] = visited[now] + 1
                q.append(next)


N, M = map(int,input().split())
d = {}

for _ in range(N+M):
    s,e = map(int,input().split())
    d[s] = e

print(bfs())