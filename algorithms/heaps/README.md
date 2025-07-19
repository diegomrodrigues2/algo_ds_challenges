# 🎯 Heap Data Structures and Applications

Este diretório contém implementações de **heaps** e suas aplicações avançadas em Python. As implementações avançadas são **esqueletos** para você praticar e implementar.

## 📚 Implementações Básicas (Completas)

### 1. **BinaryHeap** (`binary_heap.py`)
- **Min-heap** binário implementado do zero
- Operações: `insert`, `extract_min`, `peek`, `size`
- Complexidade: O(log n) para inserção e remoção

### 2. **K Largest Elements** (`k_largest_elements.py`)
- Encontra os **k maiores** elementos de um array
- Usa min-heap para manter k elementos
- Complexidade: O(n log k)

## 🚀 Aplicações Avançadas (Para Implementar)

### 3. **Heap Sort** (`heap_sort.py`) ⚠️ **IMPLEMENTAR**
- Algoritmo de ordenação usando heap
- Complexidade: O(n log n)
- Utilize a implementação `BinaryHeap`

### 4. **Median Finder** (`median_finder.py`) ⚠️ **IMPLEMENTAR**
- **Classe** que mantém a mediana de um stream de números
- Use **dois heaps**: max-heap (metade menor) e min-heap (metade maior)
- Operações: `add_num`, `find_median`
- Complexidade: O(log n) por operação

### 5. **Merge K Sorted Lists** (`merge_k_sorted_lists.py`) ⚠️ **IMPLEMENTAR**
- Combina **k listas ordenadas** em uma única lista ordenada
- Use min-heap para selecionar o menor elemento entre as listas
- Complexidade: O(n log k) onde n é o total de elementos

### 6. **Top K Frequent Elements** (`top_k_frequent.py`) ⚠️ **IMPLEMENTAR**
- Encontra os **k elementos mais frequentes** em um array
- Duas implementações:
  - **Heap-based**: O(n log k)
  - **Bucket sort**: O(n) para casos específicos

### 7. **Priority Queue** (`priority_queue.py`) ⚠️ **IMPLEMENTAR**
- **Fila de prioridade** genérica com suporte a desempate
- Use contador para garantir ordem FIFO em prioridades iguais
- Operações: `push`, `pop`, `peek`, `peek_priority`, `size`, `is_empty`, `clear`

### 8. **Sliding Window Median** (`sliding_window_median.py`) ⚠️ **IMPLEMENTAR**
- Encontra a **mediana** de cada janela deslizante de tamanho k
- Use dois heaps com remoção eficiente
- Complexidade: O(n log k) onde n é o tamanho do array

## 🧪 Testes

Cada implementação possui testes abrangentes que **falharão** até você implementar as funções:

```bash
# Executar todos os testes de heaps
pytest algorithms/heaps/ -v

# Executar testes específicos
pytest algorithms/heaps/test_median_finder.py -v
pytest algorithms/heaps/test_merge_k_sorted_lists.py -v
```

## 📊 Complexidades Esperadas

| Algoritmo | Tempo | Espaço | Status |
|-----------|-------|--------|--------|
| BinaryHeap | O(log n) | O(n) | ✅ Completo |
| K Largest | O(n log k) | O(k) | ✅ Completo |
| Heap Sort | O(n log n) | O(n) | ⚠️ Implementar |
| Median Finder | O(log n) | O(n) | ⚠️ Implementar |
| Merge K Lists | O(n log k) | O(k) | ⚠️ Implementar |
| Top K Frequent | O(n log k) | O(n) | ⚠️ Implementar |
| Priority Queue | O(log n) | O(n) | ⚠️ Implementar |
| Sliding Window Median | O(n log k) | O(k) | ⚠️ Implementar |

## 🎯 Dicas de Implementação

### **Median Finder**
```python
# Use dois heaps:
# - max_heap (valores negativos): metade menor dos números
# - min_heap: metade maior dos números
# Mediana = raiz do max-heap (ímpar) ou média das raízes (par)
```

### **Merge K Sorted Lists**
```python
# Use min-heap com tuplas: (valor, índice_da_lista, índice_do_elemento)
# Sempre insira o próximo elemento da lista que teve o elemento removido
```

### **Top K Frequent**
```python
# Opção 1: Min-heap para manter k mais frequentes
# Opção 2: Bucket sort por frequência (mais eficiente)
```

### **Priority Queue**
```python
# Use tuplas: (prioridade, contador, item)
# Contador garante ordem FIFO para prioridades iguais
```

### **Sliding Window Median**
```python
# Use dois heaps como Median Finder
# Implemente remoção eficiente de elementos antigos
# Rebalanceie os heaps após cada remoção
```

## 🔧 Dependências

- **Python 3.7+** (para type hints)
- **heapq** (biblioteca padrão)
- **collections.Counter** (biblioteca padrão)
- **pytest** (para testes)

## 📝 Estrutura dos Arquivos

Cada arquivo de implementação contém:
- **Docstrings** explicando o problema
- **Type hints** para parâmetros e retornos
- **`raise NotImplementedError("Implementar esta função")`** onde você deve implementar

Cada arquivo de teste contém:
- **Casos básicos** e **edge cases**
- **Testes abrangentes** para validar sua implementação
- **Exemplos práticos** de uso

## 🎓 Conceitos para Aplicar

- **Estruturas de dados**: Heap, Priority Queue
- **Algoritmos**: Heap Sort, Two Pointers, Sliding Window
- **Otimização**: Manter apenas k elementos em heap
- **Balanceamento**: Dois heaps para mediana
- **Genéricos**: Priority Queue com type hints
- **Eficiência**: Remoção O(log n) de elementos específicos 