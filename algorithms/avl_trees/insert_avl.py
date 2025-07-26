from __future__ import annotations
from typing import Optional


class TreeNode:
    """Node of an AVL tree."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None,
                 right: Optional['TreeNode'] | None = None, height: int = 1) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.height = height


def insert_avl(root: Optional[TreeNode], value: int) -> TreeNode:
    """Insert a value into an AVL tree.
    
    This function implements insertion with AVL balance property, which maintains
    strict balance through factor of balance constraints. AVL trees are optimized
    for read-heavy workloads due to their minimum height guarantee.
    
    The AVL balance property ensures that for every node:
    |height(left_subtree) - height(right_subtree)| ≤ 1
    
    This results in O(log n) height and faster search operations, but requires
    more rotations during insertions and deletions.

    Args:
        root: Root of the AVL tree (may be ``None``).
        value: Value to insert.

    Returns:
        New root of the tree after insertion and rebalancing.
        
    Example:
        # Insert sequence: 10, 5, 15, 3, 7
        # After insertion of 3, a rotation is needed
        root = insert_avl(root, 10)  # No rotation
        root = insert_avl(root, 5)   # No rotation
        root = insert_avl(root, 15)  # No rotation
        root = insert_avl(root, 3)   # LL rotation needed
        root = insert_avl(root, 7)   # No rotation
    """
    raise NotImplementedError("Implementar esta função")

