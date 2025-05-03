class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = set()
        left, right = 0, 0

        longest = 0
        while left <= right < len(s):
            if s[right] in subs:
                subs.remove(s[left])
                left += 1
            else:
                subs.add(s[right])
                longest = max(longest, right - left + 1)
                right += 1
        
        return longest