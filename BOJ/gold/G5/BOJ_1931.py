import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 회의의 수(N), 회의 시작-끝(s,e)
# 출력: 최대 가능 회의

#  끝나는 시각에 맞추어 정렬 (만약 끝나는 시간이 같으면 시작이 더 빠른거 우선으로 하자)
#  회의 시작-끝 정보 돌면서 시작이 이전 회의 후라면 회의 가능

N = int(input())
arr = []

for i in range(N):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x:(x[1],x[0]))

e = arr[0][1]
ans = 1

for i in range(1, N):
    if arr[i][0] >= e:
        e = arr[i][1]
        ans += 1

print(ans)