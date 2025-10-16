import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
1012번 유기농배추
'''


# 입력: 테스트케이스(T), 가로*세로(M*N), 배추가 심어져 있는 개수(K), 배추의 위치
# 출력: 필요한 최소의 배추흰지렁이 수

# DFS

def dfs(si, sj, m, n):
    s = [(si, sj)]

    while s:
        i, j = s.pop()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and field[ni][nj] == 1:
                field[ni][nj] = 0
                s.append((ni,nj))

def bfs(si,sj,m,n):
    pass



t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    field = [[0] * m for _ in range(n)]

    ans = k

    q = []

    for _ in range(k):
        j, i = map(int, input().split())
        field[i][j] = 1

    #  밭을 돌면서 배추가 발견되면 주변 탐색 가볼 예정
    cnt = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                dfs(i, j, m, n)
                cnt += 1

    print(cnt)
