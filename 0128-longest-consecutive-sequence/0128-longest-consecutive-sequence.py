class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for n in s:
            if n - 1 not in s:
                count = 1
                next_num = n + 1
                while next_num in s:
                    count += 1
                    next_num += 1
                longest = max(longest, count)
        
        return longest
