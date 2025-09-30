import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

'''
1620번 나는야 포켓몬 마스터 이다솜
'''

# 입력: 포켓몬 개수(N), 문제의 개수(M), 포켓몬 번호 배열, 문제 배열
# 출력: 알파벳 -> 포켓몬 번호, 포켓몬 번호 -> 알파벳

#  시간 초과 -> dict로 접근

n, m = map(int, input().split())
pokemon_num_dict = {}
pokemon_name_dict = {}

# 포켓몬 배열 받기
for i in range(n):
    name = input().strip()
    pokemon_num_dict[i+1] = name
    pokemon_name_dict[name] = i+1

# 문제
for i in range(m):
    q = input().strip()
    if q.isdigit():
        print(pokemon_num_dict.get(int(q)))
    else:
        print(pokemon_name_dict.get(q))

