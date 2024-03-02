class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes mapped by characters
        self.children = {}  
        # Flag indicating whether the node represents the end of a word
        self.end = False  

class WordDictionary:

    def __init__(self):
        # Initialize the Trie with an empty root node
        self.root = TrieNode()  
        

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            # Create a new node if the child does not exist
            if char not in current.children:
                current.children[char] = TrieNode()  
            current = current.children[char]
        # Mark the last node as representing the end of the inserted word
        current.end = True  

        

    def search(self, word: str) -> bool:
        def dfs(counter, root):
            current = root

            for x in range(counter, len(word)):
                char = word[x]
                # Handle wildcard character "."
                if char == ".":  
                    # Recursively search all child nodes for wildcard query
                    for child in current.children.values():  
                        if dfs(x + 1, child):  
                            return True
                    return False
                else:
                    if char not in current.children:
                        return False

                    current = current.children[char]
            # Return True if the last node represents the end of a word
            return current.end 

        # Start DFS search from the root
        return dfs(0, self.root)  
    
 # ---------- Second Example --------------- 
    

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        stack = [(self.root, 0)] # Initialize stack with root node and depth 0

        while stack:
            curr, idx = stack.pop() # Pop a node and its depth
            # print(f"Visiting node with value {node.value} at depth {depth}")

            if idx == len(word):
                if curr.isEnd:
                    return True
            elif word[idx] == ".":
                for child in curr.children.values():
                    stack.append((child, idx+1))
            elif word[idx] in curr.children:
                stack.append((curr.children[word[idx]], idx+1))

        return False  


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
    
# Commented code
    # Definition of a Trie node (individual element of the Trie)
class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes where each key is a character of the alphabet
        # and the corresponding value is another TrieNode (child node).
        self.children = {}  
        # Boolean flag to indicate whether this node marks the end of a word in the Trie.
        self.end = False  

# A class to represent the whole Trie structure, which is a collection of TrieNodes.
class WordDictionary:

    def __init__(self):
        # The Trie is initialized with a single, empty root node.
        self.root = TrieNode()  
        
    # Method to add a word to the Trie.
    def addWord(self, word: str) -> None:
        current = self.root  # Start from the root node.
        for char in word:  # Iterate through each character in the word.
            # If the current character is not present in the current node's children,
            # create a new TrieNode and add it to the children dictionary.
            if char not in current.children:
                current.children[char] = TrieNode()  
            # Move to the child node associated with the current character.
            current = current.children[char]
        # After adding all characters, mark the last node as the end of a word.
        current.end = True  
        
    # Method to search for a word in the Trie, supporting wildcard '.' searches.
    def search(self, word: str) -> bool:
        # Helper function for depth-first search (DFS).
        def dfs(counter, root):
            current = root  # Start DFS from the given node.

            # Iterate through each character in the word starting from 'counter' index.
            for x in range(counter, len(word)):
                char = word[x]
                # If the current character is a wildcard '.',
                # we must check all possible child paths.
                if char == ".":  
                    # Iterate through each child node.
                    for child in current.children.values():  
                        # Recursively search the remainder of the word from this child.
                        # If any path returns True (word found), return True.
                        if dfs(x + 1, child):  
                            return True
                    # If no paths matched the word, return False.
                    return False
                else:
                    # If the character is not in the current node's children,
                    # the word does not exist in the Trie.
                    if char not in current.children:
                        return False
                    # Move to the next node in the path.
                    current = current.children[char]
            # After processing all characters, check if we're at a word's end.
            return current.end 

        # Start the DFS search from the root node for the entire word.
        return dfs(0, self.root)  
