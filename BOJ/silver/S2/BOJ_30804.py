import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

# 입력: 과일의 개수(N), 과일 배열
# 출력: 과일 개수


# (첫 시도) 재귀 => 시간 초과
# set을 이용해서 과일 set으로 관리하고
# len(s) 가 2 될 때까지 재귀함수로 경우의 수 구해보면 될 것 같은데

# 선택지는 앞에서 뺄건지, 뒤에서 뺼건지
# 종료 조건 len(s) < 2
# 가지 치기 max_cnt > cur_cnt
# def recur(cnt):
#     global max_cnt
#
#     if max_cnt > cnt:
#         return
#
#     if len(set(arr)) <= 2:
#         max_cnt = cnt
#         return
#
#     # 앞에서 뺄 경우
#     l = arr.popleft()
#     recur(cnt-1)
#     arr.appendleft(l)
#
#     # 뒤에서 뺄 경우
#     r = arr.pop()
#     recur(cnt-1)
#     arr.append(r)
#
#
# N = int(input())
# arr = deque(map(int,input().split()))
# max_cnt = 0
#
# recur(N)
#
# print(max_cnt)


# (두번째 시도 투 포인터)
# 처음 부터 시작해서 어디까지 갈 수 있을까를 알아보자
N = int(input())
arr = list(map(int,input().split()))

# 과일 종류 cnt를 세서 cnt > 2 (2종류가 넘어가게 되면 왼쪽 포인터를 옮기기)

f = {}

for i in range(10):
    f[i] = 0

l = 0
cnt = 0
ans = 0

for i in range(N):
    right = arr[i]

    # 오른쪽 포인터 이동 -> 과일 추가
    if f[right] == 0 :
        cnt += 1

    f[right] += 1

    # 왼쪽 포인터 이동 과일 종류가 2개가 넘어갈때
    while cnt > 2:
        left = arr[l]
        f[left] -= 1
        if f[left] == 0:
            cnt -= 1
        l += 1

    ans = max(ans, i-l)

print(ans+1)