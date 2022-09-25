class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r = nums[0]
        for i in range(1,len(nums)):
            r = r ^ nums[i]
        return r
