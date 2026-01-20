import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 좌표 개수(N), 좌표 배열
# 출력: 좌표 압축을 적용한 결과

# 크기를 생각해서 출력하면 된다
N = int(input())
arr = list(map(int,input().split()))

# s = set(arr)
#
# s_arr = list(s)
#
# s_arr.sort()
#
# d = {}
#
# for i in range(len(s)):
#     d[s_arr[i]] = i
#
# for num in arr:
#     print(d[num],end=" ")

#  비효율적인 부분 정리하고 더 깔끔히
s_arr = sorted(set(arr))

d = {}

for i, num in enumerate(s_arr):
    d[num] = i

print(" ".join(map(str,[d[num] for num in arr])))

