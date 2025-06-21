class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if(len(nums) not in nums):
            return len(nums)
        nums.sort()
        for i in range (len(nums)):
            if(i not in nums):
                return i
        