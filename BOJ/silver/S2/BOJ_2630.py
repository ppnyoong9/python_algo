import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

'''
2630. 색종이 만들기
'''

#  입력: 종이 한 변의 길이(N), 정사각형칸의 색 배열
#  출력: 잘라진 하얀색 종이와 파란색 종이의 개수

# N/2 로 계속 쪼개지니까
# 전체가 같은 색인지 확인하고 엇 같은색 아님 하면 그때 쪼개기
# 쪼개는건 무조건 4등분이니까 ( 좌상, 좌하, 우상, 우하 ) 쪼개지는 곳의 시작점을 기준으로 또 같은색 인지 확인해가기

def f(si, sj, n):
    global w
    global b
    for i in range(si,si+n):
        for j in range(sj,sj+n):
            if arr[si][sj] != arr[i][j]:
                c = int(n/2)
                # 4등분
                f(si,sj,c)              # 왼쪽 위
                f(si,sj+c, c)           # 오른쪽 위
                f(si+c,sj,c)            # 왼쪽 아래
                f(si+c, sj+c, c)        # 오른쪽 아레
                return
    else:
        if arr[si][sj] == 0:
            w += 1
        else:
            b += 1


n = int(input())
arr =  [list(map(int,input().split())) for _ in range(n)]

w = 0
b = 0
f(0,0,n)


print(w)
print(b)