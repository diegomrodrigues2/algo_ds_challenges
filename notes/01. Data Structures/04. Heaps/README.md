# 🗂️ Heaps - Índice

## 📚 Visão Geral

Esta pasta contém **resumos didáticos** sobre Heaps (Filas de Prioridade), organizados por tópicos específicos.


## 📖 Estrutura dos Resumos

### 🎯 [01. Binary Heap.md](./01.%20Binary%20Heap.md)
**Conceitos Fundamentais**
- O que é uma Binary Heap
- Propriedades fundamentais
- Min-heap vs Max-heap
- Representação em array
- Complexidade das operações

### 🔄 [02. Operações Básicas.md](./02.%20Operações%20Básicas.md)
**Inserção, Remoção e Manutenção**
- Algoritmos de inserção (bubble-up)
- Algoritmos de remoção (bubble-down)
- Heapify (construção da heap)
- Operações de peek e size

### 📊 [03. Heap Sort.md](./03.%20Heap%20Sort.md)
**Algoritmo de Ordenação**
- Conceito do heap sort
- Implementação in-place
- Análise de complexidade
- Comparação com outros algoritmos

### 🎯 [04. Aplicações Avançadas.md](./04.%20Aplicações%20Avançadas.md)
**Casos de Uso Específicos**
- K maiores/menores elementos
- Merge K sorted lists
- Median finder
- Top K frequent elements


## 🎯 Problemas Relacionados

Baseado na análise dos arquivos em `algorithms/heaps/`:

### 🔄 **Implementação Básica**
- `binary_heap.py` → [02. Operações Básicas](./02.%20Operações%20Básicas.md)

### 📊 **Ordenação**
- `heap_sort.py` → [03. Heap Sort](./03.%20Heap%20Sort.md)

### 🎯 **Aplicações**
- `k_largest_elements.py` → [04. Aplicações Avançadas](./04.%20Aplicações%20Avançadas.md)


## 🎯 Conceitos-Chave

### 🌟 **Propriedade Fundamental**
```
Para qualquer nó N:
- Min-heap: N ≤ filhos de N
- Max-heap: N ≥ filhos de N
```

### ⚡ **Complexidade**
| Operação | Complexidade | Explicação |
|----------|--------------|------------|
| Inserção | O(log n) | Bubble-up até a raiz |
| Remoção | O(log n) | Bubble-down até a folha |
| Peek | O(1) | Acesso direto à raiz |
| Heapify | O(n) | Construção bottom-up |

### 🔄 **Representação em Array**
```
Para índice i:
- Pai: (i-1) // 2
- Filho esquerdo: 2*i + 1
- Filho direito: 2*i + 2
```

### 🎯 **Tipos de Heap**
- **📉 Min-heap**: Menor elemento na raiz
- **📈 Max-heap**: Maior elemento na raiz
- **🌳 Binary heap**: Máximo 2 filhos por nó
- **🌿 Fibonacci heap**: Estrutura mais complexa


## 💡 Dicas de Estudo

### 🎓 **Ordem Recomendada**
1. **Conceitos básicos** → [01. Binary Heap](./01.%20Binary%20Heap.md)
2. **Operações fundamentais** → [02. Operações Básicas](./02.%20Operações%20Básicas.md)
3. **Algoritmo de ordenação** → [03. Heap Sort](./03.%20Heap%20Sort.md)
4. **Aplicações práticas** → [04. Aplicações Avançadas](./04.%20Aplicações%20Avançadas.md)

### 🔍 **Para Prática**
1. **Desenhe a árvore** antes e depois das operações
2. **Implemente bubble-up** e bubble-down separadamente
3. **Teste com arrays pequenos** para visualizar o processo
4. **Compare min-heap** e max-heap


## 🎯 Próximos Passos

### 📚 **Tópicos Relacionados**
- **Priority Queues**: Implementação com heaps
- **Fibonacci Heaps**: Estrutura mais eficiente
- **Binomial Heaps**: Estrutura alternativa
- **Leftist Heaps**: Heaps auto-balanceadas

### 🔧 **Implementações Práticas**
- **Schedulers**: Sistemas de agendamento
- **Dijkstra's algorithm**: Caminhos mais curtos
- **Huffman coding**: Compressão de dados
- **Event systems**: Processamento de eventos


*💡 **Dica**: Heaps são fundamentais para algoritmos de ordenação e filas de prioridade. Dominar essas estruturas abrirá portas para algoritmos avançados de grafos e processamento de dados!* 