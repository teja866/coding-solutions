class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        arr=[]
        for i in range(n):
            if nums[i]!=val:
                arr.append(nums[i])
        nums[:]=arr
        return len(arr)
