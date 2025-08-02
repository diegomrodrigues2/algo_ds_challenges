"""
Exemplo de Implementação Completa do Algoritmo de Karatsuba

Este arquivo contém uma implementação completa do algoritmo de Karatsuba
para fins de demonstração e referência. Não deve ser usado nos testes.
"""


def add_strings(str1: str, str2: str) -> str:
    """Adiciona dois números representados como strings."""
    if len(str1) > len(str2):
        str1, str2 = str2, str1
    
    str1 = str1.zfill(len(str2))
    result = []
    carry = 0
    
    for i in range(len(str2) - 1, -1, -1):
        digit_sum = int(str1[i]) + int(str2[i]) + carry
        carry = digit_sum // 10
        result.append(str(digit_sum % 10))
    
    if carry:
        result.append(str(carry))
    
    return ''.join(reversed(result))


def subtract_strings(str1: str, str2: str) -> str:
    """Subtrai dois números representados como strings."""
    str2 = str2.zfill(len(str1))
    result = []
    borrow = 0
    
    for i in range(len(str1) - 1, -1, -1):
        digit1 = int(str1[i])
        digit2 = int(str2[i])
        
        if borrow:
            digit1 -= 1
            borrow = 0
        
        if digit1 < digit2:
            digit1 += 10
            borrow = 1
        
        result.append(str(digit1 - digit2))
    
    result_str = ''.join(reversed(result))
    return result_str.lstrip('0') or '0'


def remove_leading_zeros(s: str) -> str:
    """Remove zeros à esquerda de uma string, mantendo pelo menos um zero."""
    return s.lstrip('0') or '0'


def karatsuba_multiply(a: str, b: str) -> str:
    """Implementação completa do algoritmo de Karatsuba."""
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
    
    # Extrair as partes esquerda e direita
    a_left = a[:mid]
    a_right = a[mid:]
    b_left = b[:mid]
    b_right = b[mid:]
    
    # Três multiplicações recursivas
    z0 = karatsuba_multiply(a_right, b_right)  # b * d
    z2 = karatsuba_multiply(a_left, b_left)    # a * c
    z1 = karatsuba_multiply(
        add_strings(a_left, a_right),           # (a + b)
        add_strings(b_left, b_right)            # (c + d)
    )
    z1 = subtract_strings(subtract_strings(z1, z0), z2)  # z1 - z0 - z2
    
    # Combinar os resultados
    # result = 10^(2*mid) * z2 + 10^mid * z1 + z0
    result = add_strings(
        add_strings(
            z2 + "0" * (2 * mid),  # 10^(2*mid) * z2
            z1 + "0" * mid          # 10^mid * z1
        ),
        z0                          # z0
    )
    
    return result


def multiply_large_numbers(a: str, b: str) -> str:
    """Interface principal para multiplicação de números grandes."""
    if not a or not b:
        return "0"
    
    if not a.isdigit() or not b.isdigit():
        raise ValueError("Entrada deve conter apenas dígitos")
    
    if a == "0" or b == "0":
        return "0"
    
    return karatsuba_multiply(a, b)


if __name__ == "__main__":
    # Exemplos de uso
    test_cases = [
        ("123", "456"),
        ("9999", "9999"),
        ("123456789", "987654321"),
        ("1000000", "1000000"),
    ]
    
    print("🚀 Testes do Algoritmo de Karatsuba\n")
    
    for a, b in test_cases:
        result = multiply_large_numbers(a, b)
        expected = str(int(a) * int(b))
        
        print(f"📊 {a} × {b}")
        print(f"   Resultado: {result}")
        print(f"   Esperado:  {expected}")
        print(f"   ✅ Correto: {result == expected}\n") 