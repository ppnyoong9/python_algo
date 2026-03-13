import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 테스트 케이스(T), 열의 길이(n), 스티커 배열
# 출력: 스티커 점수의 최댓값

# row = 0 일떄 -> 후보지 [0,j-2], [0,j-1]
# row = 1 일때 -> 후보지 [1,j-2], [1,j-1]

T = int(input())
for tc in range(T):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(2)]

    if n > 1:
        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]

        for j in range(2,n):
            # row=0
            arr[0][j] += max(arr[1][j-2],arr[1][j-1])

            # row=1
            arr[1][j] += max(arr[0][j-1],arr[0][j-2])

    print(max(arr[0][n-1],arr[1][n-1]))