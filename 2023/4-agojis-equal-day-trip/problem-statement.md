[Home](../README.md) | [Solution](./solution.py)

## Agoji's Equal-Day Trip

<sup>Section: 4, Score: 50, Time limit per test: 30 seconds, Memory limit per test: 512MB, Input: stdin, Output: stdout</sup>

Agoji is a traveler who loves to explore new cities. He has planned a trip to visit different cities around the world. Agoji has received N offers for different cities for his trip each offer contains the city name, the maximum number of days in the city, and the price per day. With each offer, he can choose to stay for any number of days between 0 and max number of days. His goal is to maximize the total stay while minimizing the total cost. The number of days he stays per city must be equal as he does not want to visit some cities more than others. It’s not required for him to visit all cities available.

Can you help him find the best deals for his trip?

### Input Format

The first line of the input is an integer, $N$, which represents the number of offers.

Following that, there are $N$ lines, each consisting of three values separated by spaces. The first value is a string, city_name, representing the name of a city. The second value is an integer, max_num_days, indicating the maximum number of days a traveler can stay in that city. The third value is an integer, cost_per_day, representing the daily cost of staying in the city.

### Constraints

$1 \le N \le 10^5$

$1 \le \left|city\\_name\right| \le 20$

city_name is a string consisting of English letters, 

$1 \le max\\_num\\_days \le 10^5$

$1 \le cost\\_per\\_day \le 10^5$

### Output Format

Print two value - maximum number of days and minimum cost

### Sample Input

```
5
Nyc 4 100
Bangkok 3 10
Nyc 2 15
Warsaw 1 12
Paris 3 80
```

### Sample Output

```
9 400
```

### Explanation

An optimal solution is to choose offers 1, 2, 3, and 5, allowing Mr. Agoji to spend three days each in New York City, Bangkok, and Paris for a total of nine days. This approach satisfies all the problem constraints and minimizes the cost of the entire trip, which comes out to be 400. 

### Sample Input

```
8
London 2 100
Delhi 1 50
Paris 3 200
Rome 2 100
London 1 40
Paris 1 80
Bangkok 5 170
Delhi 3 75
```

### Sample Output

```
12 1430
```
