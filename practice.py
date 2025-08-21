# 입력: 건물의 개수(N), N개의 건물의 높이
# 출력: 조망권이 확보된 세대의 수

for tc in range(1,11):
    n = int(input())
    arr = list(map(int,input().split()))

    ans = 0
    for i in range(2,n-2):
        max_v = 0
        for j in range(i-2,i+3):
            if j == i:
                continue
            max_v = max(max_v, arr[j])
        if arr[i] > max_v:
            ans += arr[i] - max_v

    print(f'#{tc} {ans}')