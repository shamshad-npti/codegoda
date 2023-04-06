"""
Approach: Ad-hoc
Time Complexity: O(sqrt(Y) + N)
Space Complexity: O(sqrt(Y) + N)
"""

def main():
    Y, N = map(int, input().split())
    islands = list(map(int, input().split()))

    factors = []

    prime = 3
    while prime * prime <= Y:
        while Y % prime == 0:
            factors.append(prime)
            Y //= prime
        prime += 2

    if Y > 1:
        factors.append(Y)

    subset_sum = set([0])

    for factor in factors:
        subset_sum |= {factor + x for x in subset_sum}

    return [i + 1 for i in range(N) if islands[i] in subset_sum]


if __name__ == '__main__':
    result = main()
    print(len(result))
    if result:
        print(*result)
