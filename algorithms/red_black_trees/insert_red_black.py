from __future__ import annotations
from typing import Optional


RED = "red"
BLACK = "black"


class RBNode:
    """Nó de uma árvore Rubro-Negra."""

    def __init__(self, value: int, color: str = RED,
                 left: Optional['RBNode'] | None = None,
                 right: Optional['RBNode'] | None = None,
                 parent: Optional['RBNode'] | None = None) -> None:
        self.value = value
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent


def insert(root: Optional[RBNode], value: int) -> RBNode:
    """Insere um valor em uma árvore Rubro-Negra.
    
    Esta função implementa inserção com propriedades Red-Black, que mantêm
    balanceamento flexível através de regras de cores. Red-Black trees são
    otimizadas para write-heavy workloads devido ao menor número de rotações.
    
    As propriedades Red-Black garantem que:
    1. Raiz é sempre preta
    2. Nós vermelhos não têm filhos vermelhos
    3. Todos os caminhos da raiz às folhas têm mesmo número de nós pretos
    
    Isso resulta em altura limitada (h ≤ 2×log₂(n+1)) e menos rotações durante
    inserções e remoções, mas altura ligeiramente maior que AVL.

    Args:
        root: raiz atual da árvore ou ``None`` se vazia.
        value: valor a ser inserido.

    Returns:
        Nova raiz da árvore contendo ``value`` após rebalanceamento.
        
    Example:
        # Sequência de inserção: 10, 5, 15, 3, 7
        # Após inserção de 3, recolorização pode ser necessária
        root = insert(root, 10)  # Raiz preta
        root = insert(root, 5)   # Possível recolorização
        root = insert(root, 15)  # Possível recolorização
        root = insert(root, 3)   # Possível rotação
        root = insert(root, 7)   # Possível recolorização
    """
    raise NotImplementedError("Implementar esta função")
