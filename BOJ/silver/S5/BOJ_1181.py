import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

'''
1181번 단어 정렬
'''

# 입력: 단어의 개수(N), 소문자로 이루어진 단어
# 출력: 정렬된 단어

# 길이가 짧은 것 부터
# 길이가 같으면 사전 순으로


n = int(input())

arr = []

for i in range(n):
    s = input().strip()
    if s not in arr:
        arr.append(s)

arr.sort(key=lambda x: (len(x),x))

for i in range(len(arr)):
    print(arr[i])
