class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen=[]
        duplicates=[]
        k=0
        for i in range(len(nums)):
            if nums[i] in seen:
                duplicates.append(nums[i])
            else:
                seen.append(nums[i])
                nums[k]=nums[i]
                k+=1
        k=len(seen)
        return k