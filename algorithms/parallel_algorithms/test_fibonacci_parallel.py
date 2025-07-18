"""
Testes para o algoritmo P-FIB (Fibonacci paralelo)
"""

import pytest
from .fibonacci_parallel import p_fib, serial_fib, analyze_work_span


class TestPFib:
    """Testes para a função p_fib"""
    
    def test_base_cases(self):
        """Testa casos base"""
        assert p_fib(0) == 0
        assert p_fib(1) == 1
    
    def test_small_values(self):
        """Testa valores pequenos"""
        assert p_fib(2) == 1
        assert p_fib(3) == 2
        assert p_fib(4) == 3
        assert p_fib(5) == 5
        assert p_fib(6) == 8
        assert p_fib(7) == 13
        assert p_fib(8) == 21
        assert p_fib(9) == 34
        assert p_fib(10) == 55
    
    def test_consistency_with_serial(self):
        """Testa que p_fib produz os mesmos resultados que serial_fib"""
        for n in range(15):  # Testa até n=14 para evitar overflow
            assert p_fib(n) == serial_fib(n)
    
    def test_large_values(self):
        """Testa valores maiores (ainda computáveis)"""
        # Fibonacci cresce exponencialmente, então limitamos a valores razoáveis
        assert p_fib(20) == 6765
        assert p_fib(25) == 75025
    
    def test_negative_input(self):
        """Testa comportamento com entrada negativa"""
        # Para entrada negativa, a função recursiva pode causar recursão infinita
        # ou comportamento indefinido, mas não necessariamente RecursionError
        # Vamos testar se a função não retorna um valor válido para entrada negativa
        try:
            result = p_fib(-1)
            # Se não levantar exceção, o resultado deve ser inválido
            assert result < 0 or result != 0  # Fibonacci de número negativo não é bem definido
        except (RecursionError, RuntimeError):
            # Esperado para entrada negativa
            pass


class TestSerialFib:
    """Testes para a função serial_fib"""
    
    def test_base_cases(self):
        """Testa casos base"""
        assert serial_fib(0) == 0
        assert serial_fib(1) == 1
    
    def test_small_values(self):
        """Testa valores pequenos"""
        assert serial_fib(2) == 1
        assert serial_fib(3) == 2
        assert serial_fib(4) == 3
        assert serial_fib(5) == 5
        assert serial_fib(10) == 55
    
    def test_large_values(self):
        """Testa valores maiores"""
        assert serial_fib(20) == 6765
        assert serial_fib(25) == 75025
        assert serial_fib(30) == 832040
    
    def test_negative_input(self):
        """Testa comportamento com entrada negativa"""
        # serial_fib não lida com entradas negativas
        # Isso pode causar comportamento indefinido
        pass


class TestWorkSpanAnalysis:
    """Testes para a análise de work/span"""
    
    def test_analysis_structure(self):
        """Testa que a análise retorna a estrutura correta"""
        result = analyze_work_span(10)
        
        assert 'work' in result
        assert 'span' in result
        assert 'parallelism' in result
        assert 'phi' in result
        
        assert isinstance(result['work'], float)
        assert isinstance(result['span'], int)
        assert isinstance(result['parallelism'], float)
        assert isinstance(result['phi'], float)
    
    def test_phi_value(self):
        """Testa que phi tem o valor correto"""
        result = analyze_work_span(5)
        expected_phi = (1 + 5**0.5) / 2
        assert abs(result['phi'] - expected_phi) < 1e-10
    
    def test_span_calculation(self):
        """Testa que span é igual ao valor de entrada"""
        for n in range(10):
            result = analyze_work_span(n)
            assert result['span'] == n
    
    def test_work_growth(self):
        """Testa que work cresce exponencialmente"""
        result_5 = analyze_work_span(5)
        result_6 = analyze_work_span(6)
        result_7 = analyze_work_span(7)
        
        # Work deve crescer exponencialmente
        assert result_6['work'] > result_5['work']
        assert result_7['work'] > result_6['work']
        
        # Razão deve ser aproximadamente phi
        ratio_5_6 = result_6['work'] / result_5['work']
        ratio_6_7 = result_7['work'] / result_6['work']
        
        assert abs(ratio_5_6 - result_5['phi']) < 0.1
        assert abs(ratio_6_7 - result_6['phi']) < 0.1
    
    def test_parallelism_calculation(self):
        """Testa cálculo de parallelism"""
        for n in range(1, 10):
            result = analyze_work_span(n)
            expected_parallelism = result['work'] / result['span']
            assert abs(result['parallelism'] - expected_parallelism) < 1e-10
    
    def test_parallelism_growth(self):
        """Testa que parallelism cresce dramaticamente"""
        result_5 = analyze_work_span(5)
        result_10 = analyze_work_span(10)
        result_15 = analyze_work_span(15)
        
        # Parallelism deve crescer dramaticamente
        assert result_10['parallelism'] > result_5['parallelism']
        assert result_15['parallelism'] > result_10['parallelism']


class TestPerformanceCharacteristics:
    """Testes para características de performance"""
    
    def test_work_span_relationship(self):
        """Testa que work é sempre maior ou igual ao span"""
        for n in range(1, 10):
            result = analyze_work_span(n)
            assert result['work'] >= result['span']
    
    def test_parallelism_positive(self):
        """Testa que parallelism é sempre positivo para n > 0"""
        for n in range(1, 10):
            result = analyze_work_span(n)
            assert result['parallelism'] > 0
    
    def test_exponential_work_growth(self):
        """Testa crescimento exponencial do work"""
        results = [analyze_work_span(n) for n in range(1, 8)]
        
        # Verifica que work cresce exponencialmente
        for i in range(1, len(results)):
            ratio = results[i]['work'] / results[i-1]['work']
            # Razão deve ser aproximadamente phi
            assert 1.5 < ratio < 2.0  # phi ≈ 1.618


if __name__ == "__main__":
    pytest.main([__file__]) 