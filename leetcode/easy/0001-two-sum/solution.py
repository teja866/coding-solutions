class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        hm={}
        for i in range(n):
            compli=target-nums[i]
            if compli in hm:
                return [hm[compli],i]
            hm[nums[i]]=i
        