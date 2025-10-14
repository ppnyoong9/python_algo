import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
9095번 1,2,3 더하기
'''

# 입력: 테스트케이스(T), 정수(N)
# 출력: n을 1,2,3 의 합으로 나타내는 방법의 수

# 재귀로 시작해서 이것저것 해보다 결국 힌트 보고 말았다..
# 1로 끝나는 경우, 2로 끝나는 경우, 3으로 끝나는 경우 고려
# 예) 8일때 (f(7)의 벙법의 수 + 1), (f(6)의 방법의 수 + 2), (f(5)의 방법의 수 + 3)
# 점화식 = f(n) = f(n-1) + f(n-2) + f(n-3)

t = int(input())

d = [0] * 12
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 12):
    d[i] = d[i - 1] + d[i - 2] + d[i - 3]

for _ in range(t):
    print(d[int(input())])