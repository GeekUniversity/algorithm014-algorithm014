


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            intd = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[intd])
            root.left = self.buildTree(preorder, inorder[:intd])
            root.right = self.buildTree(preorder, inorder[intd + 1 :])
            return root

