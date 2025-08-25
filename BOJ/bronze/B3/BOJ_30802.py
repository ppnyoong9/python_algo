import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
30802번 웰컴 키트
'''

# 티셔츠 S, M, L, XL, XXL, XXXL의 6가지 사이즈
# 티셔츠는 같은 사이즈의 T장 묶음으로만 주문 가능 -> 남아도 되지만 부족해서는 안된다
# 펜은 한 종류로, P자루씩 묶음으로 주문하거나 한 자루씩 주문 -> 펜은 남거나 부족해서는 안되고 정확히 참가자 수만큼
# 티셔츠를 T장씩 최소 몇 묶음 주문해야 하는지, 그리고 펜을 P자루씩 최대 몇 묶음 주문할 수 있고, 그 때 한 자루씩 몇 개 주문하는지

# 입력: 참가자의 수(N), 티셔츠 사이즈별 신청자의 수 (S, M, L, XL, XXL, XXXl ), 티셔츠 묶음 수(T), 펜의 묶음 수(P)
# 출력: 티셔츠 묶음 최소 주문 수, 펜 주문수, 펜 한자루 당 몇 개 주문하는지

N = int(input())
size_arr = list(map(int,input().split()))
T,P =  map(int,input().split())

t = 0

#  배열을 돌면서 부족한지 체크
for size in size_arr:
    if size == 0 :
        continue
    elif size%T == 0:
        t += size//T
    else:
        t += size//T+1

print(t)
print(N//P, N%P)
