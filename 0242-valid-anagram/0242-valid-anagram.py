class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        s_list.sort()
        t_list.sort()

        if ''.join(s_list) == ''.join(t_list):
            return True
        return False
        