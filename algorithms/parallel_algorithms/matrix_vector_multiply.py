"""
Multiplicação Matriz-Vetor Paralela
Implementação do algoritmo P-MAT-VEC usando modelo fork-join
"""

def p_mat_vec(A, x, y, n):
    """
    Multiplica matriz A (n×n) pelo vetor x (n) e armazena resultado em y.
    Versão paralela usando parallel for no loop externo.
    
    Args:
        A: Matriz n×n (lista de listas)
        x: Vetor de entrada (lista de n elementos)
        y: Vetor de saída (lista de n elementos, será modificado)
        n: Dimensão da matriz e vetores
    
    Exemplo:
        >>> A = [[1, 2], [3, 4]]
        >>> x = [5, 6]
        >>> y = [0, 0]
        >>> p_mat_vec(A, x, y, 2)
        >>> y
        [17, 39]
    """
    # TODO: Implementar parallel for
    # parallel for i = 1 to n:
    #     for j = 1 to n:
    #         y[i] = y[i] + A[i][j] * x[j]
    
    # Implementação serial temporária
    for i in range(n):
        for j in range(n):
            y[i] = y[i] + A[i][j] * x[j]


def p_mat_vec_wrong(A, x, y, n):
    """
    Versão INCORRETA da multiplicação matriz-vetor paralela.
    Demonstra race condition ao paralelizar ambos os loops.
    
    Args:
        A: Matriz n×n (lista de listas)
        x: Vetor de entrada (lista de n elementos)
        y: Vetor de saída (lista de n elementos, será modificado)
        n: Dimensão da matriz e vetores
    
    ⚠️ ATENÇÃO: Esta função tem race conditions e não é determinística!
    """
    # ❌ INCORRETO - Race condition!
    # parallel for i = 1 to n:
    #     parallel for j = 1 to n:
    #         y[i] = y[i] + A[i][j] * x[j]
    
    # Implementação serial para demonstração
    for i in range(n):
        for j in range(n):
            y[i] = y[i] + A[i][j] * x[j]


def serial_mat_vec(A, x, y, n):
    """
    Versão serial da multiplicação matriz-vetor para comparação.
    
    Args:
        A: Matriz n×n (lista de listas)
        x: Vetor de entrada (lista de n elementos)
        y: Vetor de saída (lista de n elementos, será modificado)
        n: Dimensão da matriz e vetores
    """
    for i in range(n):
        for j in range(n):
            y[i] = y[i] + A[i][j] * x[j]


def create_test_matrix(n, pattern="identity"):
    """
    Cria matriz de teste com diferentes padrões.
    
    Args:
        n: Dimensão da matriz
        pattern: Padrão da matriz ("identity", "ones", "sequential")
    
    Returns:
        Matriz n×n como lista de listas
    """
    if pattern == "identity":
        return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    elif pattern == "ones":
        return [[1 for j in range(n)] for i in range(n)]
    elif pattern == "sequential":
        return [[i * n + j + 1 for j in range(n)] for i in range(n)]
    else:
        raise ValueError(f"Padrão desconhecido: {pattern}")


def create_test_vector(n, pattern="ones"):
    """
    Cria vetor de teste com diferentes padrões.
    
    Args:
        n: Dimensão do vetor
        pattern: Padrão do vetor ("ones", "sequential", "alternating")
    
    Returns:
        Vetor como lista de n elementos
    """
    if pattern == "ones":
        return [1 for _ in range(n)]
    elif pattern == "sequential":
        return [i + 1 for i in range(n)]
    elif pattern == "alternating":
        return [1 if i % 2 == 0 else -1 for i in range(n)]
    else:
        raise ValueError(f"Padrão desconhecido: {pattern}")


def analyze_work_span(n):
    """
    Análise teórica de work e span para P-MAT-VEC.
    
    Args:
        n: Dimensão da matriz
    
    Returns:
        Dicionário com work, span e parallelism estimados
    """
    # Work: T₁(n) = Θ(n²) - mesmo que serial
    # Span: T₁(n) = Θ(log n) + Θ(n) = Θ(n)
    # Parallelism: T₁(n)/T₁(n) = Θ(n²)/Θ(n) = Θ(n)
    
    work = n * n
    span = n  # Dominado pelo loop interno
    parallelism = work / span if span > 0 else 0
    
    return {
        'work': work,
        'span': span,
        'parallelism': parallelism,
        'n': n
    }


def verify_result(A, x, y, n):
    """
    Verifica se o resultado da multiplicação está correto.
    
    Args:
        A: Matriz n×n
        x: Vetor de entrada
        y: Vetor de resultado
        n: Dimensão
    
    Returns:
        True se o resultado está correto, False caso contrário
    """
    expected = [0] * n
    serial_mat_vec(A, x, expected, n)
    
    for i in range(n):
        if abs(y[i] - expected[i]) > 1e-10:
            return False
    return True 