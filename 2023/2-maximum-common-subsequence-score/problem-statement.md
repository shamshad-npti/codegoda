[Home](../README.md) | [Solution](./solution.py)

## Maximum Common Subsequence Score

<sup>Section: 2, Score: 19, Time limit per test: 30 seconds, Memory limit per test: 512MB, Input: stdin, Output: stdout</sup>

Mr. Tomyum loves to travel. He always books hotel rooms on Agoda while making any trip plans. Before booking a hotel room, Mr. Tomyum always checks hotel reviews first.

He wants to save time and only read reviews that are relevant to him and skip reviews that are similar. He noticed that reviews with his favorite words tend to be more relevant. So, he comes up with a list of favorite words, each with a score.

To find similarity of reviews, he calculates a score by looking at common subsequence of words and letters between 2 reviews. He calls this score, maximum common subsequence score (MCSS).  A MCSS is the highest total score of the subsequence of the letters and words.

Mr. Tomyum is busy planning his trip these days, please help him calculate MCSS for two reviews.

A subsequence of a given string is a sequence that can be derived from the given string by deleting some or no characters without changing the order of the remaining characters.

A common subsequence is the subsequence that exists in both review strings.

A word is a substring present in the review string without having space character.

Any letter missing in the favorite word list has a score of one and space should be ignored (i.e. it has a score of zero.)

### Input Format

The first line contains an integer $N$, denoting the number of favorite words.

Each of the next $N$ lines contain a lowercase English words $W$, followed by an integer score $S$, separated by space.

The next line contains first review string, ReviewString1

The next line contains second review string, ReviewString2

### Constraints

$0 \le N \le 50$

$2 \le S \le 10^5$

$1 \le \left|W\right| \le 5$

The input may contain duplicate words

$1 \le \left|ReviewString1\right| \times \left|ReviewString2\right| \le 10^6$

ReviewString1 and ReviewString2 will consist of lowercase English letters and spaces.

### Output Format

Print the maximum common subsequence score derived from ReviewString1 and ReviewString2

### Sample Input

```
4
nice 100
beach 2
good 200
z 10
nice hotel za is goooood
za was good and nice
```

### Sample Output

```
100
```

### Sample Input

```
4
pool 20
nice 1000
water 20000
hotel 10
hotela nice pool
hotelb nizzzce pool water is clean
```

### Sample Output

```
34
```

### Explanation

The highest-scoring common subsequence is 'hotelnicepool' with a total score of 34, comprising 10 points for 'hotel', 1 point each for 'n', 'i', and 'c', 1 point for 'e', and 20 points for 'pool'. It is worth noting that we cannot consider 'nice' as a word since it is not a substring present in both review strings. However, we can count 'hotel' as a word since it appears as a substring in both review strings.
