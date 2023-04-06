"""
Approach: Backtracking, Bitmasking, Memoization, Exhaustive Search
Time Complexity: O(N*2^N)
Space Complexity: O(2^N)
"""


def backtrack(N, current_value, used, store):
    if current_value <= 0:
        return False

    if used in store:
        return store[used]

    for i in range(N):
        if used & (1 << i) == 0:
            if not backtrack(N, current_value - i - 1, used | (1 << i), store):
                store[used] = True
                return True
    store[used] = False
    return False


def main():
    T = int(input())
    for _ in range(T):
        N, S = map(int, input().split())
        print(["NO", "YES"][not S or (N * (N + 1) //
              2 >= S and backtrack(N, S, 0, {}))])


if __name__ == "__main__":
    main()
