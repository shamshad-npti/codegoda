## Mr Agoji and bartender
<sup>Section: 1, Score: 12, Time limit per test: 30 seconds, Memory limit per test: 512MB, Input: stdin, Output: stdout</sup>

Our hiring manager, Mr. Agoji, went to a bar and met with a bartender. To his surprise, the bartender turned out to be a recently laid off software engineer. Mr. Agoji wants to help the bartender by giving him a job but first he wants to make sure if he is up to the mark or not. 

Mr. Agoji saw two queues with different types of glasses. Each glass is represented by a type_id. He gave the bartender a task to convert the first queue to the second queue. The queues are considered the same if the glass type is the same at corresponding positions in each queue. 

To do this, Mr. Agoji gave bartender $M$ pairs of swappable positions $(x, y)$ in the first queue. The bartender can only swap the position of glasses present at position $x$ and $y$ in the first queue any number of times. 

Help the bartender tell if he can convert the first queue to the second queue using these operations. 

### Input Format
The first line of input will contain an integer $T$, denoting the number of test cases. 

Each test case starts with two space-separated integers - $N$ denoting the number of glasses present in both queues and $M$ pairs of number $(x, y)$ given by Mr. Agoji. 

The next line contains $N$ space-separated integers denoting type_id’s for the first queue. 

The next line contains $N$ space-separated integers denoting type_id’s for the second queue. 

Each of the next $M$ lines contains two space-separated integers, $x$ and $y$, denoting the positions of swappable glasses in the first queue.

### Constraints
$1 \le T \le 10$

$2 \le N \le 10^5$

$0 \le M \le 10^5$

$1 \le type\text{\_}id_i \le 10^9$

$1 \le x \lt y \le N$

### Output Format
For each testcase, in a new line, print “YES” if the bartender can make the first queue the same as the second queue, otherwise print “NO” 

### Sample Input
```
2 
4 1 
1 3 2 4 
1 4 2 3
3 4
4 1
1 3 2 4
1 4 2 3
2 4
```
### Sample Output
```
NO
YES
```
### Explanation
For the first case, we can swap glasses at position 3 and 4. After swapping, the glass sequence will become (1 3 4 2) which is not same as the second queue sequence (1 4 2 3). 

For the second case, we can swap glasses at position 2 and 4. After swapping, the sequence becomes (1 4 2 3) which is same as the second queue sequence. 

### Sample Input
```
3
10 6
56 35 5 39 76 93 9 53 90 94
53 35 5 39 76 93 9 56 90 94
4 6
1 3
3 5
1 8
8 9
1 10
7 5
33 47 69 67 36 50 77
33 47 69 77 36 50 67
3 4
4 6
3 7
1 2
2 5
6 1
15 66 65 20 69 61
17 66 65 20 69 61
4 5
```
### Sample Output
```
YES
YES
NO
```
