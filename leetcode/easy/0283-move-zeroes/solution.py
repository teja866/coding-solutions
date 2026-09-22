class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        nonzero=0
        for i in range(n):
            if nums[i]!=0:
                nums[nonzero]=nums[i]
                nonzero+=1
        for i in range(nonzero,n):
            nums[i]=0