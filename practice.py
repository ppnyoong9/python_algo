
T = int(input())

for tc in range(1,T+1):
    data = input()
    ans = 0
    temp = 0

    for c in data:
        if c == 'O':
            temp+=1
        else :
            temp = 0

        ans += temp

    print(ans)