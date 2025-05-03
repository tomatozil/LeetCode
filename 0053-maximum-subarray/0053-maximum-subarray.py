class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur, max_sum = nums[0], nums[0]

        for n in nums[1:]:
            cur = max(n, n + cur)
            max_sum = max(max_sum, cur)
        
        return max_sum