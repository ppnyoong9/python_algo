import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
2869번 달팽이는 올라가고 싶다
'''

# 입력: 달팽이가 올라갈 수 있는 거리(A), 밤에 잠을 자는 동안 미끄러지는 거리(B), 높이(V)
# 출력: 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지

a,b,v = map(int,input().split())

ans = 1

if a <= v:
    v -= a
    ans += v // (a - b)
    if v%(a-b) > 0:
        ans += 1


print(ans)