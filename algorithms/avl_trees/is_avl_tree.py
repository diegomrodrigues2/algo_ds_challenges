from __future__ import annotations
from typing import Optional


class TreeNode:
    """Node of a binary tree."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None,
                 right: Optional['TreeNode'] | None = None, height: int = 1) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.height = height


def is_avl_tree(root: Optional[TreeNode]) -> bool:
    """Verify if a tree is a valid AVL tree.

    The tree must be a binary search tree and for every node the difference
    between the heights of left and right subtrees cannot exceed 1.

    Args:
        root: root node of the tree.

    Returns:
        ``True`` if the tree is a valid AVL tree; ``False`` otherwise.
    """
    raise NotImplementedError("Implementar esta função")

