import sys
sys.stdin = open('input.txt', 'r')

'''
1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기
'''

# 입력: 테스트 케이스(T), 테스트 케이스 번호, 점수
# 출력: 최빈수 출력

# 최빈수가 여러 개 일때는 가장 큰 점수를 출력
# 카운트 배열 활용

T = int(input())
for _ in range(T):
    tc = int(input())
    c = [0] * 101

    arr = list(map(int,input().split()))

    for num in arr:
        c[num] += 1


    max_v = 0
    max_idx = 0

    for i in range(100,-1,-1):
        if max_v < c[i]:
            max_v = c[i]
            max_idx = i
            
    # 출력
    print(f'#{tc} {max_idx}')