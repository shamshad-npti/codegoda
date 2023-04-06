"""
Approach: Matrix Exponentiation, DP, Modular Arithmetic, Probability
Time Complexity: O(K^3 * log(N))
Space Complexity: O(K^2)
"""


MOD = 10**9 + 7


def create_frac(num, den):
    return num*pow(den, MOD-2, MOD) % MOD


def matrix_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    C = [[0 for _ in range(p)] for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k]*B[k][j]
            C[i][j] %= MOD
    return C


def matrix_pow(A, n):
    """
    calculate A^n
    """
    res = [[1 if i == j else 0 for j in range(len(A))] for i in range(len(A))]
    while n:
        if n & 1:
            res = matrix_mul(res, A)
        A = matrix_mul(A, A)
        n >>= 1
    return res


def main():
    K, N = map(int, input().split())
    R = list(map(int, input().split()))
    transition_matrix = [[create_frac(0, 1)
                          for _ in range(K+1)] for _ in range(K+1)]
    for i in range(K):
        transition_matrix[i][0] = create_frac(R[i]-1, R[i])
        transition_matrix[i][i+1] = create_frac(1, R[i])
    transition_matrix[K][K] = create_frac(1, 1)
    transition_matrix = matrix_pow(transition_matrix, N)
    initial_state = [create_frac(1 if k == 0 else 0, 1) for k in range(K+1)]
    final_state = matrix_mul([initial_state], transition_matrix)[0]
    print(final_state[-1])


if __name__ == "__main__":
    main()
