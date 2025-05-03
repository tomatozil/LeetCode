class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]

        right = [1] * len(nums)
        for i in range(len(nums)-1, 0, -1):
            right[i-1] = right[i] * nums[i]
        
        ret = [1] * len(nums)
        for i in range(len(nums)):
            ret[i] = left[i] * right[i]
        
        return ret