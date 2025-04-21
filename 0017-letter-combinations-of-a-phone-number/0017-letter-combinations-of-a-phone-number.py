class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 
        6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        characters = [] # ["def", "ghi"]
        for c in digits:
            characters.append(phone[int(c)])
        
        if not characters:
            return []
         
        result = []
        m = len(digits)
        def comb(level, tmp):
            if level == m:
                result.append(tmp)
                return
            
            for c in characters[level]:
                tmp += c
                comb(level+1, tmp)
                tmp = tmp[:-1]
        
        comb(0, "")

        return result