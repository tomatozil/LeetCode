class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        count = 0
        prefix_history = {0:1}

        for n in nums:
            cur_sum += n
            if (cur_sum - k) in prefix_history:
                count += prefix_history[cur_sum - k]
            if cur_sum in prefix_history:
                prefix_history[cur_sum] += 1
            else:
                prefix_history[cur_sum] = 1

        return count
