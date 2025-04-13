import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

'''
1158번 요세푸스
'''

# 원형 큐 문제인가..?

# 입력: 사람 수(N), 제거 될 순번(K)
# 출력: 순서대로 K번쨰 사람을 제거할 때 제거되는 순서


'''시간 초과'''
# N, K = map(int,input().split())
# # 큐 생성
# q = [0] * (N + 1)
# front = -1
# rear = N
#
# # 1번부터 N번까지 사람 채워넣기
# for i in range(N):
#     q[i] = i + 1
#
# # 이제 제거를 해보자
# ans = ''
#
# for _ in range(N):
#     # K번째 요소 제거해야 하는데
#     for _ in range(K):
#         front = (front + 1) % N
#         # 만약 이미 제거한 요소라면 pass
#         if q[front] == -1:
#             while q[front] == -1:
#                 front = (front + 1) % N
#
#     ans += str(q[front])
#     q[front] = -1
#
# print('<',end='')
# print(', '.join(ans),end='')
# print('>',end='')



# 입력: 사람 수(N), 제거 될 순번(K)
# 출력: 순서대로 K번쨰 사람을 제거할 때 제거되는 순서

N, K = map(int,input().split())
# 큐 생성
q = [0] * N
front = 0

# 1번부터 N번까지 사람 채워넣기
for i in range(N):
    q[i] = i + 1

# 이제 제거를 해보자
ans = []

for _ in range(N):
    front = (front + K - 1) % len(q)
    ans.append(str(q.pop(front)))


print('<',end='')
print(', '.join(ans),end='')
print('>',end='')