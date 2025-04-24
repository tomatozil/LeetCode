class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in dic:
                dic[sorted_str].append(s)
            else:
                dic[sorted_str] = [s]
        
        return [arr for k, arr in dic.items()]