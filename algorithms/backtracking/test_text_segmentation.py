"""
Testes para Text Segmentation (Segmentação de Texto)
===================================================

Testes unitários para todas as implementações de segmentação de texto.
"""

import pytest
from text_segmentation import (
    text_segmentation_backtracking,
    text_segmentation_with_memoization,
    text_segmentation_all_solutions,
    text_segmentation_count_solutions,
    text_segmentation_optimized,
    analyze_text_segmentation_complexity,
    create_word_dict,
    is_word_in_dict
)


class TestTextSegmentationBasic:
    """Testes para a implementação básica de backtracking."""
    
    def test_empty_string(self):
        """Testa string vazia."""
        def is_word(s): return False
        
        result = text_segmentation_backtracking("", is_word)
        assert result == []
    
    def test_single_word(self):
        """Testa string com uma única palavra."""
        def is_word(s): return s == "hello"
        
        result = text_segmentation_backtracking("hello", is_word)
        assert result == ["hello"]
    
    def test_two_words(self):
        """Testa string com duas palavras."""
        def is_word(s): return s in ["hello", "world"]
        
        result = text_segmentation_backtracking("helloworld", is_word)
        assert result == ["hello", "world"]
    
    def test_no_segmentation_possible(self):
        """Testa caso onde não é possível segmentar."""
        def is_word(s): return s in ["hello", "world"]
        
        result = text_segmentation_backtracking("helloworldx", is_word)
        assert result is None
    
    def test_multiple_words(self):
        """Testa string com múltiplas palavras."""
        def is_word(s): return s in ["i", "am", "a", "student"]
        
        result = text_segmentation_backtracking("iamastudent", is_word)
        assert result == ["i", "am", "a", "student"]


class TestTextSegmentationMemoization:
    """Testes para a implementação com memoização."""
    
    def test_basic_memoization(self):
        """Testa funcionalidade básica com memoização."""
        def is_word(s): return s in ["hello", "world"]
        
        result = text_segmentation_with_memoization("helloworld", is_word)
        assert result == ["hello", "world"]
    
    def test_complex_case_memoization(self):
        """Testa caso complexo com memoização."""
        def is_word(s): return s in ["i", "am", "a", "student", "of", "computer", "science"]
        
        result = text_segmentation_with_memoization("iamastudentofcomputerscience", is_word)
        expected = ["i", "am", "a", "student", "of", "computer", "science"]
        assert result == expected
    
    def test_no_solution_memoization(self):
        """Testa caso sem solução com memoização."""
        def is_word(s): return s in ["hello", "world"]
        
        result = text_segmentation_with_memoization("helloworldx", is_word)
        assert result is None


class TestTextSegmentationAllSolutions:
    """Testes para encontrar todas as soluções."""
    
    def test_single_solution(self):
        """Testa caso com uma única solução."""
        def is_word(s): return s in ["hello", "world"]
        
        result = text_segmentation_all_solutions("helloworld", is_word)
        assert result == [["hello", "world"]]
    
    def test_multiple_solutions(self):
        """Testa caso com múltiplas soluções."""
        def is_word(s): return s in ["a", "aa", "aaa"]
        
        result = text_segmentation_all_solutions("aaa", is_word)
        # Possíveis segmentações: ["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]
        assert len(result) == 4
        assert ["a", "a", "a"] in result
        assert ["a", "aa"] in result
        assert ["aa", "a"] in result
        assert ["aaa"] in result
    
    def test_no_solutions(self):
        """Testa caso sem soluções."""
        def is_word(s): return s in ["hello", "world"]
        
        result = text_segmentation_all_solutions("helloworldx", is_word)
        assert result == []


class TestTextSegmentationCountSolutions:
    """Testes para contar soluções."""
    
    def test_count_single_solution(self):
        """Testa contagem de uma única solução."""
        def is_word(s): return s in ["hello", "world"]
        
        count = text_segmentation_count_solutions("helloworld", is_word)
        assert count == 1
    
    def test_count_multiple_solutions(self):
        """Testa contagem de múltiplas soluções."""
        def is_word(s): return s in ["a", "aa", "aaa"]
        
        count = text_segmentation_count_solutions("aaa", is_word)
        assert count == 4
    
    def test_count_no_solutions(self):
        """Testa contagem quando não há soluções."""
        def is_word(s): return s in ["hello", "world"]
        
        count = text_segmentation_count_solutions("helloworldx", is_word)
        assert count == 0


class TestTextSegmentationOptimized:
    """Testes para a implementação otimizada."""
    
    def test_optimized_basic(self):
        """Testa funcionalidade básica da versão otimizada."""
        def is_word(s): return s in ["hello", "world"]
        
        result = text_segmentation_optimized("helloworld", is_word)
        assert result == ["hello", "world"]
    
    def test_optimized_complex(self):
        """Testa caso complexo da versão otimizada."""
        def is_word(s): return s in ["i", "am", "a", "student", "of", "computer", "science"]
        
        result = text_segmentation_optimized("iamastudentofcomputerscience", is_word)
        expected = ["i", "am", "a", "student", "of", "computer", "science"]
        assert result == expected
    
    def test_optimized_no_solution(self):
        """Testa caso sem solução da versão otimizada."""
        def is_word(s): return s in ["hello", "world"]
        
        result = text_segmentation_optimized("helloworldx", is_word)
        assert result is None


class TestTextSegmentationCorrectness:
    """Testes de correção comparando diferentes implementações."""
    
    def test_correctness_multiple_implementations(self):
        """Testa que todas as implementações retornam o mesmo resultado."""
        def is_word(s): return s in ["i", "am", "a", "student"]
        text = "iamastudent"
        
        result1 = text_segmentation_backtracking(text, is_word)
        result2 = text_segmentation_with_memoization(text, is_word)
        result3 = text_segmentation_optimized(text, is_word)
        
        assert result1 == result2 == result3
        assert result1 == ["i", "am", "a", "student"]
    
    def test_correctness_no_solution(self):
        """Testa correção quando não há solução."""
        def is_word(s): return s in ["hello", "world"]
        text = "helloworldx"
        
        result1 = text_segmentation_backtracking(text, is_word)
        result2 = text_segmentation_with_memoization(text, is_word)
        result3 = text_segmentation_optimized(text, is_word)
        
        assert result1 == result2 == result3 is None


class TestTextSegmentationComplexity:
    """Testes para análise de complexidade."""
    
    def test_complexity_analysis(self):
        """Testa análise de complexidade."""
        def is_word(s): return s in ["a", "b", "c"]
        text = "abc"
        
        analysis = analyze_text_segmentation_complexity(text, is_word)
        
        assert analysis["input_size"] == 3
        assert "O(2^n)" in analysis["time_complexity"]["worst_case"]
        assert "O(n)" in analysis["space_complexity"]["total"]
        assert "Memoização" in analysis["optimizations"][0]


class TestTextSegmentationEdgeCases:
    """Testes para casos extremos."""
    
    def test_single_character(self):
        """Testa string com um único caractere."""
        def is_word(s): return s == "a"
        
        result = text_segmentation_backtracking("a", is_word)
        assert result == ["a"]
    
    def test_repeated_characters(self):
        """Testa string com caracteres repetidos."""
        def is_word(s): return s in ["a", "aa", "aaa"]
        
        result = text_segmentation_backtracking("aaa", is_word)
        assert result is not None
        assert len(result) > 0
    
    def test_long_word(self):
        """Testa string que forma uma única palavra longa."""
        def is_word(s): return s == "supercalifragilisticexpialidocious"
        
        result = text_segmentation_backtracking("supercalifragilisticexpialidocious", is_word)
        assert result == ["supercalifragilisticexpialidocious"]


class TestTextSegmentationHelperFunctions:
    """Testes para funções auxiliares."""
    
    def test_create_word_dict(self):
        """Testa criação de dicionário de palavras."""
        words = ["hello", "world", "python"]
        word_dict = create_word_dict(words)
        
        assert "hello" in word_dict
        assert "world" in word_dict
        assert "python" in word_dict
        assert "invalid" not in word_dict
    
    def test_is_word_in_dict(self):
        """Testa verificação de palavra no dicionário."""
        word_dict = {"hello", "world", "python"}
        
        assert is_word_in_dict("hello", word_dict) is True
        assert is_word_in_dict("world", word_dict) is True
        assert is_word_in_dict("python", word_dict) is True
        assert is_word_in_dict("invalid", word_dict) is False


class TestTextSegmentationPerformance:
    """Testes de performance."""
    
    def test_performance_small_input(self):
        """Testa performance com entrada pequena."""
        def is_word(s): return s in ["a", "b", "c", "d"]
        text = "abcd"
        
        import time
        start = time.time()
        result = text_segmentation_backtracking(text, is_word)
        end = time.time()
        
        assert result is not None
        assert end - start < 1.0  # Deve ser muito rápido
    
    def test_performance_medium_input(self):
        """Testa performance com entrada média."""
        def is_word(s): return s in ["a", "aa", "aaa", "aaaa"]
        text = "aaaa"
        
        import time
        start = time.time()
        result = text_segmentation_backtracking(text, is_word)
        end = time.time()
        
        assert result is not None
        assert end - start < 1.0  # Deve ser rápido


if __name__ == "__main__":
    pytest.main([__file__]) 