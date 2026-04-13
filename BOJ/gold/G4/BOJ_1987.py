import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from collections import deque
# 입력: 세로(R), 가로(C), 보드 배열
# 출력: 최대 칸 수 (이전 알파벳 X)


def bfs():
    d = ((0,1),(1,0),(0,-1),(-1,0))
    s = set([(0,0,board[0][0])])

    max_len = 1

    while s:
        i, j, path = s.pop()
        max_len = max(max_len,len(path))
        for di, dj in d:
            ni,nj = i+di, j+dj
            if 0 <= ni < r and 0 <= nj < c and board[ni][nj] not in path:
                s.add((ni,nj,path + board[ni][nj]))


    return max_len

r, c = map(int,input().split())

board = [list(input().strip()) for _ in range(r)]

print(bfs())