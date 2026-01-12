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