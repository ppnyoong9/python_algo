import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 물건 수(N), 최대 소지 가능 무게(K), 각 물건의 무게,가치(W,V)
# 출력:배낭에 넣을 수 있는 물건들의 가치합 최대값


'''
물건(i), 부피(j), 2차원 배열 만들기
dp[i]: i 물건까지 고려해 채웠을떄의 최대가치
물건을 담을지 안담을지 고려, 만약 담을 수 있다면 최대한 부피 채워서 담아야 이득임
do[i][j] = max(물건 i를 담지 않았을떄의 최대값, 물건 i를 담고 남는 공간도 꽉 채워서 담아서 나올 수 있는 값)
dp[i][j] = max(dp[i-1][j], dp[i-1][j-V] + K)
'''

N, K = map(int,input().split())
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1,N+1):
    W, B = map(int,input().split())
    for j in range(1,K+1):
        # 담을 수 없을떄
        if W > j:
            dp[i][j] = dp[i-1][j]
        # 담을 수 있을떄는 비교
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W] + B)

print(dp[N][K])
