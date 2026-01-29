import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 배열크기(2^n * 2^n), 탐색 행(r), 탐색 열(c)
# 출력: r행 c열을 몇 번째로 방문했는지 출력

# 분할정복?
# N > 1 일때 4개 -> 좌상/우상/좌하/우하 로 나눌 수 있음
# n=1일때 z자 1,2,3,4
# 배열 크기에 따라서 n=1 이 될 때까지 재귀 ㄱㄱ, 순서 기록


# 시간 초과 났다네요.. 당연한 N이 15고 2**15  * 2**15 면 시간초과 날 것 같았음 하하
# 규칙을 찾아야한다 행과 열 주어진 것만으로도 알 수 있는 방법!
# def f(i,j,n):
#     global cnt
#     if n == 1:
#         d = cnt * 4
#         arr[i][j] = d
#         arr[i][j+1] = d + 1
#         arr[i+1][j] = d + 2
#         arr[i+1][j+1] = d + 3
#         cnt += 1
#     else:
#         c = 2**(n-1)
#         f(i,j,n-1)
#         f(i,j+c,n-1)
#         f(i+c,j,n-1,)
#         f(i+c,j+c,n-1)



n, r, c = map(int,input().split())
# N = 2**n
# arr = [[0] * N for _ in range(N)]
# cnt = 0

# f(0,0,n)

ans = 0
while n > 0:
    half = 2**(n-1)
    d = half * half
    # 좌상/우상/좌하/우하
    if r < half and c < half:
        pass
    elif r < half and c >= half:
        ans += d
        c -= half
    elif r >= half and c < half:
        ans += 2 * d
        r -= half
    else:
        ans += 3 * d
        r -= half
        c -= half

    n -= 1

print(ans)