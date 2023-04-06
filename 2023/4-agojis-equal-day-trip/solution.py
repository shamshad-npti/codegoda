"""
Approach: Merging K Sorted Lists
Time Complexity: O(N * log(N))
Space Complexity: O(N)

Note: Another approach is to first determine the maximum number of days, and then identify the 
minimum cost among all the indices that have the maximum number of days.
"""


from collections import defaultdict
import heapq


def main():
    N = int(input())
    cities = defaultdict(list)
    for _ in range(N):
        city, days, cost = input().split()
        days, cost = int(days), int(cost)
        cities[city].append((days, cost))

    cities = list(cities.values())
    pq = []
    curr_cost, total_cost, num_days, max_days, min_cost = 0, 0, 0, 0, float(
        'inf')
    for i, trips in enumerate(cities):
        trips.sort(key=lambda x: x[1])
        curr_cost += trips[0][1]
        pq += [(trips[0][0], i, 1)]
    heapq.heapify(pq)
    while pq:
        days, city, trip = pq[0]
        total_cost += (days-num_days)*curr_cost
        cost1, cost2 = cities[city][trip -
                                    1][1], cities[city][trip][1] if trip < len(cities[city]) else 0
        curr_cost += cost2 - cost1
        num_days = days
        if trip == len(cities[city]):
            nmax_days = num_days * len(pq)
            if nmax_days >= max_days:
                if nmax_days == max_days:
                    min_cost = min(min_cost, total_cost)
                else:
                    min_cost = total_cost
                max_days = nmax_days
            heapq.heappop(pq)
            total_cost -= sum([d*c for d, c in cities[city]])
        else:
            days += cities[city][trip][0]
            heapq.heapreplace(pq, (days, city, trip+1))

    return max_days, min_cost


if __name__ == '__main__':
    max_days, min_cost = main()
    print(f"{max_days} {min_cost}")
