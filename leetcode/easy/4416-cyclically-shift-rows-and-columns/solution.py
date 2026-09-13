class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        for i in range(n):
            k=rowShift[i]
            new_row=[0]*n
            for j in range(n):
                new_row[(j-k+n)%n]=grid[i][j]
            grid[i]=new_row

        for j in range(n):
            k=colShift[j]
            new_col=[0]*n
            for i in range(n):
                new_col[(i-k+n)%n]=grid[i][j]
            for i in range(n):
                grid[i][j]=new_col[i]

        return grid