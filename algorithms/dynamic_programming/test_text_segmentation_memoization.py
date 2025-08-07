"""
Testes para Segmentação de Texto com Memoização

Este módulo contém testes abrangentes para validar a implementação
do Desafio 22: Segmentação de Texto com Memoização.
"""

import unittest
import time
from typing import Set, List, Optional

from text_segmentation_memoization import (
    text_segmentation_memoization,
    text_segmentation_backtracking,
    text_segmentation_tabulation,
    text_segmentation_optimized_memoization,
    compare_approaches,
    analyze_text_segmentation_complexity,
    generate_test_cases
)


class TestTextSegmentationMemoization(unittest.TestCase):
    """Testes para segmentação de texto com memoização."""
    
    def setUp(self):
        """Configuração inicial para os testes."""
        self.basic_dictionary = {"i", "like", "gfg"}
        self.english_dictionary = {"cat", "cats", "and", "sand", "dog", "pine", "apple", "pineapple"}
        self.simple_dictionary = {"a", "aa", "aaa", "aaaa"}
    
    def test_basic_cases(self):
        """Testa casos básicos de segmentação."""
        test_cases = [
            ("ilike", self.basic_dictionary, ["i", "like"]),
            ("ilikegfg", self.basic_dictionary, ["i", "like", "gfg"]),
            ("ilikemangoes", self.basic_dictionary, None),
        ]
        
        for text, dictionary, expected in test_cases:
            with self.subTest(text=text):
                result = text_segmentation_memoization(text, dictionary)
                self.assertEqual(result, expected)
    
    def test_edge_cases(self):
        """Testa casos extremos."""
        # String vazia
        result = text_segmentation_memoization("", self.basic_dictionary)
        self.assertEqual(result, [])
        
        # String de um caractere
        result = text_segmentation_memoization("i", self.basic_dictionary)
        self.assertEqual(result, ["i"])
        
        # String sem solução
        result = text_segmentation_memoization("xyz", self.basic_dictionary)
        self.assertIsNone(result)
    
    def test_overlapping_words(self):
        """Testa casos com palavras sobrepostas."""
        # Caso onde uma palavra contém outra
        result = text_segmentation_memoization("pineapple", self.english_dictionary)
        self.assertIn(result, [["pineapple"], ["pine", "apple"]])
        
        # Caso com múltiplas possibilidades
        result = text_segmentation_memoization("catsanddog", self.english_dictionary)
        self.assertIsNotNone(result)
        self.assertTrue(all(word in self.english_dictionary for word in result))
    
    def test_long_strings(self):
        """Testa strings longas."""
        # String longa com repetição
        long_text = "a" * 100
        result = text_segmentation_memoization(long_text, self.simple_dictionary)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 100)  # Deve ser segmentado em 100 "a"s
    
    def test_all_approaches_consistency(self):
        """Testa se todas as abordagens produzem resultados consistentes."""
        test_cases = [
            ("ilike", self.basic_dictionary),
            ("ilikegfg", self.basic_dictionary),
            ("catsanddog", self.english_dictionary),
            ("a" * 20, self.simple_dictionary),
        ]
        
        for text, dictionary in test_cases:
            with self.subTest(text=text):
                # Testa todas as implementações
                memo_result = text_segmentation_memoization(text, dictionary)
                tabulation_result = text_segmentation_tabulation(text, dictionary)
                optimized_result = text_segmentation_optimized_memoization(text, dictionary)
                
                # Backtracking pode ser muito lento para strings longas
                if len(text) <= 20:
                    backtracking_result = text_segmentation_backtracking(text, dictionary)
                    self.assertEqual(memo_result, backtracking_result)
                
                # Todas as outras implementações devem ser consistentes
                self.assertEqual(memo_result, tabulation_result)
                self.assertEqual(memo_result, optimized_result)
    
    def test_performance_improvement(self):
        """Testa se a memoização realmente melhora a performance."""
        # Teste com string moderada
        text = "a" * 15
        dictionary = self.simple_dictionary
        
        # Mede tempo do backtracking
        start_time = time.time()
        backtracking_result = text_segmentation_backtracking(text, dictionary)
        backtracking_time = time.time() - start_time
        
        # Mede tempo da memoização
        start_time = time.time()
        memoization_result = text_segmentation_memoization(text, dictionary)
        memoization_time = time.time() - start_time
        
        # Verifica que os resultados são iguais
        self.assertEqual(backtracking_result, memoization_result)
        
        # Verifica que a memoização é mais rápida
        self.assertLess(memoization_time, backtracking_time)
        
        # Verifica melhoria significativa (pelo menos 2x mais rápida)
        improvement_ratio = backtracking_time / memoization_time
        self.assertGreater(improvement_ratio, 2.0)
    
    def test_memoization_cache_effectiveness(self):
        """Testa se o cache de memoização está funcionando corretamente."""
        # String que força múltiplas chamadas recursivas
        text = "aaaaaaaaaa"  # 10 'a's
        dictionary = {"a", "aa", "aaa"}
        
        # Primeira execução
        start_time = time.time()
        result1 = text_segmentation_memoization(text, dictionary)
        time1 = time.time() - start_time
        
        # Segunda execução (deve usar cache)
        start_time = time.time()
        result2 = text_segmentation_memoization(text, dictionary)
        time2 = time.time() - start_time
        
        # Resultados devem ser iguais
        self.assertEqual(result1, result2)
        
        # Segunda execução deve ser mais rápida (cache)
        self.assertLess(time2, time1)
    
    def test_complexity_analysis(self):
        """Testa a análise de complexidade."""
        analysis = analyze_text_segmentation_complexity(100, 50)
        
        # Verifica se a análise contém os campos esperados
        expected_fields = [
            'input_size', 'dictionary_size', 'complexity_class',
            'space_complexity', 'exponential_improvement',
            'memoization_benefit', 'practical_viability'
        ]
        
        for field in expected_fields:
            self.assertIn(field, analysis)
        
        # Verifica valores específicos
        self.assertEqual(analysis['input_size'], 100)
        self.assertEqual(analysis['dictionary_size'], 50)
        self.assertEqual(analysis['complexity_class'], 'O(n²)')
        self.assertTrue(analysis['exponential_improvement'])
    
    def test_compare_approaches(self):
        """Testa a função de comparação de abordagens."""
        text = "ilikegfg"
        dictionary = self.basic_dictionary
        
        comparison = compare_approaches(text, dictionary)
        
        # Verifica estrutura da comparação
        self.assertIn('input_text', comparison)
        self.assertIn('dictionary_size', comparison)
        self.assertIn('approaches', comparison)
        self.assertIn('performance_improvement', comparison)
        
        # Verifica que todas as abordagens foram testadas
        approaches = comparison['approaches']
        self.assertIn('backtracking', approaches)
        self.assertIn('memoization', approaches)
        self.assertIn('tabulation', approaches)
        self.assertIn('optimized_memoization', approaches)
        
        # Verifica que os resultados são consistentes
        results = [approach['result'] for approach in approaches.values()]
        self.assertTrue(all(result == results[0] for result in results))
    
    def test_generate_test_cases(self):
        """Testa a geração de casos de teste."""
        test_cases = generate_test_cases()
        
        # Verifica que há casos de teste
        self.assertGreater(len(test_cases), 0)
        
        # Verifica estrutura dos casos de teste
        for text, dictionary, expected in test_cases:
            self.assertIsInstance(text, str)
            self.assertIsInstance(dictionary, set)
            self.assertIsInstance(expected, (list, type(None)))
            
            # Testa se o caso de teste funciona
            result = text_segmentation_memoization(text, dictionary)
            self.assertEqual(result, expected)
    
    def test_optimized_memoization_benefits(self):
        """Testa se a memoização otimizada oferece benefícios."""
        # String que se beneficia da ordenação decrescente
        text = "pineapple"
        dictionary = {"pine", "pineapple", "apple"}
        
        # A versão otimizada deve encontrar "pineapple" primeiro
        result = text_segmentation_optimized_memoization(text, dictionary)
        self.assertEqual(result, ["pineapple"])
        
        # A versão normal pode encontrar ["pine", "apple"] primeiro
        result_normal = text_segmentation_memoization(text, dictionary)
        self.assertIn(result_normal, [["pineapple"], ["pine", "apple"]])
    
    def test_error_handling(self):
        """Testa o tratamento de erros."""
        # Testa com entrada None
        with self.assertRaises(TypeError):
            text_segmentation_memoization(None, self.basic_dictionary)
        
        # Testa com dicionário None
        with self.assertRaises(TypeError):
            text_segmentation_memoization("test", None)
        
        # Testa com dicionário vazio
        result = text_segmentation_memoization("test", set())
        self.assertIsNone(result)


class TestTextSegmentationPerformance(unittest.TestCase):
    """Testes de performance para segmentação de texto."""
    
    def test_scalability(self):
        """Testa a escalabilidade das diferentes abordagens."""
        dictionary = {"a", "aa", "aaa", "aaaa"}
        
        # Testa diferentes tamanhos de entrada
        sizes = [10, 20, 30]
        
        for size in sizes:
            with self.subTest(size=size):
                text = "a" * size
                
                # Mede tempo das diferentes abordagens
                times = {}
                
                # Memoização
                start_time = time.time()
                text_segmentation_memoization(text, dictionary)
                times['memoization'] = time.time() - start_time
                
                # Tabulação
                start_time = time.time()
                text_segmentation_tabulation(text, dictionary)
                times['tabulation'] = time.time() - start_time
                
                # Memoização otimizada
                start_time = time.time()
                text_segmentation_optimized_memoization(text, dictionary)
                times['optimized'] = time.time() - start_time
                
                # Verifica que todas as implementações são rápidas
                for approach, execution_time in times.items():
                    self.assertLess(execution_time, 1.0, f"{approach} muito lento para tamanho {size}")
    
    def test_memory_efficiency(self):
        """Testa a eficiência de memória."""
        # Testa com string longa para verificar uso de memória
        text = "a" * 1000
        dictionary = {"a", "aa", "aaa"}
        
        # Deve completar sem erro de memória
        result = text_segmentation_memoization(text, dictionary)
        self.assertIsNotNone(result)
        
        # Deve ter o tamanho esperado
        self.assertEqual(len(result), 1000)


if __name__ == "__main__":
    # Executa os testes
    unittest.main(verbosity=2) 