import sys
# sys.stdin = open('input.txt','r')
input = sys.stdin.readline

'''
1436번 영화감독 숌
'''

# 입력: 순서(N) 
# 출력: 영화의 제목에 들어간 수


n = int(input())
arr = [0]*10001
j = 1

for i in range(666, 2666800):
    if '666' in str(i):
        arr[j] = i
        j += 1

print(arr[n])
