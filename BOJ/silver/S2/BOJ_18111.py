import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 세로 크기(N), 가로 크기(M), 보유 블록(B), 땅 높이 배열
# 출력: 작업에 걸리는 최소 시간, 땅의 높이

# 블록 제거 = 2초, 블록 심기 = 1초

# 땅의 높이 최대 256 -> 땅 높이를 몇으로 평평하게 만들까? 가 관건
# 높이들을 카운팅 배열 형식으로 저장 (같은 높이는 한 번에 처리)
# 인벤토리 고려해야하는데
# 블록 제거 하면 +1, 심으면 -1

N,M,B = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
cnt_arr = [0] * 257

range_min = 256
range_max = 0

min_t = 500*500*256*2
max_h = 0

for i in range(N):
    for j in range(M):
        h = arr[i][j]
        cnt_arr[h] += 1
        range_min = min(range_min,h)
        range_max = max(range_max,h)

# 256 ~ 0 까지 돌면서 비교해보자
for target_h in range(range_max,range_min-1,-1):
    # 심을 땅 수(p), 제거할 땅 수(m)
    p = 0
    m = 0
    for h in range(range_min,range_max+1):

        if cnt_arr[h] == 0:
            continue

        diff = target_h - h

        # 심기
        if diff > 0:
            p += diff * cnt_arr[h]
        # 제거
        elif diff < 0:
            m += -diff * cnt_arr[h]

    # 불성립: 심을 땅  > + 인벤 보유량 + 제거할 땅
    if p > B+m :
        continue

    if min_t > (p+m*2):
        min_t = p + m*2
        max_h = target_h

print(min_t, max_h)