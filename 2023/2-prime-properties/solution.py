"""
Approach: Ad-hoc, Math, Prime Numbers
Time Complexity: O(sqrt(X+Y))
Space Complexity: O(1)
"""


def is_prime(num):
    if num <= 2 or num % 2 == 0:
        return num == 2

    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2

    return True


def solve(A, B):
    if is_prime(abs(A-B)):
        return f"{A} {B}"

    S, L = min(A, B), max(A, B)

    if S == 3 and L == 7:
        return f"{A} 5 {B}"

    if S == 2:
        if is_prime(L+2):
            return f"{A} {L+2} {B}"
        elif is_prime(L-2):
            return f"{A} {L-2} {B}"
    else:
        S1, S2 = solve(A, 2), solve(2, B)
        if S1 and S2:
            return f"{S1} {S2[2:]}"

    return False


if __name__ == "__main__":
    A, B = map(int, input().split())

    print(solve(A, B) or "Sorry Ms. Agoji!")
