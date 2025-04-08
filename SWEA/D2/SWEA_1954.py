import sys
sys.stdin = open('input.txt', 'r')

'''
1954. 달팽이 숫자
'''

# 입력: 테스트 케이스(T), 정수(N)
# 출력: 달팽이 숫자 출력 (배열)

# 델타 문제
# 나올 수 있는 방향은 총 4가지 (오른쪽, 아래, 왼쪽, 위)  -> 시계방향으로

# (0, 0)에서부터 시작
# 방향 전환 조건: 벽에 부딪히거나 이미 배열에 요소가 채워져있는 경우


T = int(input())
for tc in range(1, T + 1):
    # 정수 입력 받기
    N = int(input())
    # 값을 채울 배열 생성
    arr = [[0] * N for _ in range(N)]

    # 방향
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # 방향: 오른쪽부터 시작
    d = 0
    # 좌표: (0,0)부터 시작
    i = j =  0

    # N*N 수 채워 나가기
    for k in range(1, (N*N)+1):
        arr[i][j] = k
        # 다음 위치
        ni, nj = i + di[d], j + dj[d]
        # 범위 벗어나지 않고 아직 채워지지 않은 값이면
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            i, j = ni, nj
        # 채울 수 없을 것 같을 경우 방향 바꿔야함
        else:
            d = (d + 1) % 4
            i, j = i + di[d], j + dj[d]

    # 출력
    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j],end=' ')
        print()
