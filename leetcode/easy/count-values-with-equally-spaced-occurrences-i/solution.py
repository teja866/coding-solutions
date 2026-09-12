class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        n=len(nums)
        special=set()
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]==nums[j]==nums[k]:
                        if j-i==k-j:
                            special.add(nums[i])
        return len(special)