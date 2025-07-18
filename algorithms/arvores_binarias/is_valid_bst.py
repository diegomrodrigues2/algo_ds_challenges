from __future__ import annotations
from typing import Optional


class TreeNode:
    """Nó de uma árvore binária."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None, right: Optional['TreeNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """Verifica se a árvore é uma BST válida.

    Args:
        root: raiz da árvore.

    Returns:
        ``True`` se a árvore obedecer as propriedades de uma BST, caso contrário ``False``.
    """
    def validate(node: Optional[TreeNode], min_val: Optional[int], max_val: Optional[int]) -> bool:
        # Empty tree is valid
        if node is None:
            return True
        
        # Check if current node violates BST property
        if (min_val is not None and node.value <= min_val) or \
           (max_val is not None and node.value >= max_val):
            return False
        
        # Recursively validate left and right subtrees with updated bounds
        return (
            validate(node.left, min_val, node.value) and 
            validate(node.right, node.value, max_val)
        )
    
    return validate(root, None, None)

    
    

    
