# 문제: 합승 택시 요금
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/72413

# [성능 요약] 메모리: 17.5 MB 시간: 29.46 ms

'''
정확성: 50.0
효율성: 50.0
합계: 100.0 / 100.0
'''

# n = 지점개수, s = 출발지점, a = A의 도착지점, b = B의 도착지점, fares= 택시요금
# 시작점에 각 정점까지 가는거 구해보고..? 그 정점에서 다시 A와 B를 가보기
import heapq
def solution(n, s, a, b, fares):

    def dijkstra(start):
        INF = 100000 * n-1 + 1
        pq = [(0,start)]
        dist = [INF] * (n+1)
        dist[start] = 0

        while pq:
            w, node = heapq.heappop(pq)

            if dist[node] < w:
                continue

            for next_w, next_n in g[node]:
                new_w = next_w + w

                if dist[next_n] <= new_w:
                    continue

                dist[next_n] = new_w
                heapq.heappush(pq,(new_w,next_n))

        return dist


    # 간선 정보 받기
    g = [[] for _ in range(n+1)]
    for u,v,w in fares:
        g[u].append([w,v])
        g[v].append([w,u])

    s_dist = dijkstra(s)
    a_dist = dijkstra(a)
    b_dist = dijkstra(b)

    answer = a_dist[s] + b_dist[s]
    for i in range(1, n+1):
        if i == s:
            continue
        answer = min(answer, s_dist[i]+a_dist[i]+b_dist[i])

    return answer



print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))