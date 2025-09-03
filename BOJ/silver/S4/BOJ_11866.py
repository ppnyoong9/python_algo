import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


'''
11866번 요세푸스 문제 0
'''

# 입력: 사람 수(N), 순서(K)
# 출력: 요세푸스 순열
# 원형 큐 문제

n, k = map(int, input().split())

# 일단 큐 채워넣기
q = [i + 1 for i in range(n)]
ans = [''] * n

# 현재 위치
c = -1

for i in range(n):
    temp = 0
    while temp < k:
        c += 1
        c = c % n
        if q[c] != -1:
            temp += 1
    ans[i] = str(q[c])
    q[c] = -1

print(f"<{', '.join(ans)}>")
