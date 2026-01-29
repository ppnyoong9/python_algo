import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 정수(N), 문자열 길이(M), 문자열(S)
# 출력: IOI..  -> Pn 몇 군데 포함되어 있는지

# 시간초과
# N = int(input())
# M = int(input())
#
# S = input()
#
# P = 'IOI'
#
# for i in range(1, N):
#     P += 'OI'
#
# ans = 0
#
# l = len(P)
#
# for i in range(M):
#     if S[i:i+l] == P:
#         ans += 1
#
# print(ans)


# KMP 알고리즘
def kmp(s,p):
    sl = M
    pl = len(p)

    lps = [0]* (pl + 1)

    # preprocessing
    j = 0 # 일치한 개수 == 배교할 패턴 위치
    lps[0] = -1
    for i in range(1, pl):
        lps[i] = j          # p[i] 이전에 일치한 개수
        if p[i] == p[j]:
            j+=1
        else:
            j=0
    lps[pl] = j

    # search
    i = 0   # 비교할 텍스트 위치
    j = 0   # 비교할 패턴 위치

    while i < sl and j <= pl:
        if j == -1 or s[i] == p[j]:  # 첫 글자가 불일치 했거나, 일치하면
            i += 1
            j += 1
        else:               # 불일치
            j = lps[j]
        
        if j == pl:         # 패턴을 찾을 경우
            j = lps[j]


N = int(input())
M = int(input())

S = input()

P = 'IOI'

for i in range(1,N):
    P += 'OI'