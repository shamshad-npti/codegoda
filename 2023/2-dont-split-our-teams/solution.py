"""
Approach: Sliding Window
Time Complexity: O(N*Q)
Space Complexity: O(N+Q), O(Q) for result, O(N) for input
"""


def main():
    N, _ = map(int, input().split())
    A = list(map(int, input().split()))
    result = []
    for q in map(int, input().split()):
        left, right, running_sum, count = 0, 0, 0, 0
        while right < N:
            running_sum += A[right]
            while running_sum > q:
                running_sum -= A[left]
                left += 1
            if running_sum == q:
                count += 1
            right += 1
        result.append(count)

    return result


if __name__ == '__main__':
    print(*main(), sep='\n')
