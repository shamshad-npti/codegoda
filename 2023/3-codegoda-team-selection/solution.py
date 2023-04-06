"""
Approach: Combinatorics
Time Complexity: O(T * (X + K) * (log(M) + log(N)))
Space Complexity: O(X + K)
"""

MOD = 10 ** 9 + 7
MAX = int(2e5)+5
fact = [1] * MAX
for i in range(1, MAX):
    fact[i] = (fact[i-1] * i) % MOD

ifact = [1] * MAX
ifact[MAX-1] = pow(fact[MAX-1], MOD-2, MOD)
for i in range(MAX-2, -1, -1):
    ifact[i] = (ifact[i+1] * (i+1)) % MOD


def ncr(n, r):
    return (fact[n] * ifact[r] * ifact[n-r]) % MOD


def main():
    M, N, X, K = map(int, input().split())
    return ncr(X, K) * pow(K, M, MOD) * sum(pow(-1, i) * pow(K-i, N, MOD) * ncr(K, i) for i in range(K+1)) % MOD % MOD


if __name__ == '__main__':
    print('\n'.join([str(main()) for _ in range(int(input()))]))
