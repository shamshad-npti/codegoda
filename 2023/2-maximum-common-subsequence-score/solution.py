"""
Approach: Dynamic Programming
R1 = lenght(ReviewString1)
R2 = lenght(ReviewString1)
Time Complexity: O(N+R1*R2)
Space Complexity: O(N+R1*R2)
"""

def main():
    N = int(input())
    word_score = {}
    for _ in range(N):
        word, score = input().split()
        word_score[word] = max(word_score.get(word, 0), int(score))
    review_score1 = input()
    review_score2 = input()
    n, m = len(review_score1), len(review_score2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
            for k in range(min(i+1, j+1, 5)):
                s1 = review_score1[i-k:i+1]
                s2 = review_score2[j-k:j+1]
                if s1 == s2:
                    score = word_score.get(s1, len(s1)-s1.count(' '))
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1],
                                           dp[i - k][j - k] + score)
    return dp[n][m]


if __name__ == '__main__':
    print(main())
