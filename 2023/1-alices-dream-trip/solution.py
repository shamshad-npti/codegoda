"""
Approach: Dynamic Programming
Time Complexity: O(N)
Space Complexity: O(1), O(N) for input
"""

def main():
    N = int(input())
    rates = [int(input()) for _ in range(N)]
    prev, cur, = 0, rates[0]
    for i in range(1, N):
        prev, cur = cur, max(prev + rates[i], cur)
    print(cur)


if __name__ == '__main__':
    main()
