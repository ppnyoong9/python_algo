import sys

sys.stdin = open('input.txt', 'r')

'''
9093번 단어 뒤집기
'''

# 입력: 테스트케이스(T), 대상 문자열
# 출력: 문장의 단어를 모두 뒤집어 출력

'''
방법 1 ) 인덱스로만 해보기
'''

# T = int(input())
# for _ in range(T):
#     data_list  = input().split()
#     ans = ''
#     for data in data_list:
#         temp = ''
#         for i in range(len(data)-1,-1,-1):
#                temp += data[i]
#         ans += temp + ' '
#
#     print(ans)

'''
방법 2) 인덱스 슬라이싱 활용
'''
T = int(input())
for _ in range(T):
    data_list = input().split()
    ans = ''
    for data in data_list:
        ans += data[::-1]+' '

    print(ans)
