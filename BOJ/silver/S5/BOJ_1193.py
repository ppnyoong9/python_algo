import sys
# sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 순서(x)
# 출력: 순서에 해당하는 x번째 분수

# 1 <= x <= 10,000,000

# 하나는 증가 하나는 감소

x = int(input())

"""
for 문 2번 돌리기 -> 당연히 시간초과라네용..
"""
# temp = 0
#
# for i in range(1, 10000000):
#     for j in range(1, i+1):
#         temp += 1
#         if x == temp:
#             if i % 2 == 0:
#                 print(f'{j}/{i-j+1}')
#             else:
#                 print(f'{i-j+1}/{j}')
#             exit()

"""
대각선 번호를 구해서 규칙을 약간.. 비효율적으로 생각한 것 같다
수학적이진 않음
"""
temp = 0
r = 0
for i in range(1, 10000000):
    temp += i

    if temp >= x:
        r = i
        break

# temp = 10
# temp - r  = 6
# 4,7 ->  1/4
# 4,8 ->  2/3
# 4,9 ->  3/2
# 4,10 ->  4/1

# asc = x - (temp - r)
# des = temp - x + 1
#

#
# if r % 2 == 0:
#     print(f'{asc}/{des}')
# else:
#     print(f'{des}/{asc}')
#


# 수학적 풀이
# 대각선 번호 찾기 -> 1번째 대각선 = 1개 , 2번째 대각선 = 2개, 3번째 대각선 = 3개
# 대각선 번호(y)와 그 대각선 안에 몇 번째인지(x)를 쉽게 구할 수 있음

y = 1
while x > y:
    x -= y  # 대각선 안에서 몇 번째 인지를 알기 위해 갯수만큼 빼주기
    y += 1  # 대각선 번호는 갈수록 증가

# 이제 대각선이 짝수냐 홀수냐일때가 중요 ( 방향이 번갈아가며 바뀌기 때문에 )
if y % 2 == 0:
    a = x
    b = y - x + 1
else:
    a = y - x + 1
    b = x

print(f'{a}/{b}')
