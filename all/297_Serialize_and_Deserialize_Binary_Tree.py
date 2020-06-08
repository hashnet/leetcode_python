import sys
sys.path.append(".")

from utility.TreeUtility import *

class Codec:

    def __init__(self):
        self.idx = 0

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return [None]

        return [root.val] + self.serialize(root.left) + self.serialize(root.right)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data[self.idx] == None:
            self.idx += 1
            return None
        
        node = TreeNode(data[self.idx])
        self.idx += 1
        node.left = self.deserialize(data)
        node.right = self.deserialize(data)
        return node

        
if __name__ == "__main__":
    codec = Codec()
    prettyPrintTree(codec.deserialize(codec.serialize(stringToTreeNode("[1,2,3,null,null,4,5]"))))