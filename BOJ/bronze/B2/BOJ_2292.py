import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline().strip()

'''
2292번 벌집
'''

# 보니까 6*N 만큼 주변을 둘러싸는게 늘어나는 것 같다 6개, 12개, 18개...
# 즉, 주변을 둘러싸고 있는 각 단계의 끝점들은 7, 19, 37
# 각 단계 범위안에 들어오는지 확인하면 될 것 같다

# 입력: 숫자(N)
# 출력: N까지 가기위한 최소 개수의 방


N = int(input)

result = 1
temp = 1
while N > temp:
    temp += 6*(result)
    result += 1

print(result)
