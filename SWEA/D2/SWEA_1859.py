import sys
sys.stdin = open('input.txt','r')

'''
1859. 백만 장자 프로젝트
'''

# 입력: 테스트케이스(T), 일 수(N), N일 동안 매매가
# 출력: 최대 이익

# 무조건 최고 고점에서 팔아야 최대 이득!
# 뒤에서 부터 시작하여 max_v 를 찾고
# 다음 max_v가 나타나면 갱신해가면서
# max_v 와 매매가 차이 더해주기


T = int(input())
for tc in range(1, T+1):
    # 일 수, 매매가 받기
    N = int(input())
    arr = list(map(int,input().split()))

    # 최고 매매가를 저장할 변수
    max_v = 0
    # 최대 이익을 저장할 변수 (정답)
    ans = 0

    # 뒤에서부터 가보자
    for i in range(N-1,-1,-1):
        # 최고 매매가일때는 갱신만
        if max_v < arr[i]:
            max_v = arr[i]
            continue

        ans += max_v - arr[i]

    # 출력
    print(f'#{tc} {ans}')