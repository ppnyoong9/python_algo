import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

'''
4949번 균형잡힌 세상
'''

# 입력: 문자열
# 출력: 균형을 이루고 있으면 'yes', 아니면 'no'

# 괄호는 (), [] 2가지
# Stack에 (, [ 왼쪽 괄호들을 넣은 후에
# 마지막까지 stack 비워져 있지 않거나 짝이 안맞으면 균형 x

pair = {')':'(',']':'['}

while True:
    st = input()
    if st == ".":
        break
    s = [0] * len(st)
    top = -1
    for c in st:
        # 왼쪽 괄호일 경우 stack 에 집어넣기
        if c in '([':
            top +=1
            s[top] = c
        if c in ')]':
            # 만약 짝이 맞으면
            if pair[c] == s[top]:
                #  짝 데리고 떠나기
                top -= 1
            else:
                print('no')
                break

    # 만약 오른쪽 짝이 부족한 경우 (짝이 안맞는 경우)
    else:
        if top > -1:
            print('no')
            continue

        print('yes')


