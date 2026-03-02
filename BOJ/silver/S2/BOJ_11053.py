import sys
sys.stdin  = open('input.txt','r')
input = sys.stdin.readline

# 입력: 수열 A의 크기(N), 자연수 배열
# 출력: 가장 긴 증가하는 부분 수열의 길이

'''
시간초과 
부분집합을 set 자료형 에 넣은뒤 따져보기
'''

# N = int(input())
# arr = list(map(int,input().split()))
#
# ans = 1
#
# # 부분 집합을 다 구해서 따져봐야 할 듯
# for i in range(1 << N):
#     temp = []
#     for j in range(N):
#         if i & (1<<j):
#             if arr[j] not in temp:
#                 temp.append(arr[j])
#     if temp == sorted(temp):
#         ans = max(ans,len(temp))
#
# print(ans)



'''
내 기준에서 나보다 작은 아이들을 살펴보자!
dp에 길이를 저장해놓고
만약 나보다 작은 값들이 여러개 일때
어디에 붙어야 길이가 최대가 될까를 생각해봐야한다
'''

# N = int(input())
# arr = list(map(int,input().split()))
#
# # 보완 포인트 -> N+1 까지 할 필요 없음 N으로 충분
# dp = [0] * (N+1)
#
# dp[0] = 1
# for i in range(1, N):
#     for j in range(0,i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j]+1)
#
#     # 보완 포인트 -> 애초에 dp 배열을 1로 다 채워놨으면 될 일
#     if dp[i] == 0:
#         dp[i] = 1
#
# print(max(dp))

'''
풀이를 더 찾아보았는데
수열에서 탐색하면서 내가 가장 큰 값인 것 같다 -> 집어넣기
앞에 나보다 더 큰 값이 있다 -> 이 큰 값 대신 나로 교체하여 유리한 후보군으로 만들어서 탐색
자리교체를 한다고 생각하면 될 듯
이런 방법이 있다 
10, 20, 15 , 30 이라고 하면
[10], [10, 20], [10, 15(교체)],[10,15,30] 이런식으로 더 유리하게!

* 주의 무조건 큰 값이 아닌 내가 들어갈 수 있는 자리를 찾아 들어가야한다
[10,20,40,50] 에 25가 들어가야한다고 하면 50의 자리가 아니라 40 자리에 들어가야함
'''

N = int(input())
arr = list(map(int,input().split()))

l = [arr[0]]

for i in range(1, N):
    for j in range(len(l)):
        if arr[i] <= l[j]:
            l[j] = arr[i]
            break
    else:
        l.append(arr[i])

print(len(l))