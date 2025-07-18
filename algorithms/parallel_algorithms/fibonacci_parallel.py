"""
Algoritmo P-FIB: Cálculo de números de Fibonacci em paralelo
Usando modelo fork-join com spawn e sync
"""

def p_fib(n):
    """
    Calcula o n-ésimo número de Fibonacci usando paralelismo.
    
    Args:
        n: Índice do número de Fibonacci (n >= 0)
    
    Returns:
        O n-ésimo número de Fibonacci
    
    Exemplo:
        >>> p_fib(0)
        0
        >>> p_fib(1)
        1
        >>> p_fib(10)
        55
    """
    if n <= 1:
        return n
    
    # TODO: Implementar spawn para paralelismo
    # x = spawn p_fib(n-1)  # Executa em paralelo
    # y = p_fib(n-2)        # Continua executando
    # sync                  # Espera spawn terminar
    # return x + y
    
    # Implementação serial temporária
    x = p_fib(n-1)
    y = p_fib(n-2)
    return x + y


def serial_fib(n):
    """
    Versão serial do cálculo de Fibonacci para comparação.
    
    Args:
        n: Índice do número de Fibonacci (n >= 0)
    
    Returns:
        O n-ésimo número de Fibonacci
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def analyze_work_span(n):
    """
    Análise teórica de work e span para P-FIB(n).
    
    Args:
        n: Tamanho da entrada
    
    Returns:
        Dicionário com work, span e parallelism estimados
    """
    # Work: T₁(n) = Θ(φⁿ) onde φ = (1 + √5)/2 ≈ 1.618
    # Span: T₁(n) = Θ(n)
    # Parallelism: T₁(n)/T₁(n) = Θ(φⁿ/n)
    
    phi = (1 + 5**0.5) / 2
    work = phi**n
    span = n
    parallelism = work / span if span > 0 else 0
    
    return {
        'work': work,
        'span': span,
        'parallelism': parallelism,
        'phi': phi
    } 