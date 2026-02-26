import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 입력 X
# 출력: 10000보다 작거나 같은 셀프 넘버 수열

# 10000 을 다 넣은 dict 만들어놓고 for 문으로 value 0인거 뽑아내면 되지 않을까

dic = {}
for i in range(1, 10001):
    dic[i] = 0

for num in range(1, 10001):
    temp = num
    for c in str(num):
        temp += int(c)

    if temp > 10000:
        continue

    dic[temp] += 1

for i in range(1, 10001):
    if dic[i] == 0:
        print(i)