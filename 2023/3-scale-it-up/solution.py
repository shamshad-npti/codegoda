"""
Approach: Dijkstra's Algorithm, Sorting, Greedy, Two Pointers,
Time Complexity: O(N * log(N) + M * log(N) + Q * log(Q))
Space Complexity: O(N + M + Q)
"""

import heapq


def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u-1] += [(v-1, w)]
        graph[v-1] += [(u-1, w)]

    dist = [float("inf")] * N
    dist[0] = 0
    pq = [(0, 0)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    warmup_time = map(int, input().split())
    throughput = map(int, input().split())
    total_time = [w + d for w, d in zip(warmup_time, dist)]
    time_to_serve = list(sorted(zip(total_time, throughput)))
    for i in range(1, N):
        time_to_serve[i] = (time_to_serve[i][0],
                            time_to_serve[i][1] + time_to_serve[i-1][1])
    Q = int(input())
    queries = [(int(input()), i) for i in range(Q)]
    result = [-1] * Q
    queries.sort()
    i, j = 0, 0
    while i < Q and j < N:
        q, index = queries[i]
        if q <= time_to_serve[j][1]:
            result[index] = time_to_serve[j][0]
            i += 1
        else:
            j += 1

    print("\n".join(map(str, result)))


if __name__ == "__main__":
    main()
