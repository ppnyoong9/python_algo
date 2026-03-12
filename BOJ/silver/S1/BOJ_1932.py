import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 삼각형의 크기(n), 정수 삼각형
# 출력: 합이 최대가 되는 경로의 합


"""
너무..복잡하게 내가 만든 배열처럼 1차원적으로 생각해서 풀었다
"""
# n = int(input())
#
# dp = [0] * (n*(n+1)//2 +1)
#
# idx = 4
#
# ms = 1
#
# for i in range(n):
#     ms += i
#
#     s = input().split()
#
#     # 1번째 요소
#     if ms == 1:
#         dp[1] = int(s[0])
#         continue
#
#     # 2,3 번째 요소
#     if ms == 2:
#         dp[2] = int(s[0]) + dp[1]
#         dp[3] = int(s[1]) + dp[1]
#         continue
#
#
#     for j in range(len(s)):
#
#         cur = int(s[j])
#
#         left = idx - i - 1
#         right = left + 1
#
#         # 왼쪽 가장자리
#         if idx == ms:
#             dp[idx] = cur + dp[right]
#         # 오른쪽 가장자리
#         elif idx == ms + i:
#             dp[idx] = cur + dp[left]
#         # 가운데 낀거면 왼쪽이랑 오른쪽중 max 고르기
#         else:
#             dp[idx] = cur+max(dp[left],dp[right])
#
#         idx +=1
#
# print(max(dp))

''''

i행의 j번째 요소 -> 2차원 배열 사용
dp[i][j] = cur + max(dp[i-1][j-1], dp[i-1][j])

   [3,1], [3,2], [3,3]
[4,1], [4,2], [4.3], [4,4]

이렇게 구하고 마지막 행에서 max를 출력하면 된다
'''

n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))

# arr를 dp처럼 바로 활용해도 될 것 같다
for i in range(1,n):
    for j in range(i+1):
        # 왼쪽 가장자리
        if j == 0:
            arr[i][j] += arr[i-1][j]
        # 오른쪽 가장자리
        elif j == i:
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += max(arr[i-1][j],arr[i-1][j-1])

print(max(arr[n-1]))


'''
오 추가로 아래에서부터 올라갈 수도 있음
자식 2명은 무조건 가지고 있기 때문에 
굳이 조건 나눠가며 할 필요가 없어짐
'''
# for i in range(n-2,-1,-1):
#     for j in range(len(arr[i])):
#         arr[i][j] += max(arr[i+1][j],arr[i+1][j+1])
#
# print(max(arr[n-1]))
