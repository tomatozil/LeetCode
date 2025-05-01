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
        
        ret = [words[i] for i in range(len(words)-1, -1, -1)]
        
        return ' '.join(ret)
            
            

