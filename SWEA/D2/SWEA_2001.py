import sys
sys.stdin = open('input.txt', 'r')

'''
2001. 파리 퇴치
'''

# 입력: 테스트 케이스(T), 배열의 크기(N), 파리채 크기(M), 배열 정보
# 출력: 최대로 많이 죽일 수 있는 파리

T = int(input())
for tc in range(1,T+1):
    # 배열의 크기(N), 파리채 크기(M)
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for p in range(M):
                for q in range(M):
                    temp += arr[i+p][j+q]
            if max_v < temp:
                max_v = temp

    print(f'#{tc} {max_v}')

