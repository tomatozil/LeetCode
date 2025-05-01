class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        
        ret = [words[i] for i in range(len(words)-1, -1, -1)]
        
        return ' '.join(ret)
            
            

