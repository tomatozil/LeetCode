class Solution:
    def reverseWords(self, s: str) -> str:
        trim_str = s.strip()
        output = ""
        i = len(trim_str)-1
        while i >= 0:
            if trim_str[i] != " ":
                word = ""
                while i >= 0 and trim_str[i] != " ":
                    word = trim_str[i] + word
                    i -= 1
                output += word
            else:
                output += " "
                while i >= 0 and trim_str[i] == " ":
                    i -= 1
        return output
            
            

