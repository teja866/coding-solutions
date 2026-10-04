class Solution:
    def minRotations(self, s: str) -> int:
        total=0
        curr=0
        for ch in s:
            next_digit = int(ch)   
            distance = abs(curr - next_digit)
            total += min(distance, 10 - distance)
            curr = next_digit
        return total