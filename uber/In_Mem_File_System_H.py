'''
Very Good Tutorial: https://algo.monster/liteproblems/588
https://www.youtube.com/watch?v=oXEPfYaMOwI&list=PL1MJrDFRFiKYNOtppzGe9I50Fff3zu9Vf&index=2
'''

class TrieNode:
    def __init__(self):
        self.name = None
        self.is_file = None
        self.content = []
        self.children = {} # name: TrieNode() children for efficient traversal
    

    def insert(self, path, is_file):
        # inserts a new file or directory to the trie data structure
        # returns the node representing the inserted path

        node = self # initial node
        path_members = path.split("/")

        for mem in path_members[1:]:
            if mem not in node.children:
                node.children[mem] = TrieNode()
            node = node.children[mem] # move the node ahead
        
        # mark as file if we are at the end and it is a file
        node.is_file = is_file
        if is_file:
            node.name = path_members[-1]
        
        return node
    

    def search(self, path):
        node = self

        if path == '/':
            return node
        

        path_members = path.split('/')

        for mem in path_members[1:]:
            if mem  not in node.children:
                return None
            node = node.children[mem]
        
        return node
    


class FileSystem:

    def __init__(self):
        self.root = TrieNode()
        

    def ls(self, path: str) -> List[str]:
        node = self.root.search(path)

        if node is None:
            return []
        
        if node.is_file:
            return [node.name]
        
        return sorted(node.children.keys())
    
        

    def mkdir(self, path: str) -> None:
        self.root.insert(path, is_file=False)
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        # if filepath doesnt exist create that file and the path dire
        # and add the content
        file_node = self.root.insert(filePath, is_file=True)
        file_node.content.append(content)
        

    def readContentFromFile(self, filePath: str) -> str:
        file_node = self.root.search(filePath)
        return ''.join(file_node.content)
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)