import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

# 입력: 초기 값(A), 대상 값(B)
# 출력: 연산의 최솟값

# *2 또는 1을 오른쪽에 추가(*10 + 1)

# 갈 수 있는 타겟 값들을 정점으로 보는 BFS 활용하기에는..
# 10^9 만큼이라 정점을 다 미리 만들어놓기에는 시간초과 뜰 것 같다
# dict에 그때 그때 저장?

# A, B = map(int,input().split())
#
# # 연산횟수 저장
# d  = {A: 1}
#
# q = deque([A])
#
# ans = 0
#
# while q:
#     n = q.popleft()
#
#     if n == B:
#         ans = d[n]
#         break
#
#     t = n*2
#     if t not in d and t <= B:
#         d[t] = d[n] +1
#         q.append(t)
#
#     t = n*10 + 1
#     if t not in d and t <= B:
#         d[t] = d[n] +1
#         q.append(t)
#
# print(ans if ans > 0 else -1)



# 아니면 B -> A 로 내려오는 방법 (거꾸로 생각하기)
# B가 2로 나누어떨어지면 2로 나누고 끝자리가 1이라면 1을 제거
# 위의 두 경우 둘 다 안되는데 A에 도달하지 않았다면 라면 A를 만들지 못하는 숫자임
A, B = map(int,input().split())
ans = 1

while B > A:
    if B % 2 == 0:
        B //= 2
    elif B % 10 == 1:
        B //= 10
    else:
        break

    ans += 1

print(ans if B==A else -1)