"""
Problema das Árvores Binárias de Busca Ótimas (Optimal Binary Search Tree)

Dado um conjunto de chaves ordenadas com probabilidades de busca conhecidas,
construir uma árvore binária de busca que minimize o custo médio de busca.

Exemplo:
- Chaves: [10, 20, 30, 40]
- Probabilidades: [0.1, 0.3, 0.2, 0.4]
- Objetivo: Minimizar custo esperado = Σ(profundidade(i) × probabilidade(i))
"""

class TreeNode:
    """Nó de uma árvore binária de busca"""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def optimal_bst_basic(keys, probabilities):
    """
    Solução básica para o problema de árvore binária de busca ótima.
    
    Args:
        keys: Lista de chaves ordenadas
        probabilities: Lista de probabilidades correspondentes
    
    Returns:
        O custo mínimo esperado da árvore ótima
    """
    n = len(keys)
    
    # TODO: Implementar solução básica
    # Dica: Use programação dinâmica com tabela 2D
    raise NotImplementedError("Implementar solução básica")


def optimal_bst_with_tree(keys, probabilities):
    """
    Solução que retorna tanto o custo mínimo quanto a árvore ótima.
    
    Args:
        keys: Lista de chaves ordenadas
        probabilities: Lista de probabilidades correspondentes
    
    Returns:
        Tupla (custo_minimo, raiz_da_arvore)
    """
    n = len(keys)
    
    # TODO: Implementar solução que constrói a árvore
    # Dica: Mantenha uma tabela para rastrear as raízes escolhidas
    raise NotImplementedError("Implementar solução que constrói a árvore")


def optimal_bst_knuth_optimization(keys, probabilities):
    """
    Solução otimizada usando a propriedade de monotonicidade de Knuth.
    
    Args:
        keys: Lista de chaves ordenadas
        probabilities: Lista de probabilidades correspondentes
    
    Returns:
        O custo mínimo esperado da árvore ótima
    """
    n = len(keys)
    
    # TODO: Implementar otimização de Knuth
    # Dica: Use a propriedade root[i][j-1] ≤ root[i][j] ≤ root[i+1][j]
    raise NotImplementedError("Implementar otimização de Knuth")


def optimal_bst_space_optimized(keys, probabilities):
    """
    Solução com otimização de espaço usando apenas duas linhas da tabela.
    
    Args:
        keys: Lista de chaves ordenadas
        probabilities: Lista de probabilidades correspondentes
    
    Returns:
        O custo mínimo esperado da árvore ótima
    """
    n = len(keys)
    
    # TODO: Implementar otimização de espaço
    # Dica: Use apenas duas linhas da tabela dp
    raise NotImplementedError("Implementar otimização de espaço")


def compute_expected_cost(tree, keys, probabilities):
    """
    Calcula o custo esperado de uma árvore binária de busca.
    
    Args:
        tree: Raiz da árvore
        keys: Lista de chaves
        probabilities: Lista de probabilidades
    
    Returns:
        O custo esperado da árvore
    """
    def compute_cost_recursive(node, depth):
        if node is None:
            return 0
        
        # Custo do nó atual
        key_index = keys.index(node.key)
        node_cost = depth * probabilities[key_index]
        
        # Custo das subárvores
        left_cost = compute_cost_recursive(node.left, depth + 1)
        right_cost = compute_cost_recursive(node.right, depth + 1)
        
        return node_cost + left_cost + right_cost
    
    return compute_cost_recursive(tree, 1)


def build_balanced_bst(keys):
    """
    Constrói uma árvore binária de busca balanceada para comparação.
    
    Args:
        keys: Lista de chaves ordenadas
    
    Returns:
        Raiz da árvore balanceada
    """
    def build_bst_recursive(start, end):
        if start > end:
            return None
        
        mid = (start + end) // 2
        node = TreeNode(keys[mid])
        node.left = build_bst_recursive(start, mid - 1)
        node.right = build_bst_recursive(mid + 1, end)
        
        return node
    
    return build_bst_recursive(0, len(keys) - 1)


def validate_bst_properties(tree, keys):
    """
    Valida se uma árvore é uma BST válida.
    
    Args:
        tree: Raiz da árvore
        keys: Lista de chaves originais
    
    Returns:
        True se a árvore é uma BST válida
    """
    def inorder_traversal(node, result):
        if node is None:
            return
        inorder_traversal(node.left, result)
        result.append(node.key)
        inorder_traversal(node.right, result)
    
    result = []
    inorder_traversal(tree, result)
    
    # Verificar se contém todas as chaves em ordem
    return result == keys 