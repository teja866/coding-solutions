class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n&(1<<k) or n==1 or n<k:
            return "0"
        else:
            return "1"