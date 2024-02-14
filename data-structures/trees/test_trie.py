class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.end

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
    
    def print_tree_ascii(self, node=None, prefix='', level=0):
        if node is None:
            node = self.root
            # Start from the root with an empty prefix
            print("Root")
        for char, child in sorted(node.children.items()):
            # Generate the prefix for the current level
            indent = " " * 4 * level
            child_prefix = prefix + char
            if child.end:
                # Mark the end of a word distinctly
                print(f"{indent}--> {child_prefix} [End]")
            else:
                print(f"{indent}--> {child_prefix}")
            # Recursively print children
            self.print_tree_ascii(child, child_prefix, level + 1)


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
trie.insert("baby")
trie.insert("cat")
print('---------------')
trie.print_tree_ascii()
