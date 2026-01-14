import sys
#sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 가진 랜선 개수(K), 필요한 랜선 개수(N), 가진 랜선의 각 길이
# 출력: 최대 랜선의 길이

# 단순히 몫을 n부터 시작해서 1씩 줄어나가보면 되지 않나? 1부터 늘려보면 되지 않나 했는데..? 2 4 10 8 의 테스트 케이스처럼 순차적으로 접근해서 찾기 힘든 케이스가 많았따
# 그렇다고 다 찾기에는 시간이 오래 걸리지 않나 했는데 이진 탐색 문제였다..
# 1 ~ 가장 큰 값 까지 범위로 길이를 구해야함

k, n = map(int,input().split())
arr = [0] * k

for i in range(k):
    arr[i] = int(input())

start = 1
end = max(arr)
ans = 0

while start <= end:
    # 중간값
    middle = (start + end) // 2
    
    # middle 길이로 잘랐을 떄 랜선 개수
    q_sum = 0
    for i in range(k):
        q_sum += arr[i] // middle
    
    # 더 자를 수 있을 것 같을 때
    if q_sum >= n:
        ans = middle
        start = middle + 1

    # 너무 길게 잘라서 길이를 줄여야할때
    else:
        end = middle - 1

print(ans)