[Home](../README.md) | [Solution](./solution.py)

## Algoji's Secret Trip Plan to Cyclades
<sup>Section: 2, Score: 19, Time limit per test: 30 seconds, Memory limit per test: 512MB, Input: stdin, Output: stdout</sup>

Mr. Algoji is planning his anniversary trip to the Cyclades Islands on Agoda. To keep this a surprise for Mrs. Algoji, Mr. Algoji has decided to write down his notes in code. He chooses a secret odd number, $Y$, and writes a list of $N$ discrete integers for each island indicating island’s distinctiveness. It is now time for him to narrow down which islands he wants to visit. Mr. Algoji loves prime numbers and decides that he only wants to visit islands with distinctiveness score which are primourite numbers to $Y$. 

A number is primourite to $Y$ if it can be made by summing up any non-empty subset of the prime factorization set of $Y$.  

For instance, if $Y$ is $4125$, the prime factorization set of $Y$ is $3, 5, 5, 5, 11 (3 \times 5 \times 5 \times 5 \times 11 = 4125)$. Mr. Algoji decides to visit an island with a distinctiveness score, $8$, because $8 = 3+5$. However, he decides to not visit an island with a distinctiveness score, $6$, because there is no subset of the prime factorization of $Y$ that sums to $6$. 

Can you help Mr. Algoji to decide on a list of islands he will visit during his trip?

### Input Format
The first line of the input contains two space-separated integers, the secret odd number $Y$, and the number of the Cyclades islands $N$.  

Next line contains $N$ space-separated integers, the distinctiveness of the islands. 

### Constraints
$1 \le N \le 10^6$

$3 \le Y \lt 3\times10^{11}$

$Y$ is odd

$3 \le distinctiveness_i \lt 3\times10^{11}$

### Output Format
The first line of the output contains the number of islands that he will visit. The second line contains the indices of those islands sorted in ascending order. 

### Sample Input
```
4125 8
12 14 5 12 8 3 20 8
```
### Sample Output
```
5
2 3 5 6 8
```
### Explanation
For the sample test case  

$Y = 4125$,

the prime factorization set for Y is $3, 5, 5, 5, 11 (3 \times 5 \times 5 \times 5 \times 11 = 4125)$.

$N = 8$,

`distinctiveness= [12, 14, 5, 12, 8, 3, 20, 8]`

In the given distinctiveness list, the primourite numbers to $Y = 4125$ are $14, 5, 8, 3, 8$. So, Mr. Algoji will visit islands with indices = $2, 3, 5, 6, 8$. 
### Sample Input
```
15 5
3 4 5 8 10
```
### Sample Output
```
3
1 3 4
```