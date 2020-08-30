class Solution:
    def __init__(self):
        self.ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def ancestor_tree(current_node):
            if not current_node:
                return False
            left = self.ancestor_tree(current_node.left)
            right = self.ancestor_tree(current_node.right)
            middle = current_node == p or current_node == q
            if middle + left + right >= 2:
                self.ans = current_node
            return middle or left or right
        ancestor_tree(root)
        return self.ans

