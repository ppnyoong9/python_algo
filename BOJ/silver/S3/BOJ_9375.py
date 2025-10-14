import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
9375번 패션왕 신해빈
'''

# 입력: 테스트케이스(T), 해빈이가 가진 의상의 수(n), n개의 의상의 이름과 종류
# 출력: 의상을 입을 수 있는 경우의 수


t = int(input())
for _ in range(t):
    n = int(input())
    dic = {}
    cat_n = 0
    for _ in range(n):
        name, cat = input().split()
        if dic.get(cat):
            dic[cat] += 1
        else:
            dic[cat] = 1
            cat_n += 1

    # 모든 종류의 부분집합을 만들 이유가 없다
    arr = list(dic.values())
    # ans = n
    #
    # for i in range(1 << cat_n):
    #     temp_arr = []
    #     for j in range(cat_n):
    #         if i & (1 << j):
    #             temp_arr.append(arr[j])
    #     if len(temp_arr) > 1:
    #         temp = 1
    #         for k in temp_arr:
    #             temp *= k
    #         ans += temp

    # 이 문제의 핵심은 각 종류별로 입거나, 안입거나를 선택하는 것
    # 즉 어떤 종류의 의상이 k개 있다면 선택할 수 있는 경우는 옷 k가지 중 하나를 입거나, 아무것도 안입는 경우
    # -> 총 k+1 가지

    ans = 1

    # 따라서 각 종류의 선택지수를 모두 곱한 값에서 모든 종류에서 아무것도 안입는다를 선택하는 단 하나의 경우만 제거하면 된다.
    for k in arr:
        ans *= (k + 1)

    print(ans - 1)
