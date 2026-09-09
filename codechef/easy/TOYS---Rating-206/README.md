# TOYS - Rating 206

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Playing with Toys

Chef got $N$ toys for his birthday. Everyday, if he has at least one toy with him, he plays with one specific toy for that day.

Unfortunately, Chef is very careless, and will inevitably break that toy by the end of the day. When he does break it, he does not play with a new toy but just waits for the next day.

After $M$ days, how many toys will Chef be left with?

### Input Format
- The first and only line of each test case contains $2$ integers - $N$ and $M$.
### Output Format

Output the number of toys left with Chef after $M$ days

### Constraints
- $1 \le N, M \le 10$
### Sample 1:
Input
Output

```
1 2

```

```
0
```

### Explanation:

Chef had $1$ toy only, and he broke it on day $1$. On day $2$ he had nothing to play with. He is left with $0$ toys after day $2$.

### Sample 2:
Input
Output

```
5 3

```

```
2

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-09T11:13:48.989Z  

```py
# cook your dish here
n,m=map(int,input().split())
if n-m<0:
    toys=0
else:
    toys=n-m
print(toys)
```

---

[View on CodeChef](https://www.codechef.com/problems/TOYS)