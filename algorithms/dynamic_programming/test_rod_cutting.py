import pytest
from .rod_cutting import (
    rod_cutting_recursive,
    rod_cutting_dp,
    rod_cutting_bottom_up,
    rod_cutting_with_solution
)


class TestRodCutting:
    
    def test_rod_cutting_recursive_basic(self):
        """Testa casos básicos da solução recursiva"""
        prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
        
        # Caso base: barra de comprimento 0
        assert rod_cutting_recursive(prices, 0) == 0
        
        # Barra de comprimento 1
        assert rod_cutting_recursive(prices, 1) == 1
        
        # Barra de comprimento 2
        assert rod_cutting_recursive(prices, 2) == 5
        
        # Barra de comprimento 3
        assert rod_cutting_recursive(prices, 3) == 8
        
        # Barra de comprimento 4
        assert rod_cutting_recursive(prices, 4) == 10  # 2 + 2 = 5 + 5 = 10
    
    def test_rod_cutting_recursive_medium(self):
        """Testa casos médios da solução recursiva"""
        prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
        
        # Barra de comprimento 5
        assert rod_cutting_recursive(prices, 5) == 13  # 2 + 3 = 5 + 8 = 13
        
        # Barra de comprimento 6
        assert rod_cutting_recursive(prices, 6) == 17  # 6 = 17
        
        # Barra de comprimento 7
        assert rod_cutting_recursive(prices, 7) == 18  # 1 + 6 = 1 + 17 = 18
        
        # Barra de comprimento 8
        assert rod_cutting_recursive(prices, 8) == 22  # 2 + 6 = 5 + 17 = 22
    
    def test_rod_cutting_dp_basic(self):
        """Testa casos básicos da solução com programação dinâmica"""
        prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
        
        assert rod_cutting_dp(prices, 0) == 0
        assert rod_cutting_dp(prices, 1) == 1
        assert rod_cutting_dp(prices, 2) == 5
        assert rod_cutting_dp(prices, 3) == 8
        assert rod_cutting_dp(prices, 4) == 10
    
    def test_rod_cutting_dp_medium(self):
        """Testa casos médios da solução com programação dinâmica"""
        prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
        
        assert rod_cutting_dp(prices, 5) == 13
        assert rod_cutting_dp(prices, 6) == 17
        assert rod_cutting_dp(prices, 7) == 18
        assert rod_cutting_dp(prices, 8) == 22
    
    def test_rod_cutting_bottom_up_basic(self):
        """Testa casos básicos da solução bottom-up"""
        prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
        
        assert rod_cutting_bottom_up(prices, 0) == 0
        assert rod_cutting_bottom_up(prices, 1) == 1
        assert rod_cutting_bottom_up(prices, 2) == 5
        assert rod_cutting_bottom_up(prices, 3) == 8
        assert rod_cutting_bottom_up(prices, 4) == 10
    
    def test_rod_cutting_bottom_up_medium(self):
        """Testa casos médios da solução bottom-up"""
        prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
        
        assert rod_cutting_bottom_up(prices, 5) == 13
        assert rod_cutting_bottom_up(prices, 6) == 17
        assert rod_cutting_bottom_up(prices, 7) == 18
        assert rod_cutting_bottom_up(prices, 8) == 22
    
    def test_rod_cutting_with_solution_basic(self):
        """Testa a solução que retorna os cortes ótimos"""
        prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
        
        # Barra de comprimento 4
        max_profit, cuts = rod_cutting_with_solution(prices, 4)
        assert max_profit == 10
        assert sum(cuts) == 4  # Os cortes devem somar o comprimento total
        
        # Barra de comprimento 5
        max_profit, cuts = rod_cutting_with_solution(prices, 5)
        assert max_profit == 13
        assert sum(cuts) == 5
    
    def test_rod_cutting_with_solution_medium(self):
        """Testa casos médios da solução com cortes"""
        prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
        
        # Barra de comprimento 6
        max_profit, cuts = rod_cutting_with_solution(prices, 6)
        assert max_profit == 17
        assert sum(cuts) == 6
        
        # Barra de comprimento 8
        max_profit, cuts = rod_cutting_with_solution(prices, 8)
        assert max_profit == 22
        assert sum(cuts) == 8
    
    def test_rod_cutting_edge_cases(self):
        """Testa casos extremos"""
        prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
        
        # Preços decrescentes (caso patológico)
        decreasing_prices = [0, 10, 9, 8, 7, 6, 5, 4, 3]
        assert rod_cutting_recursive(decreasing_prices, 4) == 40  # 4 pedaços de 1
        assert rod_cutting_dp(decreasing_prices, 4) == 40
        assert rod_cutting_bottom_up(decreasing_prices, 4) == 40
        
        # Preços iguais
        equal_prices = [0, 5, 5, 5, 5, 5, 5, 5, 5]
        assert rod_cutting_recursive(equal_prices, 4) == 20  # 4 pedaços de 1
        assert rod_cutting_dp(equal_prices, 4) == 20
        assert rod_cutting_bottom_up(equal_prices, 4) == 20
    
    def test_rod_cutting_consistency(self):
        """Testa que todas as implementações retornam o mesmo resultado"""
        prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
        
        for n in range(1, 9):
            recursive_result = rod_cutting_recursive(prices, n)
            dp_result = rod_cutting_dp(prices, n)
            bottom_up_result = rod_cutting_bottom_up(prices, n)
            
            assert recursive_result == dp_result, f"Falha para n={n}"
            assert dp_result == bottom_up_result, f"Falha para n={n}"
    
    def test_rod_cutting_performance(self):
        """Testa performance com entrada maior"""
        # Preços para barra de comprimento 20
        prices = [0] + [i * 2 for i in range(1, 21)]
        
        # Testa que as soluções DP são mais eficientes que a recursiva
        # (não deve demorar mais que alguns segundos)
        result_dp = rod_cutting_dp(prices, 15)
        result_bottom_up = rod_cutting_bottom_up(prices, 15)
        
        assert result_dp == result_bottom_up
        assert result_dp > 0  # Deve retornar um valor positivo 