"""
Exemplo de uso para Text Segmentation (Segmentação de Texto)
===========================================================

Script simples para demonstrar o uso das funções de segmentação de texto.
"""

from text_segmentation import (
    text_segmentation_backtracking,
    text_segmentation_with_memoization,
    text_segmentation_all_solutions,
    text_segmentation_count_solutions,
    text_segmentation_optimized,
    create_word_dict,
    is_word_in_dict
)


def main():
    """Função principal com exemplos de uso."""
    
    print("=== Text Segmentation (Segmentação de Texto) ===\n")
    
    # Exemplo 1: Caso básico
    print("Exemplo 1: Caso básico")
    print("Texto: 'helloworld'")
    print("Dicionário: ['hello', 'world']")
    
    def is_word1(s): return s in ["hello", "world"]
    
    result1 = text_segmentation_backtracking("helloworld", is_word1)
    print(f"Resultado: {result1}")
    print()
    
    # Exemplo 2: Caso com múltiplas palavras
    print("Exemplo 2: Caso com múltiplas palavras")
    print("Texto: 'iamastudent'")
    print("Dicionário: ['i', 'am', 'a', 'student']")
    
    def is_word2(s): return s in ["i", "am", "a", "student"]
    
    result2 = text_segmentation_backtracking("iamastudent", is_word2)
    print(f"Resultado: {result2}")
    print()
    
    # Exemplo 3: Caso sem solução
    print("Exemplo 3: Caso sem solução")
    print("Texto: 'helloworldx'")
    print("Dicionário: ['hello', 'world']")
    
    result3 = text_segmentation_backtracking("helloworldx", is_word1)
    print(f"Resultado: {result3}")
    print()
    
    # Exemplo 4: Múltiplas soluções
    print("Exemplo 4: Múltiplas soluções")
    print("Texto: 'aaa'")
    print("Dicionário: ['a', 'aa', 'aaa']")
    
    def is_word4(s): return s in ["a", "aa", "aaa"]
    
    all_solutions = text_segmentation_all_solutions("aaa", is_word4)
    print(f"Todas as soluções: {all_solutions}")
    
    count = text_segmentation_count_solutions("aaa", is_word4)
    print(f"Número de soluções: {count}")
    print()
    
    # Exemplo 5: Comparação de implementações
    print("Exemplo 5: Comparação de implementações")
    print("Texto: 'iamastudent'")
    print("Dicionário: ['i', 'am', 'a', 'student']")
    
    result_basic = text_segmentation_backtracking("iamastudent", is_word2)
    result_memo = text_segmentation_with_memoization("iamastudent", is_word2)
    result_opt = text_segmentation_optimized("iamastudent", is_word2)
    
    print(f"Básico: {result_basic}")
    print(f"Memoização: {result_memo}")
    print(f"Otimizado: {result_opt}")
    print(f"Todos iguais: {result_basic == result_memo == result_opt}")
    print()
    
    # Exemplo 6: Usando funções auxiliares
    print("Exemplo 6: Usando funções auxiliares")
    words = ["hello", "world", "python", "programming"]
    word_dict = create_word_dict(words)
    
    def is_word6(s): return is_word_in_dict(s, word_dict)
    
    result6 = text_segmentation_backtracking("helloworld", is_word6)
    print(f"Resultado: {result6}")
    print()
    
    # Exemplo 7: Caso complexo
    print("Exemplo 7: Caso complexo")
    print("Texto: 'iamastudentofcomputerscience'")
    print("Dicionário: ['i', 'am', 'a', 'student', 'of', 'computer', 'science']")
    
    def is_word7(s): return s in ["i", "am", "a", "student", "of", "computer", "science"]
    
    result7 = text_segmentation_with_memoization("iamastudentofcomputerscience", is_word7)
    print(f"Resultado: {result7}")
    print()
    
    print("=== Fim dos exemplos ===")


if __name__ == "__main__":
    main() 