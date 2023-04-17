[Home](../README.md) | [Solution](./solution.py)

## Search Result Ranking

<sup>Section: 4, Score: 50, Time limit per test: 30 seconds, Memory limit per test: 512MB, Input: stdin, Output: stdout</sup>

Agoda has millions of hotels listed on its website. Each hotel has an id, a name, a location, and information about the type of accommodation it offers. To advertise these hotels on Elgo, Agoda has built a list of keywords that are relevant to each hotel. For example, the keywords for the hotel "The Grand Hotel" might be "luxury", "spa", "beach", "grand", "hotel", "resort" etc. Each keyword is associated with a score. The score is a positive integer that indicates how relevant the keyword is to the hotel. For example, the keyword "grand" might have a score of 100, while the keyword "hotel" might have a score of 10. The score of a keyword is independent of the other keywords. It should be noted that the keywords are not unique, and a keyword can have different scores for different hotels.

Elgo is a search engine that allows users to search for hotels by search queries. A search query is a string of words. The search results are ranked by the relevance of the hotels to the search query. The relevance of a hotel to a search query is the sum of the scores of the keywords relevant to the hotel, i.e., the keywords present in the search query. For example, if we have hotel with id 1 and the keywords "grand" and "hotel" with scores 100 and 10 respectively, then the relevance of the hotel to the search query "grand hotel", "luxury hotel bangkok" and "spa in bangkok" is 110, 10 and 0 (irrelevant) respectively.

Elgo has a limit on the number of hotels that can be displayed in the search results. If the number of hotels that are relevant to the keywords exceeds the limit, Elgo will only display the hotels with the highest relevance sorted in descending order of relevance. If there are multiple hotels with the same relevance, then the hotels with the lowest id will be displayed first.

Given lists of hotels, their keywords, and search queries print a list of recommended hotels for each query.

### Input Format

The first line contains two space-separated integers $N$ and $M$, where $N$ is the number of hotels and $M$ is the number of search queries.

The next $N$ lines starts with two space-separated integers $H$ and $K$, where $H$ is the id of the hotel and $K$ is the number of keywords associated with the hotel. It is followed by $K$ space-separated keyword-score pairs, where each keyword-score pair consists of a keyword and a score separated by a space. The keyword is a string of lowercase English letters. The score is a positive integer

The next $M$ lines start with an integer $L$, representing the number of words in search query, followed by $L$ space-separated words. Each word is a string of lowercase English letters.

### Constraints

$1 \le N \le 3\times 10^4$

$1 \le M \le 3\times 10^4$

$1 \le H \le 10^5$

$1 \le K, L \le 6$

$1 \le \left|word\right| \le 10$

$1 \le score \le 10^5$

All hotel ids are unique

Keywords for each hotel are unique

### Output Format

For each search query, print the hotel ids displayed in the search results. The ids must be printed in the order they appear in the search results. If there are no hotels that are relevant to the search query, print -1. If there are more than 10 hotels that are relevant to the search query, print only the first 10 hotels.

### Sample Input

```
3 2
101 3 grand 100 hotel 10 center 5
201 3 luxury 100 bangkok 10 hotel 1
301 2 goa 50 resort 50
2 grand hotel
1 goa
```

### Sample Output

```
101 201
301
```

### Explanation

For search query "grand hotel", the relevance of hotel with id 101, 201, and 301 are 110, 10, and 0, respectively. Since the first two hotels are relevant to the search query, they are displayed in the search results. The relevance of hotel with id 301 is 0, so it is not displayed in the search results.

For search query "goa", the relevance of hotel with id 101, 201, and 301 are 0, 0, and 50, respectively. Since only the third hotel is relevant to the search query, it is displayed in the search results.

### Sample Input

```
5 5
10 3 delhi 100 holiday 5 hotel 50
11 3 delhi 100 business 6 hotel 30
12 3 spa 100 luxury 20 hotel 5
14 3 delhi 100 luxury 9 hotel 10
15 3 london 500 luxury 8 hotel 30
3 luxury business hotel
3 cheap hotel london
3 delhi luxury hotel
4 vry qiravx heqpc deu
2 business holiday
```

### Sample Output

```
10 15 11 12 14
15 10 11 14 12
10 11 14 15 12
-1
11 10
```
