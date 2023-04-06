"""
Approach: DP
Time Complexity: O(N^3 + ND * (N + D))
Space Complexity: O(N^2 + ND)
"""


from itertools import accumulate


def floyd_warshall(arr, N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])


def main():
    N, D, M = map(int, input().split())
    prices = [list(map(int, input().split())) for _ in range(N)]
    prices = [[0] + list(accumulate(p)) for p in prices]
    travel_cost = [[float('inf')] * N for _ in range(N)]
    for i in range(N):
        travel_cost[i][i] = 0
    for _ in range(M):
        u, v, w = map(int, input().split())
        u, v = u - 1, v - 1
        w = min(w, travel_cost[u][v])
        travel_cost[u][v], travel_cost[v][u] = w, w

    discounts = [0] * N
    P = int(input())
    for _ in range(P):
        q, x, y = map(int, input().split())
        discounts[q-1] = (x, y)

    def calc_price(hotel, start_day, end_day):
        price = prices[hotel][end_day]-prices[hotel][start_day]
        if discounts[hotel] and discounts[hotel][0] <= end_day - start_day:
            price -= (price*discounts[hotel][1]+99)//100
        return price

    K = int(input())
    agoda_cash = [[0] * D for _ in range(N)]
    for _ in range(K):
        R, S, T = map(int, input().split())
        agoda_cash[R-1][S-1] = T

    dp1 = [[(float('-inf'), float('-inf'))] * (D+1) for _ in range(N)]
    dp2 = [[(float('-inf'), float('-inf'))] * (D+1) for _ in range(N)]
    for i in range(N):
        dp2[i][0] = (0, 0)

    floyd_warshall(travel_cost, N)

    def combine(plan1, plan2):
        return (plan1[0]+plan2[0], plan1[1]+plan2[1])

    for day in range(0, D):
        for i in range(N):
            ag_cash = 0
            for j in range(day, D):
                ag_cash += agoda_cash[i][j]
                dp1[i][j] = max(dp1[i][j], combine(dp2[i][day], (ag_cash, -calc_price(i, day, j+1))))

        for i in range(N):
            for j in range(N):
                if i != j and travel_cost[i][j] != float('inf'):
                    dp2[j][day+1] = max(dp2[j][day+1], combine(dp1[i][day], (0, -travel_cost[i][j])))

    best = max(dp1[i][D-1] for i in range(N))
    return (best[0], -best[1])


if __name__ == "__main__":
    print(*main())
