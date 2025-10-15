import sys
sys.stdin = open('input.txt','r')

input = sys.stdin.readline

'''
9461번 파도 수열
'''

# 입력: 테스트케이스(T), 순서(N)
# 출력: P(N)

t = int(input())


# 가장 긴 변의 길이가 3이 되는 p[6] 부터 점화식 적용
# p[6] = p[5] + p[1]
# p[7] = p[6] + p[2]
# ...
# p[n] = p[n-1] + p[n-5]

p = [0] * 101

p[1] = 1
p[2] = 1
p[3] = 1
p[4] = 2
p[5] = 2

for i in range(6,101):
    p[i] = p[i-1] + p[i-5]

for _ in range(t):
    n = int(input())
    print(p[n])


