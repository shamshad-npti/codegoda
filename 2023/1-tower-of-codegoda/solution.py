"""
Approach: Greedy, Reverse Iteration
Time Complexity: O(N)
Space Complexity: O(1), O(N) for input
"""

def main():
    N = int(input())
    bosses = list(map(int, input().split()))
    subord = list(map(int, input().split()))
    mx, ans = 0, 0
    for i in range(N-1, -1, -1):
        if subord[i] >= mx:
            ans += 1
        mx = max(mx, bosses[i])
    return ans


if __name__ == "__main__":
    print(main())
