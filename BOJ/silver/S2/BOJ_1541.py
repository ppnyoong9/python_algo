import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
1541번 읽어버린 괄호
'''

#  입력: 식
#  출력: 최소 수


def plus(expression):
    plus_arr = expression.split('+')
    s = 0
    for n in plus_arr:
        s += int(n)

    return s


arr = input().split('-')

ans = 0
for i in range(len(arr)):

    if arr[i] == '':
        continue

    if i == 0:
        if arr[i].isdigit():
            ans += int(arr[i])
        else:
            ans += plus(arr[i])
    else:
        ans -= plus(arr[i])

print(ans)