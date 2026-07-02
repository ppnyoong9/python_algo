import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 테스트 케이스(T), 문제 수(N), 문제의 정보(지식 a, 구현력 b, 사고력 c, 마감기한 p)
# 출력: 계획을 지킬수 있다면  YES, 아니면 NO

T = int(input())

for tc in range(T):
    N = int(input())

    sa, sb, sc = 0, 0 ,0
    day = 0

    ans = ""

    for i in range(N):
        a, b, c, p = map(int,input().split())

        if sa < a:
            day += a - sa
            sa += a - sa

        if sb < b:
            day += b - sb
            sb += b - sb

        if sc < c:
            day += c - sc
            sc += c - sc

        if day < p:
            day += 1
        else:
            ans = "NO"

    if ans == "NO":
        print(ans)
    else:
        print("YES")