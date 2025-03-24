class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [char.lower() for char in s if char.isalnum()]
        l, r = 0, len(s_list)-1

        while l < r:
            if s_list[l] != s_list[r]:
                return False
            l += 1
            r -= 1
        return True
