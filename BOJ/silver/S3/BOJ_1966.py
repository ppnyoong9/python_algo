import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from collections import deque

'''
1966번 프린터 큐
'''

# 입력: 테스트케이스(T), 문서의 개수(N), 문서의 순서(M), 중요도 배열
# 출력: 문서가 몇 번째로 인쇄되는지 출력

t = int(input())
for tc in range(t):
    n, m = map(int,input().split())
    arr = list(map(int,input().split()))
    q = deque()

    for i in range(n):
        q.append([i,arr[i]])

    ans = 0

    while q:
        idx, value = q.popleft()
        max_v = max(arr)

        if value < max_v:
            q.append([idx,value])
        else:
            ans += 1
            arr[idx] = -1
            if idx == m:
                print(ans)
                break
