"""
Testes para multiplicação matriz-vetor paralela
"""

import pytest
import numpy as np
from .matrix_vector_multiply import (
    p_mat_vec, p_mat_vec_wrong, serial_mat_vec,
    create_test_matrix, create_test_vector,
    analyze_work_span, verify_result
)


class TestPMatVec:
    """Testes para a função p_mat_vec"""
    
    def test_identity_matrix(self):
        """Testa multiplicação com matriz identidade"""
        n = 3
        A = create_test_matrix(n, "identity")
        x = create_test_vector(n, "sequential")
        y = [0] * n
        
        p_mat_vec(A, x, y, n)
        
        # Matriz identidade deve retornar o vetor original
        assert y == [1, 2, 3]
    
    def test_ones_matrix(self):
        """Testa multiplicação com matriz de uns"""
        n = 2
        A = create_test_matrix(n, "ones")
        x = create_test_vector(n, "ones")
        y = [0] * n
        
        p_mat_vec(A, x, y, n)
        
        # Matriz de uns deve somar todos os elementos do vetor
        assert y == [2, 2]  # 1*1 + 1*1 = 2 para cada linha
    
    def test_sequential_matrix(self):
        """Testa multiplicação com matriz sequencial"""
        n = 2
        A = create_test_matrix(n, "sequential")
        x = create_test_vector(n, "ones")
        y = [0] * n
        
        p_mat_vec(A, x, y, n)
        
        # A = [[1, 2], [3, 4]], x = [1, 1]
        # y[0] = 1*1 + 2*1 = 3
        # y[1] = 3*1 + 4*1 = 7
        assert y == [3, 7]
    
    def test_consistency_with_serial(self):
        """Testa que p_mat_vec produz os mesmos resultados que serial_mat_vec"""
        n = 4
        A = create_test_matrix(n, "sequential")
        x = create_test_vector(n, "alternating")
        
        y_parallel = [0] * n
        y_serial = [0] * n
        
        p_mat_vec(A, x, y_parallel, n)
        serial_mat_vec(A, x, y_serial, n)
        
        for i in range(n):
            assert abs(y_parallel[i] - y_serial[i]) < 1e-10
    
    def test_zero_vector(self):
        """Testa multiplicação com vetor zero"""
        n = 3
        A = create_test_matrix(n, "sequential")
        x = [0] * n
        y = [0] * n
        
        p_mat_vec(A, x, y, n)
        
        # Resultado deve ser zero
        assert all(val == 0 for val in y)
    
    def test_large_matrix(self):
        """Testa com matriz maior"""
        n = 10
        A = create_test_matrix(n, "identity")
        x = create_test_vector(n, "sequential")
        y = [0] * n
        
        p_mat_vec(A, x, y, n)
        
        # Matriz identidade deve retornar o vetor original
        expected = list(range(1, n + 1))
        assert y == expected


class TestSerialMatVec:
    """Testes para a função serial_mat_vec"""
    
    def test_basic_multiplication(self):
        """Testa multiplicação básica"""
        A = [[1, 2], [3, 4]]
        x = [5, 6]
        y = [0, 0]
        
        serial_mat_vec(A, x, y, 2)
        
        # y[0] = 1*5 + 2*6 = 17
        # y[1] = 3*5 + 4*6 = 39
        assert y == [17, 39]
    
    def test_identity_matrix(self):
        """Testa com matriz identidade"""
        n = 3
        A = create_test_matrix(n, "identity")
        x = create_test_vector(n, "sequential")
        y = [0] * n
        
        serial_mat_vec(A, x, y, n)
        
        assert y == [1, 2, 3]


class TestPMatVecWrong:
    """Testes para a função p_mat_vec_wrong (demonstração de race condition)"""
    
    def test_produces_correct_result_serial(self):
        """Testa que produz resultado correto na implementação serial"""
        # Nota: Esta função demonstra race conditions, mas nossa implementação
        # serial ainda produz o resultado correto
        n = 2
        A = create_test_matrix(n, "sequential")
        x = create_test_vector(n, "ones")
        y = [0] * n
        
        p_mat_vec_wrong(A, x, y, n)
        
        # Deve produzir o mesmo resultado que a versão correta
        y_correct = [0] * n
        p_mat_vec(A, x, y_correct, n)
        
        assert y == y_correct


class TestCreateTestMatrix:
    """Testes para criação de matrizes de teste"""
    
    def test_identity_matrix(self):
        """Testa criação de matriz identidade"""
        n = 3
        A = create_test_matrix(n, "identity")
        
        expected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        assert A == expected
    
    def test_ones_matrix(self):
        """Testa criação de matriz de uns"""
        n = 2
        A = create_test_matrix(n, "ones")
        
        expected = [[1, 1], [1, 1]]
        assert A == expected
    
    def test_sequential_matrix(self):
        """Testa criação de matriz sequencial"""
        n = 2
        A = create_test_matrix(n, "sequential")
        
        expected = [[1, 2], [3, 4]]
        assert A == expected
    
    def test_invalid_pattern(self):
        """Testa padrão inválido"""
        with pytest.raises(ValueError):
            create_test_matrix(3, "invalid")


class TestCreateTestVector:
    """Testes para criação de vetores de teste"""
    
    def test_ones_vector(self):
        """Testa criação de vetor de uns"""
        n = 3
        x = create_test_vector(n, "ones")
        
        assert x == [1, 1, 1]
    
    def test_sequential_vector(self):
        """Testa criação de vetor sequencial"""
        n = 3
        x = create_test_vector(n, "sequential")
        
        assert x == [1, 2, 3]
    
    def test_alternating_vector(self):
        """Testa criação de vetor alternado"""
        n = 4
        x = create_test_vector(n, "alternating")
        
        assert x == [1, -1, 1, -1]
    
    def test_invalid_pattern(self):
        """Testa padrão inválido"""
        with pytest.raises(ValueError):
            create_test_vector(3, "invalid")


class TestWorkSpanAnalysis:
    """Testes para análise de work/span"""
    
    def test_analysis_structure(self):
        """Testa que a análise retorna a estrutura correta"""
        result = analyze_work_span(5)
        
        assert 'work' in result
        assert 'span' in result
        assert 'parallelism' in result
        assert 'n' in result
        
        assert isinstance(result['work'], int)
        assert isinstance(result['span'], int)
        assert isinstance(result['parallelism'], float)
        assert isinstance(result['n'], int)
    
    def test_work_calculation(self):
        """Testa cálculo do work"""
        for n in range(1, 10):
            result = analyze_work_span(n)
            expected_work = n * n
            assert result['work'] == expected_work
    
    def test_span_calculation(self):
        """Testa cálculo do span"""
        for n in range(1, 10):
            result = analyze_work_span(n)
            expected_span = n
            assert result['span'] == expected_span
    
    def test_parallelism_calculation(self):
        """Testa cálculo de parallelism"""
        for n in range(1, 10):
            result = analyze_work_span(n)
            expected_parallelism = (n * n) / n
            assert abs(result['parallelism'] - expected_parallelism) < 1e-10
    
    def test_parallelism_growth(self):
        """Testa que parallelism cresce linearmente"""
        result_5 = analyze_work_span(5)
        result_10 = analyze_work_span(10)
        result_15 = analyze_work_span(15)
        
        # Parallelism deve crescer linearmente com n
        assert result_10['parallelism'] > result_5['parallelism']
        assert result_15['parallelism'] > result_10['parallelism']
        
        # Verifica crescimento linear
        ratio_5_10 = result_10['parallelism'] / result_5['parallelism']
        ratio_10_15 = result_15['parallelism'] / result_10['parallelism']
        
        assert abs(ratio_5_10 - 2) < 0.1  # 10/5 = 2
        assert abs(ratio_10_15 - 1.5) < 0.1  # 15/10 = 1.5


class TestVerifyResult:
    """Testes para verificação de resultados"""
    
    def test_correct_result(self):
        """Testa verificação de resultado correto"""
        n = 3
        A = create_test_matrix(n, "sequential")
        x = create_test_vector(n, "ones")
        y = [0] * n
        
        p_mat_vec(A, x, y, n)
        
        assert verify_result(A, x, y, n)
    
    def test_incorrect_result(self):
        """Testa verificação de resultado incorreto"""
        n = 2
        A = create_test_matrix(n, "identity")
        x = create_test_vector(n, "ones")
        y = [0, 0]  # Resultado incorreto
        
        assert not verify_result(A, x, y, n)
    
    def test_zero_result(self):
        """Testa verificação de resultado zero"""
        n = 3
        A = create_test_matrix(n, "sequential")
        x = [0] * n
        y = [0] * n
        
        p_mat_vec(A, x, y, n)
        
        assert verify_result(A, x, y, n)


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
    
    def test_quadratic_work_growth(self):
        """Testa crescimento quadrático do work"""
        results = [analyze_work_span(n) for n in range(1, 6)]
        
        # Verifica que work cresce quadraticamente
        for i in range(1, len(results)):
            ratio = results[i]['work'] / results[i-1]['work']
            expected_ratio = ((i+1) / i) ** 2
            assert abs(ratio - expected_ratio) < 0.1


if __name__ == "__main__":
    pytest.main([__file__]) 