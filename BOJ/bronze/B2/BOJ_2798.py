import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline



'''
2798번 블랙잭
'''

# 입력: 카드의 개수(N), 대상 수(M), 카드에 쓰여 있는 수
# 출력: M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합


# 카드의 개수, 대상 수 받기
# n, m = map(int, input().split())
# arr = list(map(int,input().split()))
#
# ans = 0
#
# for i in range(n):
#     for j in range(i+1,n):
#         for q in range(j+1,n):
#             s = arr[i] + arr[j] + arr[q]
#             if s > m:
#                 continue
#             else:
#                 ans = max(ans,s)
#
# print(ans)

n,m = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort(reverse=True)

ans = 0
for i in range(n):
    a = i
    left = i + 1
    right = n - 1
    while left < right:
        s = arr[a] + arr[left] + arr[right]
        if s > m :
            left +=1
        else:
            ans = max(s,ans)
            right -= 1

print(ans)

