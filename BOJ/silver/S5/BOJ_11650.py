import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
11650번 좌표 정렬하기
'''

# 입력: 점의 개수(N), 위치(x, y)
# 출력: 점을 정렬한 결과

n = int(input())
arr = [0] * n

# 입력 받기
for i in range(n):
    x,y = map(int,input().split())
    arr[i] = [x,y]

# 정렬
arr.sort(key=lambda x:(x[0],x[1]))

# 출력
for j in range(n):
    print(f'{arr[j][0]} {arr[j][1]}')