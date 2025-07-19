import pytest
from .median_finder import MedianFinder


class TestMedianFinder:
    """Testes para a classe MedianFinder."""
    
    def test_empty_finder(self):
        """Testa o comportamento quando não há números."""
        finder = MedianFinder()
        # Não deve lançar erro, mas o comportamento pode variar
        # dependendo da implementação específica
    
    def test_single_number(self):
        """Testa com um único número."""
        finder = MedianFinder()
        finder.add_num(5)
        assert finder.find_median() == 5.0
    
    def test_two_numbers(self):
        """Testa com dois números."""
        finder = MedianFinder()
        finder.add_num(1)
        finder.add_num(2)
        assert finder.find_median() == 1.5
    
    def test_three_numbers(self):
        """Testa com três números."""
        finder = MedianFinder()
        finder.add_num(1)
        finder.add_num(2)
        finder.add_num(3)
        assert finder.find_median() == 2.0
    
    def test_four_numbers(self):
        """Testa com quatro números."""
        finder = MedianFinder()
        finder.add_num(1)
        finder.add_num(2)
        finder.add_num(3)
        finder.add_num(4)
        assert finder.find_median() == 2.5
    
    def test_negative_numbers(self):
        """Testa com números negativos."""
        finder = MedianFinder()
        finder.add_num(-1)
        finder.add_num(-2)
        finder.add_num(-3)
        assert finder.find_median() == -2.0
    
    def test_duplicate_numbers(self):
        """Testa com números duplicados."""
        finder = MedianFinder()
        finder.add_num(1)
        finder.add_num(1)
        finder.add_num(1)
        assert finder.find_median() == 1.0
    
    def test_large_numbers(self):
        """Testa com números grandes."""
        finder = MedianFinder()
        finder.add_num(1000)
        finder.add_num(2000)
        finder.add_num(3000)
        assert finder.find_median() == 2000.0
    
    def test_stream_behavior(self):
        """Testa o comportamento de stream."""
        finder = MedianFinder()
        
        # Adiciona números sequencialmente
        finder.add_num(1)
        assert finder.find_median() == 1.0
        
        finder.add_num(2)
        assert finder.find_median() == 1.5
        
        finder.add_num(3)
        assert finder.find_median() == 2.0
        
        finder.add_num(4)
        assert finder.find_median() == 2.5
        
        finder.add_num(5)
        assert finder.find_median() == 3.0 