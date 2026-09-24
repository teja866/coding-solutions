# ICECONE - Rating 226

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Icecream and Cone

Chef has $X$ cones and $Y$ scoops of ice cream. Each ice cream cone requires exactly one cone and one scoop of ice cream.

Your task is to determine the  **maximum**  number of ice cream cones Chef can make with the available ingredients.

### Input Format
- Input will contain two integers $X$ and $Y$ - the number of cones and ice cream scoops, respectively.
### Output Format

Output the maximum number of ice cream cones Chef can make.

### Constraints
- $1 \leq X \leq 100$
- $1 \leq Y \leq 100$
### Sample 1:
Input
Output

```
10 5

```

```
5
```

### Explanation:

Chef has 10 cones and 5 scoops of ice cream. Chef can make a maximum of 5 ice cream cones.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-24T04:43:32.685Z  

```py
# cook your dish here
x,y=map(int,input().split())
print(min(x,y))
```

---

[View on CodeChef](https://www.codechef.com/problems/ICECONE)