import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline


'''
2108번 통계학
'''

# 입력: 수의 개수(N), N개의 정수
# 출력: 각 통계값

'''
산술평균 : (N개의 수들의 합) / N (소수점 첫째 자리에서 반올림)
중앙값 : 오름차순 정렬 후 중앙값
최빈값 : N개의 수들 중 가장 많이 나타나는 값 (여러개 있을 때에는 최빈값 중 두번째로 작은값)
범위 : N개의 수들 중 최댓값 - 최솟값
'''

n = int(input())

arr = [0] * n
sum = 0
num_dict =  {}
max_v = -4000
min_v = 4000

for i in range(n):
    k = int(input())
    arr[i] = k
    sum += k
    if num_dict.get(k):
        num_dict[k] += 1
    else:
        num_dict[k] = 1
    max_v = max(max_v,k)
    min_v = min(min_v,k)

arr.sort()

dict_arr = list(num_dict.items())
dict_arr.sort(key=lambda x : (-x[1], x[0]))

# 산술평균
print(round(sum/n))
# 중앙값
print(arr[(n-1)//2])
# 최빈값
if len(dict_arr) > 1:
    if dict_arr[0][1] == dict_arr[1][1]:
        print(dict_arr[1][0])
    else:
        print(dict_arr[0][0])
else:
    print(dict_arr[0][0])
# 범위
print(max_v-min_v)