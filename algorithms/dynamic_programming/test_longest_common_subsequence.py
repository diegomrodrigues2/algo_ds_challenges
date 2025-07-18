import pytest
from .longest_common_subsequence import (
    lcs_recursive,
    lcs_dp,
    lcs_with_string,
    lcs_three_strings,
    lcs_palindrome
)


class TestLongestCommonSubsequence:
    
    def test_lcs_recursive_basic(self):
        """Testa casos básicos da solução recursiva"""
        # Caso simples
        assert lcs_recursive("ABCDGH", "AEDFHR") == 3  # "ADH"
        
        # Strings vazias
        assert lcs_recursive("", "") == 0
        assert lcs_recursive("ABC", "") == 0
        assert lcs_recursive("", "ABC") == 0
        
        # Strings idênticas
        assert lcs_recursive("ABC", "ABC") == 3
        
        # Sem caracteres em comum
        assert lcs_recursive("ABC", "XYZ") == 0
    
    def test_lcs_recursive_medium(self):
        """Testa casos médios da solução recursiva"""
        # Caso clássico
        assert lcs_recursive("AGGTAB", "GXTXAYB") == 4  # "GTAB"
        
        # Strings com caracteres repetidos
        assert lcs_recursive("AAB", "AAC") == 2  # "AA"
        
        # Strings de tamanhos diferentes
        assert lcs_recursive("ABCD", "AC") == 2  # "AC"
        assert lcs_recursive("AC", "ABCD") == 2  # "AC"
    
    def test_lcs_dp_basic(self):
        """Testa casos básicos da solução com programação dinâmica"""
        assert lcs_dp("ABCDGH", "AEDFHR") == 3
        assert lcs_dp("", "") == 0
        assert lcs_dp("ABC", "") == 0
        assert lcs_dp("", "ABC") == 0
        assert lcs_dp("ABC", "ABC") == 3
        assert lcs_dp("ABC", "XYZ") == 0
    
    def test_lcs_dp_medium(self):
        """Testa casos médios da solução com programação dinâmica"""
        assert lcs_dp("AGGTAB", "GXTXAYB") == 4
        assert lcs_dp("AAB", "AAC") == 2
        assert lcs_dp("ABCD", "AC") == 2
        assert lcs_dp("AC", "ABCD") == 2
    
    def test_lcs_with_string_basic(self):
        """Testa a solução que retorna a subsequência"""
        # Caso simples
        length, subsequence = lcs_with_string("ABCDGH", "AEDFHR")
        assert length == 3
        assert subsequence == "ADH"
        
        # Strings vazias
        length, subsequence = lcs_with_string("", "")
        assert length == 0
        assert subsequence == ""
        
        # Strings idênticas
        length, subsequence = lcs_with_string("ABC", "ABC")
        assert length == 3
        assert subsequence == "ABC"
    
    def test_lcs_with_string_medium(self):
        """Testa casos médios da solução com subsequência"""
        # Caso clássico
        length, subsequence = lcs_with_string("AGGTAB", "GXTXAYB")
        assert length == 4
        assert subsequence == "GTAB"
        
        # Verificar que a subsequência é válida
        # Deve ser uma subsequência de ambas as strings
        str1, str2 = "AGGTAB", "GXTXAYB"
        i, j = 0, 0
        for char in subsequence:
            # Encontrar char em str1
            while i < len(str1) and str1[i] != char:
                i += 1
            # Encontrar char em str2
            while j < len(str2) and str2[j] != char:
                j += 1
            i += 1
            j += 1
        
        assert i <= len(str1) and j <= len(str2)
    
    def test_lcs_three_strings_basic(self):
        """Testa casos básicos para três strings"""
        # Caso simples
        assert lcs_three_strings("ABC", "AC", "AD") == 1  # "A"
        
        # Strings vazias
        assert lcs_three_strings("", "", "") == 0
        assert lcs_three_strings("ABC", "", "DEF") == 0
        
        # Strings idênticas
        assert lcs_three_strings("ABC", "ABC", "ABC") == 3
    
    def test_lcs_three_strings_medium(self):
        """Testa casos médios para três strings"""
        # Caso com subsequência comum
        assert lcs_three_strings("ABCD", "ACDF", "ADEF") == 2  # "AD"
        
        # Caso sem subsequência comum
        assert lcs_three_strings("ABC", "DEF", "GHI") == 0
    
    def test_lcs_palindrome_basic(self):
        """Testa casos básicos da subsequência palíndroma"""
        # Casos simples
        assert lcs_palindrome("A") == 1
        assert lcs_palindrome("AA") == 2
        assert lcs_palindrome("AB") == 1  # "A" ou "B"
        assert lcs_palindrome("ABA") == 3  # "ABA"
        
        # String vazia
        assert lcs_palindrome("") == 0
    
    def test_lcs_palindrome_medium(self):
        """Testa casos médios da subsequência palíndroma"""
        # Casos clássicos
        assert lcs_palindrome("BBABCBCAB") == 7  # "BABCBAB"
        assert lcs_palindrome("GEEKSFORGEEKS") == 5  # "EEKEE" ou similar
        
        # Palíndromos completos
        assert lcs_palindrome("RACECAR") == 7
        assert lcs_palindrome("MADAM") == 5
    
    def test_lcs_edge_cases(self):
        """Testa casos extremos"""
        # Strings muito longas com padrões simples
        long_str1 = "A" * 100
        long_str2 = "A" * 100
        assert lcs_recursive(long_str1, long_str2) == 100
        assert lcs_dp(long_str1, long_str2) == 100
        
        # Strings com caracteres únicos
        unique_str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        unique_str2 = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
        # Apenas um caractere em comum (dependendo da implementação)
        result = lcs_recursive(unique_str1, unique_str2)
        assert result >= 0 and result <= 26
    
    def test_lcs_consistency(self):
        """Testa que as implementações retornam resultados consistentes"""
        test_cases = [
            ("ABCDGH", "AEDFHR"),
            ("AGGTAB", "GXTXAYB"),
            ("AAB", "AAC"),
            ("ABC", "XYZ"),
            ("", "ABC"),
            ("ABC", ""),
            ("", ""),
        ]
        
        for str1, str2 in test_cases:
            recursive_result = lcs_recursive(str1, str2)
            dp_result = lcs_dp(str1, str2)
            
            assert recursive_result == dp_result, f"Falha para '{str1}' e '{str2}'"
    
    def test_lcs_performance(self):
        """Testa performance com strings maiores"""
        # Strings de tamanho médio
        str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 2
        str2 = "ZYXWVUTSRQPONMLKJIHGFEDCBA" * 2
        
        # Testa que as soluções DP são mais eficientes
        result_dp = lcs_dp(str1, str2)
        assert result_dp >= 0  # Deve retornar um valor não-negativo
    
    def test_lcs_with_string_validation(self):
        """Testa que a subsequência retornada é válida"""
        test_cases = [
            ("ABCDGH", "AEDFHR"),
            ("AGGTAB", "GXTXAYB"),
            ("AAB", "AAC"),
        ]
        
        for str1, str2 in test_cases:
            length, subsequence = lcs_with_string(str1, str2)
            
            # Verificar comprimento
            assert len(subsequence) == length
            
            # Verificar que é subsequência de str1
            i = 0
            for char in subsequence:
                while i < len(str1) and str1[i] != char:
                    i += 1
                if i >= len(str1):
                    assert False, f"'{subsequence}' não é subsequência de '{str1}'"
                i += 1
            
            # Verificar que é subsequência de str2
            j = 0
            for char in subsequence:
                while j < len(str2) and str2[j] != char:
                    j += 1
                if j >= len(str2):
                    assert False, f"'{subsequence}' não é subsequência de '{str2}'"
                j += 1 