import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

'''
2805번 나무자르기
'''

# 입력: 나무의 수(N), 필요한 나무 길이(M), 나무 높이 배열(arr)
# 출력: 절단기 높이

# 이것도 설마 반절씩 높이 줄여가면서 탐색하는 이진 탐색
# 높이 낮으면 더 잘리고 높이 높으면 덜 잘림
# m 보다 많이 남으면 높이 높여도 된다
# m 만큼 안나오면 높이 낮혀야 한다

n, m = map(int,input().split())
arr = list(map(int,input().split()))

ans = 0

start = 1
end = 1000000000

while start <= end:
    s = 0
    mid = (start+end) // 2

    for x in arr:
        if x > mid:
            s += x-mid
            if s >= m:
                break

    if s >= m:
        start = mid+1
        ans = mid
    elif s < m:
        end = mid-1

print(ans)