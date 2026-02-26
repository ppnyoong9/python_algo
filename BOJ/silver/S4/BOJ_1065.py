import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 자연수(N)
# 출력: 한수의 개수 ( 1 <= ans <= N)

# 등차 수열

N = int(input())

ans = 0


for i in range(1, N+1):
    if  i // 10 < 2:
        ans += 1
        continue

    temp = str(i)
    diff = int(temp[1]) - int(temp[0])

    for j in range(1, len(temp)):
        if diff != int(temp[j])-int(temp[j-1]):
            break
    else:
        ans += 1

print(ans)



