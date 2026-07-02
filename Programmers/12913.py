# 문제: 땅따먹기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12913?language=python3

# [성능 요약] 메모리: 43.3 MB 시간: 200.85 ms
"""
정확성: 59.8
효율성: 40.2
합계: 100.0 / 100.0
"""
# def solution(land):
#
#     dp = [[0] * 4 for _ in range(len(land))]
#
#     dp[0] = land[0]
#
#     for r in range(1, len(land)):
#         for c in range(4):
#             max_v = 0
#             for k in range(4):
#                 if k==c: continue
#                 max_v = max(max_v, dp[r-1][k])
#             dp[r][c] = land[r][c] + max_v
#
#     return max(dp[len(land)-1])


# [성능 요약] 메모리: 43.7 MB 시간: 103.69 ms
"""
채점 결과
정확성: 59.8
효율성: 40.2
합계: 100.0 / 100.0
"""
def solution(land):

    dp = [[0] * 4 for _ in range(len(land))]

    dp[0] = land[0]

    for r in range(1, len(land)):
        dp[r][0] = max(dp[r-1][1],dp[r-1][2],dp[r-1][3]) + land[r][0]
        dp[r][1] = max(dp[r-1][0],dp[r-1][2],dp[r-1][3]) + land[r][1]
        dp[r][2] = max(dp[r-1][0],dp[r-1][1],dp[r-1][3]) + land[r][2]
        dp[r][3] = max(dp[r-1][0],dp[r-1][2],dp[r-1][2]) + land[r][3]

    return max(dp[len(land)-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))