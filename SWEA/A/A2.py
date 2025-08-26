import sys
sys.stdin = open('input.txt','r')

# 입력: 테스트케이스(T), 지하철 역(N), 역 별 이용 수 배열
# 출력: 제일 높은 타당도


t = int(input())
for tc in range(1, t+1):
    # 역 수, 지하철 이용객 수 배열 받기
    n = int(input())
    arr = list(map(int,input().split()))

    ans = 0
    
    # 역은 무조건 한 칸 씩 띄워져 있어야한다
    for i in range(n-6):
        for j in range(i+2, n-4):
            for p in range(j+2, n-2):
                for q in range(p+2, n):
                    # 겹치지 않는 경우 2가지가 있다!
                    ans = max(ans,(arr[i]+arr[j])**2 + (arr[p]+arr[q])**2)
                    ans = max(ans, (arr[i]+arr[q])**2 + (arr[j]+arr[p])**2)
   
    print(f'#{tc} {ans}')