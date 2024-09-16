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
    total_per_day_cost, total_cost_so_far, days_so_far, max_days, min_cost = 0, 0, 0, 0, float(
        'inf')
    for i, trips in enumerate(cities):
        trips.sort(key=lambda x: x[1])
        # Initially, we will stay at least 1 day to each city
        # add the lowest cost to stay at least 1 day to this city
        total_per_day_cost += trips[0][1]
        # we are considering this city. So, include it in the priority queue
        pq += [(trips[0][0], i, 1)]

    heapq.heapify(pq)

    while pq:
        days, city, trip = pq[0]
        # According to the min heap, the 'days' will be the smallest available days from the heap
        remaining_days = days - days_so_far
        # we can take the remaining days from all other cities
        # multiply with the per day cost summation of each city
        total_cost_so_far += remaining_days * total_per_day_cost
        days_so_far = days
        # if this is the last trip of this city:
        if trip == len(cities[city]):
            # remaining elements in pq can add at least 1 day.
            # So, len(pq) cities can add 1*len(pq) days
            total_days = days_so_far * len(pq)
            if total_days >= max_days:
                if total_days == max_days:
                    min_cost = min(min_cost, total_cost_so_far)
                else:
                    min_cost = total_cost_so_far

                max_days = total_days

            heapq.heappop(pq)
            # as this city is popped from the pq, subtract all of its costs from total_cost
            total_cost_so_far -= sum([d * c for d, c in cities[city]])
        else:
            # we can include more days for this city
            days += cities[city][trip][0]
            heapq.heapreplace(pq, (days, city, trip + 1))

        current_trip_cost, next_trip_cost = cities[city][trip - 1][1], cities[city][trip][1] if trip < len(
            cities[city]) else 0
        # update the total_per_day_cost: remove the cost we considered(this_trip)
        # and add the next trip cost we will consider
        total_per_day_cost += next_trip_cost - current_trip_cost

    return max_days, min_cost


if __name__ == '__main__':
    max_days, min_cost = main()
    print(f"{max_days} {min_cost}")
