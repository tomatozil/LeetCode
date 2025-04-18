class Node:
    def __init__(self, char=None, is_end=False):
        self.char = char
        self.is_end = is_end
        self.children = {}

class Trie:

    def __init__(self):
        self.node = Node()

    def insert(self, word: str) -> None:
        cur = self.node
        for c in word:
            if c not in cur.children:
                child = Node(c)
                cur.children[c] = child
                cur = child
            else:
                cur = cur.children[c]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.node
        for c in word:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        if cur.is_end == False:
            return False
        return True 

    def startsWith(self, prefix: str) -> bool:
        cur = self.node
        for c in prefix:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)