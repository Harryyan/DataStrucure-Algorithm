class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
    
    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        i = 0
        n = len(prefix)
        
        for ch in prefix:
            x = ord(ch) - ord("a")
            if not node.children[x]:
                return None
            node = node.children[x]
            
            if node.isEnd and i < n - 1:
                node = self
                
            i += 1
                
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
            
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None
