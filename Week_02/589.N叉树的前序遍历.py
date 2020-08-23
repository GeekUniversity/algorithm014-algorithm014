class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return None
        stack, output = [root,], []
        # 每次都将子节点从右往左添加，这样保证最左边的子节点在栈顶
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
        return output