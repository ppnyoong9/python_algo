import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline



'''
17413번 단어 뒤집기 2
'''

# 입력: 문자열 S
# 출력: 각 단어 뒤집기(태그는 제외)

# 태그가 없으면 그냥 split() 해서 단어마다 뒤집기
# 태그가 있으면 그대로 둬야


S = input()

if '<' not in S:
    arr = S.split()
    ans = []
    for word in arr:
        ans.append(word[::-1])
    print(' '.join(ans))

else:
    # 임시로 문자열 저장할 변수
    temp = ''
    # 괄호 flag 와 뒤집을 문자열 flag
    b_flag = False
    for i in range(len(S)):
        # '<' 괄호를 만났을 경우
        if S[i] == '<':
            # 만약 뒤집을 문자열 있으면
            if temp:
                stack = []
                for word in temp.split():
                    stack.append(word[::-1])
                print(*stack,end='')
                temp = ''
            temp += S[i]
            b_flag = True
        # '>' 괄호를 만났을 경우 출력하고 초기화
        elif S[i] == '>':
            temp += S[i]
            print(temp,end="")
            temp = ''
            b_flag = False

        # 괄호가 아닌 문자열인 경우
        else:
            temp += S[i]


    # 아직 출력할 문자열 남아 있으면 출력
    if temp:
        stack = []
        for word in temp.split():
            stack.append(word[::-1])
        print(*stack, end='')


