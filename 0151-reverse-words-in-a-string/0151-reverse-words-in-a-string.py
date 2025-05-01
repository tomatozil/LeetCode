class Solution:
    def reverseWords(self, s: str) -> str:
        trim_str = s.strip()
        words = []
        i = 0
        while i < len(trim_str):
            if trim_str[i] != " ":
                word = ""
                while i < len(trim_str) and trim_str[i] != " ":
                    word = word + trim_str[i]
                    i += 1
                words.append(word)
            else:
                while i < len(trim_str) and trim_str[i] == " ":
                    i += 1
        
        left, right = 0, len(words)-1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        
        return ' '.join(words)
            
            

