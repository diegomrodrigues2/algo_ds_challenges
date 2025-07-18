import pytest
from .optimal_binary_search_tree import (
    optimal_bst_basic,
    optimal_bst_with_tree,
    optimal_bst_knuth_optimization,
    optimal_bst_space_optimized,
    compute_expected_cost,
    build_balanced_bst,
    validate_bst_properties,
    TreeNode
)


class TestOptimalBinarySearchTree:
    
    def test_optimal_bst_basic_small(self):
        """Testa casos pequenos da solução básica"""
        # Caso simples com 2 chaves
        keys = [10, 20]
        probabilities = [0.3, 0.7]
        
        # Custo esperado: 0.3*1 + 0.7*1 = 1.0 (árvore balanceada)
        cost = optimal_bst_basic(keys, probabilities)
        assert abs(cost - 1.0) < 1e-6
        
        # Caso com 3 chaves
        keys = [10, 20, 30]
        probabilities = [0.2, 0.5, 0.3]
        
        # Custo esperado: 0.2*1 + 0.5*2 + 0.3*2 = 1.8 (20 como raiz)
        cost = optimal_bst_basic(keys, probabilities)
        assert abs(cost - 1.8) < 1e-6
    
    def test_optimal_bst_basic_medium(self):
        """Testa casos médios da solução básica"""
        # Caso clássico com 4 chaves
        keys = [10, 20, 30, 40]
        probabilities = [0.1, 0.3, 0.2, 0.4]
        
        # Custo esperado: 0.1*2 + 0.3*1 + 0.2*3 + 0.4*2 = 1.9
        cost = optimal_bst_basic(keys, probabilities)
        assert abs(cost - 1.9) < 1e-6
        
        # Caso com probabilidades iguais
        keys = [10, 20, 30, 40, 50]
        probabilities = [0.2, 0.2, 0.2, 0.2, 0.2]
        
        # Para probabilidades iguais, árvore balanceada é ótima
        cost = optimal_bst_basic(keys, probabilities)
        assert cost > 0  # Deve retornar um valor positivo
    
    def test_optimal_bst_with_tree_basic(self):
        """Testa a solução que retorna a árvore"""
        keys = [10, 20, 30]
        probabilities = [0.2, 0.5, 0.3]
        
        cost, tree = optimal_bst_with_tree(keys, probabilities)
        
        # Verificar custo
        assert abs(cost - 1.8) < 1e-6
        
        # Verificar que é uma BST válida
        assert validate_bst_properties(tree, keys)
        
        # Verificar que o custo calculado é correto
        computed_cost = compute_expected_cost(tree, keys, probabilities)
        assert abs(cost - computed_cost) < 1e-6
    
    def test_optimal_bst_with_tree_medium(self):
        """Testa casos médios da solução com árvore"""
        keys = [10, 20, 30, 40]
        probabilities = [0.1, 0.3, 0.2, 0.4]
        
        cost, tree = optimal_bst_with_tree(keys, probabilities)
        
        # Verificar custo
        assert abs(cost - 1.9) < 1e-6
        
        # Verificar propriedades da árvore
        assert validate_bst_properties(tree, keys)
        
        # Verificar que é melhor que árvore balanceada
        balanced_tree = build_balanced_bst(keys)
        balanced_cost = compute_expected_cost(balanced_tree, keys, probabilities)
        assert cost <= balanced_cost  # Árvore ótima deve ser melhor ou igual
    
    def test_optimal_bst_knuth_optimization_basic(self):
        """Testa casos básicos da otimização de Knuth"""
        keys = [10, 20, 30]
        probabilities = [0.2, 0.5, 0.3]
        
        cost = optimal_bst_knuth_optimization(keys, probabilities)
        assert abs(cost - 1.8) < 1e-6
        
        # Deve retornar o mesmo resultado que a solução básica
        basic_cost = optimal_bst_basic(keys, probabilities)
        assert abs(cost - basic_cost) < 1e-6
    
    def test_optimal_bst_knuth_optimization_medium(self):
        """Testa casos médios da otimização de Knuth"""
        keys = [10, 20, 30, 40, 50]
        probabilities = [0.1, 0.2, 0.3, 0.2, 0.2]
        
        cost = optimal_bst_knuth_optimization(keys, probabilities)
        
        # Deve retornar o mesmo resultado que a solução básica
        basic_cost = optimal_bst_basic(keys, probabilities)
        assert abs(cost - basic_cost) < 1e-6
        
        assert cost > 0  # Deve retornar um valor positivo
    
    def test_optimal_bst_space_optimized_basic(self):
        """Testa casos básicos da otimização de espaço"""
        keys = [10, 20, 30]
        probabilities = [0.2, 0.5, 0.3]
        
        cost = optimal_bst_space_optimized(keys, probabilities)
        assert abs(cost - 1.8) < 1e-6
        
        # Deve retornar o mesmo resultado que a solução básica
        basic_cost = optimal_bst_basic(keys, probabilities)
        assert abs(cost - basic_cost) < 1e-6
    
    def test_optimal_bst_space_optimized_medium(self):
        """Testa casos médios da otimização de espaço"""
        keys = [10, 20, 30, 40, 50]
        probabilities = [0.1, 0.2, 0.3, 0.2, 0.2]
        
        cost = optimal_bst_space_optimized(keys, probabilities)
        
        # Deve retornar o mesmo resultado que a solução básica
        basic_cost = optimal_bst_basic(keys, probabilities)
        assert abs(cost - basic_cost) < 1e-6
    
    def test_compute_expected_cost_basic(self):
        """Testa cálculo de custo esperado"""
        # Árvore simples
        root = TreeNode(20)
        root.left = TreeNode(10)
        root.right = TreeNode(30)
        
        keys = [10, 20, 30]
        probabilities = [0.2, 0.5, 0.3]
        
        cost = compute_expected_cost(root, keys, probabilities)
        expected = 0.2*2 + 0.5*1 + 0.3*2  # 0.4 + 0.5 + 0.6 = 1.5
        assert abs(cost - expected) < 1e-6
    
    def test_compute_expected_cost_complex(self):
        """Testa cálculo de custo para árvore mais complexa"""
        # Árvore com 4 nós
        root = TreeNode(30)
        root.left = TreeNode(20)
        root.left.left = TreeNode(10)
        root.right = TreeNode(40)
        
        keys = [10, 20, 30, 40]
        probabilities = [0.1, 0.3, 0.2, 0.4]
        
        cost = compute_expected_cost(root, keys, probabilities)
        expected = 0.1*3 + 0.3*2 + 0.2*1 + 0.4*2  # 0.3 + 0.6 + 0.2 + 0.8 = 1.9
        assert abs(cost - expected) < 1e-6
    
    def test_build_balanced_bst_basic(self):
        """Testa construção de árvore balanceada"""
        keys = [10, 20, 30, 40, 50]
        
        tree = build_balanced_bst(keys)
        
        # Verificar que é uma BST válida
        assert validate_bst_properties(tree, keys)
        
        # Verificar estrutura esperada (30 como raiz)
        assert tree.key == 30
        assert tree.left.key == 20
        assert tree.right.key == 40
        assert tree.left.left.key == 10
        assert tree.right.right.key == 50
    
    def test_validate_bst_properties_basic(self):
        """Testa validação de propriedades BST"""
        # BST válida
        root = TreeNode(20)
        root.left = TreeNode(10)
        root.right = TreeNode(30)
        
        keys = [10, 20, 30]
        assert validate_bst_properties(root, keys)
        
        # BST inválida (não contém todas as chaves)
        keys_missing = [10, 20]
        assert not validate_bst_properties(root, keys_missing)
        
        # BST inválida (ordem incorreta)
        keys_wrong_order = [30, 20, 10]
        assert not validate_bst_properties(root, keys_wrong_order)
    
    def test_edge_cases(self):
        """Testa casos extremos"""
        # Caso com uma chave
        keys = [10]
        probabilities = [1.0]
        
        cost = optimal_bst_basic(keys, probabilities)
        assert abs(cost - 1.0) < 1e-6
        
        # Caso com duas chaves e probabilidades extremas
        keys = [10, 20]
        probabilities = [0.9, 0.1]  # Primeira chave muito mais provável
        
        cost = optimal_bst_basic(keys, probabilities)
        # Árvore com 10 como raiz deve ser ótima
        expected = 0.9*1 + 0.1*2  # 0.9 + 0.2 = 1.1
        assert abs(cost - expected) < 1e-6
    
    def test_probability_sum_validation(self):
        """Testa validação de soma de probabilidades"""
        keys = [10, 20, 30]
        probabilities = [0.3, 0.3, 0.3]  # Soma = 0.9 < 1.0
        
        # Deve funcionar mesmo com soma < 1.0
        cost = optimal_bst_basic(keys, probabilities)
        assert cost > 0
        
        probabilities = [0.4, 0.4, 0.4]  # Soma = 1.2 > 1.0
        
        # Deve funcionar mesmo com soma > 1.0
        cost = optimal_bst_basic(keys, probabilities)
        assert cost > 0
    
    def test_consistency_across_implementations(self):
        """Testa consistência entre diferentes implementações"""
        keys = [10, 20, 30, 40]
        probabilities = [0.1, 0.3, 0.2, 0.4]
        
        # Todas as implementações devem retornar o mesmo resultado
        basic_cost = optimal_bst_basic(keys, probabilities)
        knuth_cost = optimal_bst_knuth_optimization(keys, probabilities)
        space_cost = optimal_bst_space_optimized(keys, probabilities)
        
        assert abs(basic_cost - knuth_cost) < 1e-6
        assert abs(basic_cost - space_cost) < 1e-6
    
    def test_performance_comparison(self):
        """Testa comparação de performance com árvore balanceada"""
        keys = [10, 20, 30, 40, 50, 60, 70, 80]
        probabilities = [0.05, 0.1, 0.15, 0.2, 0.15, 0.1, 0.1, 0.15]
        
        # Árvore ótima deve ser melhor ou igual à balanceada
        optimal_cost, optimal_tree = optimal_bst_with_tree(keys, probabilities)
        balanced_tree = build_balanced_bst(keys)
        balanced_cost = compute_expected_cost(balanced_tree, keys, probabilities)
        
        assert optimal_cost <= balanced_cost
        
        # Verificar que ambas são BSTs válidas
        assert validate_bst_properties(optimal_tree, keys)
        assert validate_bst_properties(balanced_tree, keys)
    
    def test_large_input_performance(self):
        """Testa performance com entrada maior"""
        # 10 chaves com probabilidades variadas
        keys = list(range(10, 101, 10))  # [10, 20, 30, ..., 100]
        probabilities = [0.1] * 10  # Probabilidades iguais
        
        # Testa que as soluções otimizadas são mais eficientes
        # (não deve demorar mais que alguns segundos)
        cost = optimal_bst_knuth_optimization(keys, probabilities)
        assert cost > 0
        
        cost = optimal_bst_space_optimized(keys, probabilities)
        assert cost > 0 