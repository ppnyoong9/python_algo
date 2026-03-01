import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

# 입력: 테스트케이스 수(T), 레지스토 초기 값(A), 최종값(B)
# 출력: A에서 B로 변환하기 위한 최소한의 명령어 나열

# 명령어
# D: n*2 (if > 9999 -> %10000)
# S: n-1 (n=0 -> 9999)
# L: 자릿수 왼쪽으로 한칸씩 -> (n%1000) * 10 + (n / 1000)
# R: 자릿수 오른쪽으로 한칸씩 -> (n % 10) * 1000 + (n / 10)

# A와 B는 0 이상 10000미만
# 0부투 10000 까지의 숫자가 노드라고 생각해보고 갈 수 있는 경로.. 그래프
# A에서 B까지 가기 위한 최단 경로를 찾아야함
# 경로를 어떻게 저장할 것인가..!? 큐에 문자열을 같이 저장..? 'L', 'LL' 이런식으로?


# 어렵다.. 풀었다기 보다는 힌트를 많이 봤다 ㅜㅜㅜㅜ

"""
시간초과 나서 안되겠다 싶어서 찾아보았고 보니까 역추적하는 방식을 쓰라네요..
"""
# def bfs(s):
#     q = deque([[s,'']])
#     visited[s] = True
#
#     while q:
#         n, o = q.popleft()
#
#         if n == B:
#             return o
#
#         # D
#         next_n = n * 2
#         if next_n > 9999:
#             next_n = n % 10000
#
#         if not visited[next_n]:
#
#             if next_n == B: return o+'D'
#
#             visited[next_n] = True
#             q.append([next_n,o+'D'])
#
#         # S
#         next_n = n - 1
#         if not visited[next_n]:
#             if next_n == B: return o+'S'
#
#             if next_n < 1:
#                 next_n = 9999
#
#             visited[next_n] = True
#             q.append([next_n,o+'S'])
#
#         # L
#         next_n = (n%1000) * 10 + (n // 1000)
#         if not visited[next_n]:
#             visited[next_n] = True
#             q.append([next_n,o+'L'])
#
#         # R
#         next_n = (n % 10) * 1000 + (n // 10)
#         if not visited[next_n]:
#             visited[next_n] = True
#             q.append([next_n, o+'R'])
#
#
# T = int(input())
#
# for tc in range(T):
#     A, B = map(int,input().split())
#     visited = [False] * 10001
#
#     print(bfs(A))

'''
부모 노드랑, 명령어 배열을 저장하는 배열을 넣기
큐에는 오직 방문할 노드만 넣기
만약 B에 도착했다 그러면 A로 거슬러 올라가면서 명령어 배열 합치면 된다
'''

def bfs(s):
    q = deque([s])
    visited[s] = True

    while q:
        n = q.popleft()

        if n == B:
            b = B
            ans = []
            while b != A:
                ans.append(command[b])
                b = parent[b]

            return ''.join(reversed(ans))

        d = (n*2)%10000
        if not visited[d]:
            visited[d] = True
            q.append(d)
            parent[d] = n
            command[d] = 'D'

        s = 9999 if n == 0 else n - 1
        if not visited[s]:
            visited[s] = True
            q.append(s)
            parent[s] = n
            command[s] = 'S'

        l = (n%1000) * 10 + (n // 1000)
        if not visited[l]:
            visited[l] = True
            q.append(l)
            parent[l] = n
            command[l] = 'L'

        r = (n%10) * 1000 + (n // 10)
        if not visited[r]:
            visited[r] = True
            q.append(r)
            parent[r] = n
            command[r] = 'R'

T = int(input())

for tc in range(T):
    A, B = map(int,input().split())
    visited = [False] * 10001

    parent = [0] * 10001
    command = [''] * 10001

    print(bfs(A))