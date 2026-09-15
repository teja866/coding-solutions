# MAX6 - Rating 216

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Max Sixers

Your favourite cricket player played very well today. He made $X (100 \le X \le 200)$ runs from exactly $100$ balls. Each ball he scored either $0$, $1$, $2$, $3$, $4$ or $6$ runs.

Unfortunately you missed the match. So now, you are wondering what is the maximum number of sixers he could have hit? A sixer is a ball where you score $6$ runs.

### Input Format
- The first and only line of input contains $X$, the total number of runs scored.
### Output Format

For each test case, output on a new line the maximum number of $6$s.

### Constraints
- $100 \le X \le 200$
### Sample 1:
Input
Output

```
100

```

```
16

```

### Explanation:

The player could have scored $6$s on $16$ balls, $4$ on $1$ ball and then $0$ on the remaining $83$ balls.

### Sample 2:
Input
Output

```
150

```

```
25

```

### Explanation:

The player could have scored $6$ on $25$ balls, and then $0$ on $75$ balls.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T04:00:20.975Z  

```py
# cook your dish here
x=int(input())
count=0
for i in range(1,x+1):
    if i%6==0:
        count+=1
print(count)
```

---

[View on CodeChef](https://www.codechef.com/problems/MAX6)