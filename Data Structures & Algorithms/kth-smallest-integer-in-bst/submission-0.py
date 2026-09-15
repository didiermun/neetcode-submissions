# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.rig
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        input: node , k
        output?: int
        
        - empty tree, -:-> null
        - unique nodes
        
        
        approaches:
        - smallest -leftmost
        - inorder traversal - BST: ascending order
        
        plan:
            - inorder traversal
            
            k -> 3
            
                - def f(node, count):
                    if not node: return 
                     
                    - f(node.r)
                    - currnode
                    - add to the arr
                    - count++ #  3 
                    - if count == k:
                        return node.val
                    - f(node.l)
                    
                    - return 
                

            - asave valuesin an arr
            - return the kth value(idx:k-1) 
            
            n-> len(arr) idx: n- k
        
        
        """
        
        nodeValues = [] # stack 
        def inorder(node):
            if not node:
                return 
                
            inorder(node.left)
            if len(nodeValues) == 0 or nodeValues[-1] != node.val:
                nodeValues.append(node.val)
            inorder(node.right)
            
            return 
            
        # nodeValues == [1,2,3,4]
        inorder(root)
        return nodeValues[k-1]
        
    

         
        
        
            
        