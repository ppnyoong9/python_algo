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
# def kmp(s,p):
#     sl = M      # 문자열 길이
#     pl = len(p) # 찾을 패턴 길이
#
#     lps = [0]* (pl + 1)
#
#     # preprocessing
#     j = 0  # 일치한 개수 == 비교할 패턴 위치
#     lps[0] = -1
#     for i in range(1, pl):
#         lps[i] = j          # p[i] 이전에 일치한 개수
#         if p[i] == p[j]:
#             j+=1
#         else:
#             j=0
#     lps[pl] = j
#
#     # search
#     i = 0   # 비교할 텍스트 위치
#     j = 0   # 비교할 패턴 위치
#     cnt = 0
#
#     while i < sl and j <= pl:
#         if j == -1 or s[i] == p[j]:  # 첫 글자가 불일치 했거나, 일치하면
#             i += 1
#             j += 1
#         else:               # 불일치
#             j = lps[j]
#
#         if j == pl:         # 패턴을 찾을 경우
#             j = lps[j]
#             cnt += 1
#
#     return cnt
#
#
# N = int(input())
# M = int(input())
#
# S = input()
#
# P = 'IOI'
#
# for i in range(1,N):
#     P += 'OI'
#
# print(kmp(S,P))


"""
패턴 Pn이 "IOI"가 연속적으로 N번 나오는 구조
n = 1 이면 1번(IOI) n=2 이면 2번(IOIOI) ...
IOI를 발견하면? 그 다음 글자가 OI인지를 계속 확인하며 카운트 쌓아가면 된다
중요한건 IOI를 발견하고 OI만큼 건너뛰는거....... 굳이 한글자 한글자 다 비교할 필요가 없음
슬라이싱 비용이 생각보다 어마어마 하다네요
인덱스 접근 -> 메모리 주소를 찾아가서 딱 그값만 읽어옴 (O(1))
슬라이싱 -> S[i+i+L] -> L만큼의 새로운 메모리 공간을 할당하고 기존 문자열 복사 후 새로운 문자열 객체 만듬 -> (O(L))

"""
N = int(input())
M = int(input())

S = input()

ans = 0 # 최종 Pn 개수
cnt = 0 # 연속된 OI 개수
i = 0

while i < M-1 :
    # IOI 패턴을 찾은 경우
    if S[i-1] == "I" and S[i] == 'O' and S[i+1] == "I":
        cnt += 1
    
        # 연속된 'OI' 의 개수가 N 이상이면 패턴 일치
        if cnt >= N:
            ans += 1
        
        i += 2  # OI 단위로 건너뛰자

        # 끊기면 카운트 초기화해서 다시 I 부터 찾아야한다
    else:
        cnt = 0
        i+=1

print(ans)