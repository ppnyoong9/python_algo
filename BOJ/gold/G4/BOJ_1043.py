import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 입력: 사람 수(N), 파티의 수(M), 진실을 아는 사람 정보, 각 파티에 오는 사람들 번호
# 출력: 과장된 이야기 할 수 있는 파티 개수 최댓값

'''
union-find 활용
'''
# def find_set(x):
#     # 대표자가 (자기 자신이 아닌) 따로 있으면
#     while parents[x] != x:
#         # 대표자 찾으면서 경로 압축
#         parents[x] = parents[parents[x]]
#         x = parents[x]
#     return x
#
# def union(x, y):
#     ref_x = find_set(x)
#     ref_y = find_set(y)
#     if ref_x != ref_y:
#         if ref_x < ref_y:
#             parents[ref_y] = ref_x
#         else:
#             parents[ref_x] = ref_y
#
# N, M = map(int,input().split())
# T, *t_arr = map(int,input().split())
#
# # 1-n까지의 집합 생성 (초기 대표자는 자기 자신)
# parents = [i for i in range(N+1)]
#
# # 0번 노드를 진실 그룹을 묶는 대표자로 삼자
# for t_num in t_arr:
#     union(0, t_num)
#
# # 파티 목록 저장
# p_arr = []
#
# for i in range(M):
#     n, *temp = map(int,input().split())
#     p_arr.append(temp)
#     for j in range(1,n):
#         union(temp[j-1], temp[j])
#
# cnt = 0
# for x in p_arr:
#     for y in x:
#         if find_set(0) == find_set(y):
#             break
#     else:
#         cnt += 1
#
# print(cnt)

'''
Set 자료형 활용
진실을 아는 사람을 모은 set 하나
파티 목록을 파티 수(M번) 만큼 반복해서 교집합일 때 진실 set에 넣음
마지막에 파티 돌면서 이 진실 set에 없는거 세면 된다
'''

# N, M = map(int,input().split())
# T, *t_arr = map(int,input().split())
#
# if T==0:
#     print(M)
# else:
#     t_set = set(t_arr)
#     p_arr = []
#
#     for _ in range(M):
#         _, *temp = map(int,input().split())
#         p_arr.append(set(temp))
#
#     # for i in range(M):
#     #     for p_num in p_arr:
#     #         if p_num & t_set:
#     #             t_set.update(p_num)
#     '''
#     개선 포인트 -> 어떤 루프에서 더이상 추가 되는 사람 없다면 돌 필요 없음
#     '''
#     while True:
#         pre = len(t_set)
#         for p in p_arr:
#             if p & t_set:
#                 t_set.update(p)
#
#         if pre == len(t_set):
#             break
#
#     cnt = 0
#     for p_num in p_arr:
#         if len(p_num & t_set) == 0:
#             cnt += 1
#
#     print(cnt)

'''
BFS 활용
사람들을 노드로, 같은 파티에 참석한 관계를 간선으로 생각하기
처음부터 진실을 아는 사람들을 시작점에 넣고 BFS
탐색하며 만나는 모든 사람을 진실을 아는 그룹에 추가

마지막에 파티 다시 돌면서 구성원 중 진실 아는 사람 없는 파티 카운트
'''

from collections import deque

def bfs():
    q = deque(t_arr)
    true_set = set(t_arr)

    while q:
        cur = q.popleft()
        for next_n in g[cur]:
            if next_n not in true_set:
                true_set.add(next_n)
                q.append(next_n)

    return true_set



N, M = map(int,input().split())
T, *t_arr = map(int,input().split())

if T==0:
    print(M)

else:
    p_arr = []
    g = [[] for _ in range(N+1)]

    for _ in range(M):
        p, *temp = map(int,input().split())
        p_arr.append(temp)

        for i in range(p):
            for j in range(p):
                if temp[i] == temp[j]:
                    continue
                g[temp[i]].append(temp[j])


    true_set = bfs()


    cnt = 0

    for party in p_arr:
        for p_num in party:
            if p_num in true_set:
                break
        else:
            cnt += 1

    print(cnt)