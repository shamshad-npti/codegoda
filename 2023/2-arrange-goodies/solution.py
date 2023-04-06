"""
Approach: Greedy
Time Complexity: O(NlogN)
Space Complexity: O(N)
"""
from collections import defaultdict


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    counts = defaultdict(int)
    for a, b in zip(A, B):
        counts[a] += 1
        counts[b] -= 1

    values = []
    for k, v in counts.items():
        if v % 2:
            return -1
        values.extend([k] * (abs(v) // 2))

    min_element = min(A+B)
    values.sort()
    return sum(min(v, 2 * min_element) for v in values[:len(values) // 2])


if __name__ == "__main__":
    print(main())
