# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_index=0
        inorder_index = {value:i for i,value in enumerate(inorder)}
        def dfs(left,right):
            nonlocal preorder_index
            if left>right:
                return None
            
            root_val = preorder[preorder_index]
            mid = inorder_index[root_val]
            root = TreeNode(root_val)
            preorder_index+=1
            root.left=dfs(left,mid-1)
            root.right=dfs(mid+1,right)
            return root
        return dfs(0,len(inorder)-1)
