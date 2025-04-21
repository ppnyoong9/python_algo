import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline



'''
10799번 쇠막대기
'''

# '()' 는 레이저
# 쇠막대기 또한 '(', ')' 로 표현

# '(' 개수를 세다가 ')' 를 만나면 개수 빼기

# 입력: 쇠막대기와 레이저의 배치
# 출력: 잘려진 쇠막대기 조각의 총 개수

arr = list(input().strip())

# 쇠막대기 카운팅, 잘린 개수 카운팅
cnt = 1
ans = 0

for i in range(1, len(arr)):
    if arr[i] == '(':
        cnt += 1
    else:
        cnt -= 1
        if arr[i-1] == '(':
            # 자를 경우 쇠막대기 개수만큼 잘린 조각 카운팅
            ans += cnt
        else:
            # 쇠막대기 끝인 경우 잘린 조각 카운팅
            ans += 1

print(ans)

