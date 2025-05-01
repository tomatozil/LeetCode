class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = 0
        for i in range(k):
            cur_sum += nums[i]
        
        max_sum = cur_sum

        left = 1
        right = left + k - 1
        while right < len(nums):
            cur_sum -= nums[left-1]
            cur_sum += nums[right]

            max_sum = max(max_sum, cur_sum)

            left, right = left+1, right+1

        return round(max_sum / k, 5)
        
