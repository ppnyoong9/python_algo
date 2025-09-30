import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

'''
1764번 듣보잡
'''


# 입력: 듣도 보도 못한 사람의 수 (N), 보도 못한 사람의 수(M), N개의 듣도 못한 사람 이름, N+2 번째 줄부터 보도 못한 사람 이름
# 출력: 듣보잡의 수와 그 명단을 사전순으로 출력

n,m = map(int,input().split())

a = set()
b = set()

for i in range(n):
    a.add(input().strip())

for j in range(m):
    b.add(input().strip())

# 교집합 구하기
arr = list(a&b)

# 사전순 정렬
arr.sort()

# 출력
print(len(arr))
for i in arr:
    print(i)

