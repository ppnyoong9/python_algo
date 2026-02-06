import sys
sys.stdin = open('input.txt','r')
input =  sys.stdin.readline

# 입력: 테스트케이스(T), 함수식(p), 배열 길이(n), 배열
# 출력: 함수 수행 결과 (에러 발생시 error 출력)

# R = 뒤집기, D = 첫번째 수 버리기

# queue를 이용해서 방향만 left(flag)로 관리하기
# 입력받고 left 변수 선언(True, False)
# for문 함수식 -> r이면 left 변경, d면 if arr 일 때만 하나 빼기 아니면 error 리턴

# 문자열이 좀 까다롭네
#
# T = int(input())
#
# for _ in range(T):
#     p = input()
#     n = int(input())
#     arr = []
#
#     temp = input().replace('[','').replace(']','')
#
#     # 0 <= n
#     if temp:
#         arr = list(map(int, temp.split(',')))
#
#     left = True
#
#     for e in p:
#         if e == 'R':
#             left = not left
#
#         if e == 'D':
#             if not arr:
#                 print('error')
#                 break
#
#             if left:
#                 arr.pop(0)
#
#             else:
#                 arr.pop()
#     else:
#         if not left:
#             arr.reverse()
#
#         print('[',end="")
#         print(*arr,sep=",",end="")
#         print(']')
#

# 좀 깔끔하게 다듬어보자
T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    arr = input().rstrip().strip('[]').split(',')

    # n을 못써먹었는데 애초에 D를 카운트해서 비교하는데 쓰면 유용
    if n < p.count('D'):
        print('error')
        continue
    
    # 문자 인덱싱 이용해보자
    left = True
    s = 0
    e = n

    for c in p:
        if c == 'R':
            left = not left

        if c == 'D':
            if left:
                s += 1

            else:
                e -= 1
    else:
        arr = arr[s:e]

        if not left:
            arr.reverse()

        print(f"[{','.join(arr)}]")