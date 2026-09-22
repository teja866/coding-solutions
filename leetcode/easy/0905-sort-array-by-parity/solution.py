class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n=len(nums)
        a=[]
        b=[]
        for i in range(n):
            if nums[i]%2==0:
                a.append(nums[i])
            else:
                b.append(nums[i])
        return a+b