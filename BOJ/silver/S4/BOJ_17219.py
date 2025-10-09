import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline

'''
17219번 비밀번호 찾기
'''

# 입력: 저장된 사이트 주소의 수(N), 비밀번호를 찾으려는 사이트 주소의 수(M), N개의 사이트주소와 비밀번호, M개의 비밀번호를 찾으려는 사이트 주소
# 출력: 비밀번호를 찾으려는 사이트 주소의 비밀번호

n, m = map(int,input().split())

site_pwd_dict = {}

for _ in range(n):
    site, pwd = input().split()
    site_pwd_dict[site] = pwd

for _ in range(m):
    print(site_pwd_dict[input().strip()])

