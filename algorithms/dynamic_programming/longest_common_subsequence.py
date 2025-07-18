"""
Problema da Subsequência Comum Mais Longa (Longest Common Subsequence - LCS)

Dadas duas sequências, encontre a subsequência comum mais longa entre elas.
Uma subsequência é uma sequência que pode ser derivada de outra sequência 
deletando alguns elementos sem mudar a ordem dos elementos restantes.

Exemplo:
- Sequência 1: "ABCDGH"
- Sequência 2: "AEDFHR"
- LCS: "ADH" (comprimento 3)
"""

def lcs_recursive(str1, str2):
    """
    Solução recursiva para o problema da subsequência comum mais longa.
    
    Args:
        str1: Primeira string
        str2: Segunda string
    
    Returns:
        O comprimento da subsequência comum mais longa
    """
    m, n = len(str1), len(str2)
    
    def lcs_helper(i, j):
        # TODO: Implementar a lógica recursiva
        # Se os caracteres são iguais, incluir na subsequência
        # Caso contrário, tentar excluir de uma das strings
        raise NotImplementedError("Implementar a lógica recursiva")
    
    return lcs_helper(0, 0)


def lcs_dp(str1, str2):
    """
    Solução com programação dinâmica para o problema da subsequência comum mais longa.
    
    Args:
        str1: Primeira string
        str2: Segunda string
    
    Returns:
        O comprimento da subsequência comum mais longa
    """
    m, n = len(str1), len(str2)
    
    # TODO: Implementar solução com programação dinâmica
    # Dica: Use uma matriz 2D para armazenar os resultados
    raise NotImplementedError("Implementar solução com programação dinâmica")


def lcs_with_string(str1, str2):
    """
    Solução que retorna tanto o comprimento quanto a subsequência comum mais longa.
    
    Args:
        str1: Primeira string
        str2: Segunda string
    
    Returns:
        Tupla (comprimento, subsequência)
    """
    m, n = len(str1), len(str2)
    
    # TODO: Implementar solução que retorna a subsequência
    # Dica: Mantenha um array para rastrear as escolhas feitas
    raise NotImplementedError("Implementar solução que retorna a subsequência")


def lcs_three_strings(str1, str2, str3):
    """
    Problema da subsequência comum mais longa para três strings.
    
    Args:
        str1: Primeira string
        str2: Segunda string
        str3: Terceira string
    
    Returns:
        O comprimento da subsequência comum mais longa
    """
    m, n, p = len(str1), len(str2), len(str3)
    
    # TODO: Implementar solução para três strings
    # Dica: Use uma matriz 3D para armazenar os resultados
    raise NotImplementedError("Implementar solução para três strings")


def lcs_palindrome(str1):
    """
    Encontrar a subsequência palíndroma mais longa de uma string.
    Uma subsequência palíndroma é uma subsequência que é um palíndromo.
    
    Args:
        str1: String de entrada
    
    Returns:
        O comprimento da subsequência palíndroma mais longa
    """
    n = len(str1)
    
    # TODO: Implementar solução para subsequência palíndroma
    # Dica: Compare a string com sua reversa usando LCS
    raise NotImplementedError("Implementar solução para subsequência palíndroma") 