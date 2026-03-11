import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 노드의 개수(N), 노드/왼쪽 자식 노드/오른쪽 자식 노드
# 출력: 전위 순회, 중위 순회, 후위 순회

# 전위 순회
def pre_order(n):
    if n:
        print(n,end='')
        pre_order(left[n])
        pre_order(right[n])

# 중위 순회
def in_order(n):
    if n:
        in_order(left[n])
        print(n,end='')
        in_order(right[n])

# 후위 순회
def post_order(n):
    if n:
        post_order(left[n])
        post_order(right[n])
        print(n,end='')

N = int(input())

left = {}
right = {}

for _ in range(N):
    p, l, r = input().split()

    left[p] = {}
    right[p] = {}

    if l != '.':
        left[p] = l

    if r != '.':
        right[p] = r

pre_order('A')
print()
in_order('A')
print()
post_order('A')