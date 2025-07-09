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

    The function must insert ``value`` preserving the AVL balance property and
    return the new root of the tree.

    Args:
        root: Root of the AVL tree (may be ``None``).
        value: Value to insert.

    Returns:
        New root of the tree after insertion.
    """
    raise NotImplementedError("Implementar esta função")

