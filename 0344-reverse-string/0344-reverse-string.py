class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left_p = 0
        right_p = len(s)-1

        while left_p < right_p:
            s[left_p], s[right_p] = s[right_p], s[left_p]
            left_p += 1
            right_p -= 1
        