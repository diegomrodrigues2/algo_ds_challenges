from __future__ import annotations
from typing import Optional
from collections import deque

class TreeNode:
    """Nó de uma árvore binária."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None, right: Optional['TreeNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right

def tree_height_recursive(root):
    """Calcula a altura da árvore"""
    if root is None:
        return 0
    
    left_height = tree_height_recursive(root.left)
    right_height = tree_height_recursive(root.right)
    return max(left_height, right_height) + 1

def tree_height(root: Optional[TreeNode]) -> int:
    """Calcula a altura da árvore.

    Args:
        root: raiz da árvore binária.

    Returns:
        Altura da árvore, onde uma árvore vazia tem altura 0.
    """
    if root is None:
        return 0
    
    height = 1
    left_queue = deque([])
    right_queue = deque([])

    if root.left:
        left_queue.append(root.left)
    if root.right:
        right_queue.append(root.right)

    while left_queue or right_queue:
        height += 1

        left_node = left_queue.popleft() if left_queue else None

        if left_node:
            if left_node.left:
                left_queue.append(left_node.left)
            if left_node.right:
                right_queue.append(left_node.right)

        right_node = right_queue.popleft() if right_queue else None

        if right_node:        
            if right_node.left:
                left_queue.append(right_node.left)
            if right_node.right:
                right_queue.append(right_node.right)

    return height