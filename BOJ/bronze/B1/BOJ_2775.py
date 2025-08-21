import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

'''
2775번 부녀회장이 될테야
'''

# 입력: 테스트케이스(T), 층 수(k), 호 수(n)
# 출력: 해당 집에 거주민 수

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    # 아파트 배열
    arr = [[0] * n for _ in range(k+1)]
    
    # 1층 채우기
    for i in range(n):
        arr[0][i] = i+1

    # 각 층 채우기
    for i in range(1,k+1):
        for j in range(n):
            for q in range(j+1):
                arr[i][j] += arr[i-1][q]

    # 출력
    print(arr[k][n-1])