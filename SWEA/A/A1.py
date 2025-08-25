import sys
sys.stdin = open('input.txt','r')

# 입력: 테스트케이스(T), 줄 수(N), 사과의 순서와 위치
# 출력: M개의 사과를 먹기 위한 최소한의 회전 수

# 방향에 따라서 회전횟수 구할 수 있음
def f(d,i):
    x1, y1 = apple[i]
    x2, y2 = apple[i+1]
    change = [[3, 1, 2, 3], [3, 3, 1, 2], [2, 3, 3, 1], [1, 2, 3, 3]]
    if x1 > x2  and y1 < y2:
        return change[d][0]
    elif x1 < x2 and y1 < y2:
        return change[d][1]
    elif x1 < x2 and y1 > y2:
        return change[d][2]
    else:
        return change[d][3]

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]


    apple = [[0,0] for i in range(11)]
    m = 0

    # 사과 위치 찾아놓기
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                apple[arr[i][j]] = i,j
                m+=1

    # 방향: 우하좌상
    dir = [0,1,2,3]

    ans = 1
    d = 1
    i = 1

    for _ in range(m-1):
        temp = f(d%4, i)
        ans += temp
        d += temp
        i += 1

    print(f'#{tc} {ans}')