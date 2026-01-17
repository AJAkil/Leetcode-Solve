"""
PROBLEM: Design File System (LeetCode 1166 - Medium)
-----------------------------------------------------
Implement a file system with:
- createPath(path, value): creates new path and associates value. Returns false if path exists or parent doesn't exist.
- get(path): returns value associated with path, or -1 if doesn't exist.

Example:
createPath("/a", 1) -> true
createPath("/a/b", 2) -> true
createPath("/c/d", 1) -> false (parent /c doesn't exist)
get("/a/b") -> 2

KEY INSIGHT: Trie/Prefix Tree for hierarchical path structure.
- Each node represents a directory/file
- Split path by '/' and traverse/create nodes
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = -1
    
    def insert(self, path, value):
        node = self

        path_parts = path.split('/')

        for child_dir in path_parts[1:-1]:
            if child_dir not in node.children:
                return False

            node = node.children[child_dir] # propogate the node
        
        if path_parts[-1] in node.children:
            return False

        # add the final node at the end
        node.children[path_parts[-1]] = TrieNode()
        node.children[path_parts[-1]].value = value

        return True
    
    def get(self, path):
        node = self

        path_parts = path.split('/')

        for child_dir in path_parts[1:]:
            if child_dir not in node.children:
                return -1
            
            node = node.children[child_dir]
        
        return node.value

class FileSystem:

    def __init__(self):
        self.root = TrieNode()
        

    def createPath(self, path: str, value: int) -> bool:
        return self.root.insert(path, value)
        

    def get(self, path: str) -> int:
        return self.root.get(path)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)