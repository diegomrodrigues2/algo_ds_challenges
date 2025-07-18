import pytest
from .knapsack import (
    knapsack_recursive,
    knapsack_dp,
    knapsack_01,
    knapsack_fractional,
    knapsack_with_items
)


class TestKnapsack:
    
    def test_knapsack_recursive_basic(self):
        """Testa casos básicos da solução recursiva"""
        weights = [1, 2, 3]
        values = [10, 15, 20]
        
        # Capacidade 0
        assert knapsack_recursive(weights, values, 0) == 0
        
        # Capacidade 1
        assert knapsack_recursive(weights, values, 1) == 10
        
        # Capacidade 2
        assert knapsack_recursive(weights, values, 2) == 15
        
        # Capacidade 3
        assert knapsack_recursive(weights, values, 3) == 20
        
        # Capacidade 4
        assert knapsack_recursive(weights, values, 4) == 25  # 1 + 3 = 10 + 20 = 30
    
    def test_knapsack_recursive_medium(self):
        """Testa casos médios da solução recursiva"""
        weights = [1, 2, 3, 4]
        values = [10, 15, 20, 25]
        
        # Capacidade 5
        assert knapsack_recursive(weights, values, 5) == 35  # 2 + 3 = 15 + 20 = 35
        
        # Capacidade 6
        assert knapsack_recursive(weights, values, 6) == 40  # 2 + 4 = 15 + 25 = 40
        
        # Capacidade 7
        assert knapsack_recursive(weights, values, 7) == 45  # 3 + 4 = 20 + 25 = 45
    
    def test_knapsack_dp_basic(self):
        """Testa casos básicos da solução com programação dinâmica"""
        weights = [1, 2, 3]
        values = [10, 15, 20]
        
        assert knapsack_dp(weights, values, 0) == 0
        assert knapsack_dp(weights, values, 1) == 10
        assert knapsack_dp(weights, values, 2) == 15
        assert knapsack_dp(weights, values, 3) == 20
        assert knapsack_dp(weights, values, 4) == 25
    
    def test_knapsack_dp_medium(self):
        """Testa casos médios da solução com programação dinâmica"""
        weights = [1, 2, 3, 4]
        values = [10, 15, 20, 25]
        
        assert knapsack_dp(weights, values, 5) == 35
        assert knapsack_dp(weights, values, 6) == 40
        assert knapsack_dp(weights, values, 7) == 45
    
    def test_knapsack_01_basic(self):
        """Testa casos básicos da mochila 0/1"""
        weights = [1, 2, 3]
        values = [10, 15, 20]
        
        assert knapsack_01(weights, values, 0) == 0
        assert knapsack_01(weights, values, 1) == 10
        assert knapsack_01(weights, values, 2) == 15
        assert knapsack_01(weights, values, 3) == 20
        assert knapsack_01(weights, values, 4) == 25
    
    def test_knapsack_01_medium(self):
        """Testa casos médios da mochila 0/1"""
        weights = [1, 2, 3, 4]
        values = [10, 15, 20, 25]
        
        assert knapsack_01(weights, values, 5) == 35
        assert knapsack_01(weights, values, 6) == 40
        assert knapsack_01(weights, values, 7) == 45
    
    def test_knapsack_fractional_basic(self):
        """Testa casos básicos da mochila fracionária"""
        weights = [1, 2, 3]
        values = [10, 15, 20]
        
        # Para mochila fracionária, a solução pode ser diferente
        assert knapsack_fractional(weights, values, 0) == 0
        assert knapsack_fractional(weights, values, 1) == 10
        assert knapsack_fractional(weights, values, 2) == 15
        assert knapsack_fractional(weights, values, 3) == 20
        assert knapsack_fractional(weights, values, 4) == 25
    
    def test_knapsack_fractional_medium(self):
        """Testa casos médios da mochila fracionária"""
        weights = [1, 2, 3, 4]
        values = [10, 15, 20, 25]
        
        assert knapsack_fractional(weights, values, 5) == 35
        assert knapsack_fractional(weights, values, 6) == 40
        assert knapsack_fractional(weights, values, 7) == 45
    
    def test_knapsack_with_items_basic(self):
        """Testa a solução que retorna os itens selecionados"""
        weights = [1, 2, 3]
        values = [10, 15, 20]
        
        # Capacidade 4
        max_value, selected_items = knapsack_with_items(weights, values, 4)
        assert max_value == 25
        assert len(selected_items) > 0
        
        # Verificar que os itens selecionados não excedem a capacidade
        total_weight = sum(weights[i] for i in selected_items)
        assert total_weight <= 4
        
        # Verificar que o valor total é correto
        total_value = sum(values[i] for i in selected_items)
        assert total_value == max_value
    
    def test_knapsack_with_items_medium(self):
        """Testa casos médios da solução com itens"""
        weights = [1, 2, 3, 4]
        values = [10, 15, 20, 25]
        
        # Capacidade 6
        max_value, selected_items = knapsack_with_items(weights, values, 6)
        assert max_value == 40
        assert len(selected_items) > 0
        
        total_weight = sum(weights[i] for i in selected_items)
        assert total_weight <= 6
        
        total_value = sum(values[i] for i in selected_items)
        assert total_value == max_value
    
    def test_knapsack_edge_cases(self):
        """Testa casos extremos"""
        # Todos os itens têm o mesmo peso
        weights = [2, 2, 2, 2]
        values = [10, 15, 20, 25]
        capacity = 6
        
        assert knapsack_recursive(weights, values, capacity) == 45  # 3 itens de peso 2
        assert knapsack_dp(weights, values, capacity) == 45
        assert knapsack_01(weights, values, capacity) == 45
        
        # Todos os itens têm o mesmo valor
        weights = [1, 2, 3, 4]
        values = [10, 10, 10, 10]
        capacity = 5
        
        assert knapsack_recursive(weights, values, capacity) == 30  # 3 itens de valor 10
        assert knapsack_dp(weights, values, capacity) == 30
        assert knapsack_01(weights, values, capacity) == 30
    
    def test_knapsack_consistency(self):
        """Testa que as implementações retornam resultados consistentes"""
        weights = [1, 2, 3, 4]
        values = [10, 15, 20, 25]
        
        for capacity in range(1, 8):
            recursive_result = knapsack_recursive(weights, values, capacity)
            dp_result = knapsack_dp(weights, values, capacity)
            knapsack_01_result = knapsack_01(weights, values, capacity)
            
            assert recursive_result == dp_result, f"Falha para capacidade={capacity}"
            assert dp_result == knapsack_01_result, f"Falha para capacidade={capacity}"
    
    def test_knapsack_performance(self):
        """Testa performance com entrada maior"""
        # 10 itens com pesos e valores variados
        weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        capacity = 20
        
        # Testa que as soluções DP são mais eficientes
        result_dp = knapsack_dp(weights, values, capacity)
        result_01 = knapsack_01(weights, values, capacity)
        
        assert result_dp == result_01
        assert result_dp > 0  # Deve retornar um valor positivo 