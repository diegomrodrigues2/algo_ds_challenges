"""
Algoritmo de Karatsuba para Multiplicação Rápida de Inteiros Grandes

Este módulo implementa o algoritmo de Karatsuba, que é um algoritmo de 
divisão e conquista para multiplicar números inteiros grandes de forma eficiente.

O algoritmo reduz a complexidade de O(n²) para O(n^1.585) através da 
identidade algébrica que permite calcular o produto usando apenas 3 
multiplicações recursivas em vez de 4.

Referência: Erickson, "Algorithms", Capítulo 1, Seção 1.9, "Fast Multiplication"
"""


def add_strings(str1: str, str2: str) -> str:
    """
    Adiciona dois números representados como strings.
    
    Args:
        str1: Primeiro número como string
        str2: Segundo número como string
        
    Returns:
        Soma dos números como string
        
    Example:
        >>> add_strings("123", "456")
        '579'
        >>> add_strings("999", "1")
        '1000'
    """
    # Garantir que str2 seja o número maior
    if len(str1) > len(str2):
        str1, str2 = str2, str1
    
    # Preencher str1 com zeros à esquerda
    str1 = str1.zfill(len(str2))
    
    result = []
    carry = 0
    
    # Somar dígito por dígito da direita para a esquerda
    for i in range(len(str2) - 1, -1, -1):
        digit_sum = int(str1[i]) + int(str2[i]) + carry
        carry = digit_sum // 10
        result.append(str(digit_sum % 10))
    
    # Adicionar carry final se houver
    if carry:
        result.append(str(carry))
    
    return ''.join(reversed(result))


def subtract_strings(str1: str, str2: str) -> str:
    """
    Subtrai dois números representados como strings.
    Assume que str1 >= str2.
    
    Args:
        str1: Minuendo como string
        str2: Subtraendo como string
        
    Returns:
        Diferença como string
        
    Example:
        >>> subtract_strings("456", "123")
        '333'
        >>> subtract_strings("1000", "1")
        '999'
    """
    # Preencher str2 com zeros à esquerda
    str2 = str2.zfill(len(str1))
    
    result = []
    borrow = 0
    
    # Subtrair dígito por dígito da direita para a esquerda
    for i in range(len(str1) - 1, -1, -1):
        digit1 = int(str1[i])
        digit2 = int(str2[i])
        
        # Aplicar borrow se necessário
        if borrow:
            digit1 -= 1
            borrow = 0
        
        # Calcular diferença
        if digit1 < digit2:
            digit1 += 10
            borrow = 1
        
        result.append(str(digit1 - digit2))
    
    # Remover zeros à esquerda
    result_str = ''.join(reversed(result))
    return result_str.lstrip('0') or '0'


def remove_leading_zeros(s: str) -> str:
    """
    Remove zeros à esquerda de uma string, mantendo pelo menos um zero.
    
    Args:
        s: String numérica
        
    Returns:
        String sem zeros à esquerda desnecessários
        
    Example:
        >>> remove_leading_zeros("00123")
        '123'
        >>> remove_leading_zeros("000")
        '0'
    """
    i = 0
    while i < len(s):
        if s[i] != "0":
            break
        else:
            i += 1
    result = s[i:]
    return result if result else "0"            


def karatsuba_multiply(a: str, b: str) -> str:
    """
    Multiplica dois números inteiros grandes usando o algoritmo de Karatsuba.
    
    O algoritmo usa a identidade:
    (10^m * a + b) * (10^m * c + d) = 10^(2m) * ac + 10^m * (ad + bc) + bd
    
    E a otimização de Karatsuba:
    ad + bc = (a + b) * (c + d) - ac - bd
    
    Isso reduz de 4 para 3 multiplicações recursivas.
    
    Args:
        a: Primeiro número como string
        b: Segundo número como string
        
    Returns:
        Produto dos números como string
        
    Example:
        >>> karatsuba_multiply("1234", "5678")
        '7006652'
        >>> karatsuba_multiply("999", "999")
        '998001'
    """
    # Remover zeros à esquerda
    a = remove_leading_zeros(a)
    b = remove_leading_zeros(b)
    
    # Casos base
    if len(a) == 1 and len(b) == 1:
        return str(int(a) * int(b))
    
    # Garantir que ambos tenham o mesmo comprimento e seja par
    max_len = max(len(a), len(b))
    if max_len % 2 == 1:
        max_len += 1
    
    # Preencher com zeros à esquerda
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    # Dividir os números ao meio
    mid = max_len // 2
    
    a_left, a_right = a[:mid], a[mid:]
    b_left, b_right = b[:mid], b[mid:]
    
    # As três multiplicações recursivas de Karatsuba
    z0 = karatsuba_multiply(a_right, b_right)  # bd
    z2 = karatsuba_multiply(a_left, b_left)    # ac
    z1 = karatsuba_multiply(
        add_strings(a_left, a_right), 
        add_strings(b_left, b_right)
    )  # (a+b)(c+d)
    
    # Calcular ad + bc usando a identidade de Karatsuba
    z1 = subtract_strings(z1, z0)  # (a+b)(c+d) - bd
    z1 = subtract_strings(z1, z2)  # (a+b)(c+d) - bd - ac = ad + bc
    
    # Combinar os resultados: 10^(2m) * ac + 10^m * (ad + bc) + bd
    # Adicionar zeros à direita para multiplicação por potências de 10
    z2_padded = z2 + "0" * (2 * mid)  # 10^(2m) * ac
    z1_padded = z1 + "0" * mid        # 10^m * (ad + bc)
    
    result = add_strings(z2_padded, z1_padded)
    result = add_strings(result, z0)
    
    # Remover zeros à esquerda do resultado final
    return remove_leading_zeros(result)


def multiply_large_numbers(a: str, b: str) -> str:
    """
    Interface principal para multiplicação de números grandes.
    
    Args:
        a: Primeiro número como string
        b: Segundo número como string
        
    Returns:
        Produto dos números como string
        
    Example:
        >>> multiply_large_numbers("123456789", "987654321")
        '121932631112635269'
    """
    # Validar entrada
    if not a or not b:
        return "0"
    
    # Verificar se são números válidos
    if not a.isdigit() or not b.isdigit():
        raise ValueError("Entrada deve conter apenas dígitos")
    
    # Caso especial: multiplicação por zero
    if a == "0" or b == "0":
        return "0"
    
    return karatsuba_multiply(a, b) 