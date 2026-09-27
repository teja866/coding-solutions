class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans=[]
        while nums:
            distinct=sorted(set(nums))

            for val in distinct:
                nums.remove(val)
            ans.extend(distinct)
        return ans