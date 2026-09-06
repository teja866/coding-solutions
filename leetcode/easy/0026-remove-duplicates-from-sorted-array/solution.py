class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen=[]
        duplicates=[]
        for i in range(len(nums)):
            if nums[i] in seen:
                duplicates.append(nums[i])
            else:
                seen.append(nums[i])
        nums[:]=seen      
        return len(seen)