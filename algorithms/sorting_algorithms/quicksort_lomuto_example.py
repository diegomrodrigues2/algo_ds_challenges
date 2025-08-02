"""
Exemplo Completo: Quicksort com Partição de Lomuto

Este arquivo contém uma implementação completa do Quicksort usando
partição de Lomuto para demonstrar como o algoritmo funciona.
"""


def lomuto_partition(arr, low, high):
    """
    Implementa a partição de Lomuto.
    
    A partição de Lomuto escolhe o último elemento como pivô e coloca todos os
    elementos menores à esquerda e maiores à direita.
    
    Args:
        arr: Lista a ser particionada
        low: Índice inicial do subarray
        high: Índice final do subarray (pivô)
    
    Returns:
        Índice da posição final do pivô
    """
    pivot = arr[high]  # 🎯 Escolhe o último elemento como pivô
    i = low - 1        # 📍 Índice para elementos menores
    
    # 🔄 Percorre o array de low até high-1
    for j in range(low, high):
        if arr[j] <= pivot:  # ✅ Elemento menor ou igual ao pivô
            i += 1            # 📈 Avança posição
            arr[i], arr[j] = arr[j], arr[i]  # 🔄 Troca elementos
    
    # 🎯 Coloca o pivô na posição final
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # 📍 Retorna a posição final do pivô


def quicksort_lomuto(arr, low=None, high=None):
    """
    Implementa o algoritmo Quicksort usando partição de Lomuto.
    
    O Quicksort é um algoritmo de ordenação divide-and-conquer que:
    1. Escolhe um pivô (neste caso, o último elemento)
    2. Particiona o array em torno do pivô
    3. Recursivamente ordena as duas metades
    
    Args:
        arr: Lista a ser ordenada
        low: Índice inicial (padrão: 0)
        high: Índice final (padrão: len(arr) - 1)
    
    Returns:
        Lista ordenada (modifica a lista original)
    """
    # Inicializar parâmetros se não fornecidos
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    
    # 🔄 Caso recursivo
    if low < high:
        # 🎯 Particiona o array e obtém a posição do pivô
        pivot_idx = lomuto_partition(arr, low, high)
        
        # ⬅️ Recursivamente ordena subarray à esquerda do pivô
        quicksort_lomuto(arr, low, pivot_idx - 1)
        
        # ➡️ Recursivamente ordena subarray à direita do pivô
        quicksort_lomuto(arr, pivot_idx + 1, high)
    
    return arr  # ✅ Retorna o array ordenado


def quicksort_lomuto_wrapper(arr):
    """
    Wrapper para facilitar o uso do Quicksort.
    
    Args:
        arr: Lista a ser ordenada
    
    Returns:
        Lista ordenada (modifica a lista original)
    """
    if not arr:
        return arr
    
    return quicksort_lomuto(arr.copy())


def print_partition_step(arr, low, high, pivot_idx, step_name=""):
    """Imprime o estado do array após uma partição (para debug)."""
    print(f"\n{step_name}")
    print(f"Array: {arr}")
    print(f"Pivô na posição {pivot_idx}: {arr[pivot_idx]}")
    print(f"Subarray esquerdo: {arr[low:pivot_idx]}")
    print(f"Subarray direito: {arr[pivot_idx+1:high+1]}")
    print("-" * 40)


def demonstrate_quicksort():
    """Demonstra o funcionamento do Quicksort passo a passo."""
    print("🚀 Demonstração do Quicksort com Partição de Lomuto")
    print("=" * 60)
    
    # Exemplo 1: Array simples
    arr1 = [3, 7, 8, 5, 2, 1, 9, 5, 4]
    print(f"\n📊 Exemplo 1: {arr1}")
    result1 = quicksort_lomuto_wrapper(arr1)
    print(f"✅ Resultado: {result1}")
    
    # Exemplo 2: Array já ordenado
    arr2 = [1, 2, 3, 4, 5]
    print(f"\n📊 Exemplo 2 (já ordenado): {arr2}")
    result2 = quicksort_lomuto_wrapper(arr2)
    print(f"✅ Resultado: {result2}")
    
    # Exemplo 3: Array em ordem reversa
    arr3 = [5, 4, 3, 2, 1]
    print(f"\n📊 Exemplo 3 (ordem reversa): {arr3}")
    result3 = quicksort_lomuto_wrapper(arr3)
    print(f"✅ Resultado: {result3}")
    
    # Exemplo 4: Array com duplicatas
    arr4 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"\n📊 Exemplo 4 (com duplicatas): {arr4}")
    result4 = quicksort_lomuto_wrapper(arr4)
    print(f"✅ Resultado: {result4}")
    
    # Exemplo 5: Array com números negativos
    arr5 = [-3, 1, -4, 1, -5, 9, -2, 6, -5, 3, -5]
    print(f"\n📊 Exemplo 5 (com negativos): {arr5}")
    result5 = quicksort_lomuto_wrapper(arr5)
    print(f"✅ Resultado: {result5}")


def demonstrate_partition():
    """Demonstra o funcionamento da partição de Lomuto."""
    print("\n🔧 Demonstração da Partição de Lomuto")
    print("=" * 60)
    
    # Exemplo de partição
    arr = [3, 7, 8, 5, 2, 1, 9, 5, 4]
    print(f"Array original: {arr}")
    
    # Primeira partição
    pivot_idx = lomuto_partition(arr, 0, len(arr) - 1)
    print_partition_step(arr, 0, len(arr) - 1, pivot_idx, "Primeira partição")
    
    # Segunda partição (esquerda)
    if pivot_idx > 0:
        pivot_idx_left = lomuto_partition(arr, 0, pivot_idx - 1)
        print_partition_step(arr, 0, pivot_idx - 1, pivot_idx_left, "Partição esquerda")


if __name__ == "__main__":
    # Executar demonstrações
    demonstrate_quicksort()
    demonstrate_partition()
    
    print("\n🎯 Análise de Complexidade:")
    print("📊 Tempo médio: O(n log n)")
    print("⚠️  Pior caso: O(n²)")
    print("💾 Espaço: O(log n)")
    print("🔄 Estabilidade: Não estável") 