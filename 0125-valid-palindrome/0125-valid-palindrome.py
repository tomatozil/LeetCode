class Solution:
    def isPalindrome(self, s: str) -> bool:
        origin_s = ''
        opposite_s = ''

        for c in s:
            if c.isalnum():
                c_lower = c.lower()
                origin_s = origin_s + c_lower
                opposite_s = c_lower + opposite_s
        
        return origin_s == opposite_s