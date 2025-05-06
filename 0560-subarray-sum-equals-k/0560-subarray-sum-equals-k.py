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

# Time Limit 코드
        # prefix = [0] * (len(nums) + 1)

        # for i in range(len(nums)):
        #     prefix[i+1] = prefix[i] + nums[i]

        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums) + 1):
        #         if prefix[j] - prefix[i] == k:
        #             count += 1

        # return count