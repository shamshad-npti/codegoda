"""
Approach: Dynamic Programming, Combinatorics, Heap, Implementation
R = result size = 10
Time Complexity: O(N * 2^K + M * 2^L * R)
Space Complexity: O(N * 2^K)
"""


import heapq


class HotelScore(object):
    def __init__(self, hid, score):
        self.hid = hid
        self.score = score
        self.__key = (score, -hid)

    def __lt__(self, other):
        return self.__key < other.__key


def keyword_comb(keywords):
    keywords = list(sorted(keywords))
    comb = [((), 0)]
    for keyword, score in keywords:
        comb += [(c + (keyword,), s + score) for c, s in comb]
    return comb[1:]


def search_comb(search_queries):
    search_queries = list(sorted(search_queries))
    comb = [()]
    for query in search_queries:
        comb += [c + (query,) for c in comb]
    return comb[1:]


def main():
    N, M = map(int, input().split())
    dp = {}
    for _ in range(N):
        line = input().split()
        hid = int(line[0])
        keywords = line[2::2]
        scores = list(map(int, line[3::2]))
        for comb, score in keyword_comb(zip(keywords, scores)):
            if comb not in dp:
                dp[comb] = []
            hotels = dp[comb]
            heapq.heappush(hotels, HotelScore(hid, score))
            if len(hotels) > 10:
                heapq.heappop(hotels)

    for _ in range(M):
        line = input().split()
        query = line[1:]
        hotels = {}
        for comb in search_comb(query):
            for hotel in dp.get(comb, []):
                hotels[hotel.hid] = max(hotels.get(hotel.hid, 0), hotel.score)

        hotels = [(-score, hid) for hid, score in hotels.items()]
        hotels.sort()
        hotels = [hid for _, hid in hotels[:10]]
        if len(hotels) == 0:
            print(-1)
        else:
            print(' '.join(map(str, hotels)))


if __name__ == "__main__":
    main()
