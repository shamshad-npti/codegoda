import heapq

def main():
    M, N = map(int, input().split())
    dag = [[] for _ in range(M)]

    for _ in range(N):
        u, v = map(int, input().split())
        dag[v-1] += [u-1]
    
    outdeg = [0] * M
    for u in range(M):
        for v in dag[u]:
            outdeg[v] += 1

    pq = []

    for u in range(M):
        if outdeg[u] == 0:
            heapq.heappush(pq, -u)

    done = []
    while pq:
        u = -heapq.heappop(pq)
        done += [u+1]
        for v in dag[u]:
            outdeg[v] -= 1
            if outdeg[v] == 0:
                heapq.heappush(pq, -v)
    print (*done if len(done) == M else [-1])

if __name__ == '__main__':
    main()
