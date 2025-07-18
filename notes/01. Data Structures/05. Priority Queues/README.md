# 🎯 Priority Queues - Índice

## 📚 Visão Geral

Esta pasta contém **resumos didáticos** sobre Priority Queues (Filas de Prioridade), organizados por tópicos específicos.


## 📖 Estrutura dos Resumos

### 🎯 [01. Priority Queue.md](./01.%20Priority%20Queue.md)
**Conceitos Fundamentais**
- O que é uma Priority Queue
- Propriedades de prioridade
- Implementação com heap
- Complexidade das operações

### 🔄 [02. Operações Básicas.md](./02.%20Operações%20Básicas.md)
**Insert, Extract e Peek**
- Algoritmos de inserção
- Algoritmos de extração
- Operações de peek
- Verificação de estado
- Implementações iterativas

### 🔄 [03. Heap Sort.md](./03.%20Heap%20Sort.md)
**Ordenação com Heap**
- Algoritmo heap sort
- Build heap
- Heapify
- Complexidade e otimizações

### 🔧 [04. Aplicações Avançadas.md](./04.%20Aplicações%20Avançadas.md)
**Casos de Uso Específicos**
- K-ésimo menor elemento
- Merge de listas ordenadas
- Dijkstra's algorithm
- Sistemas de agendamento


## 🎯 Problemas Relacionados

Baseado na análise dos arquivos em `algorithms/priority_queues/`:

### 🎯 **Implementações Básicas**
- `min_priority_queue.py` → [02. Operações Básicas](./02.%20Operações%20Básicas.md)

### 🎯 **Algoritmos Avançados**
- `kth_smallest.py` → [04. Aplicações Avançadas](./04.%20Aplicações%20Avançadas.md)
- `merge_k_sorted_lists.py` → [04. Aplicações Avançadas](./04.%20Aplicações%20Avançadas.md)


## 🎯 Conceitos-Chave

### 🌟 **Propriedade Fundamental**
```
Priority Queue: Elementos com maior prioridade são removidos primeiro
- Min Priority Queue: Menor elemento tem maior prioridade
- Max Priority Queue: Maior elemento tem maior prioridade
```

### ⚡ **Complexidade**
| Operação | Complexidade | Explicação |
|----------|--------------|------------|
| Insert | O(log n) | Inserção com bubble-up |
| Extract Min/Max | O(log n) | Remoção com heapify |
| Peek Min/Max | O(1) | Acesso à raiz |
| Build Heap | O(n) | Heapify de baixo para cima |
| Heap Sort | O(n log n) | n extrações |

### 🎯 **Operações Principais**
- **📤 Insert**: Adiciona elemento mantendo propriedade
- **📥 Extract**: Remove elemento de maior prioridade
- **👀 Peek**: Visualiza elemento de maior prioridade
- **📏 Size**: Retorna número de elementos
- **🔍 Empty**: Verifica se está vazia

### 🎯 **Tipos de Priority Queue**
- **🎯 Min Priority Queue**: Menor elemento no topo
- **🎯 Max Priority Queue**: Maior elemento no topo
- **🎯 Custom Priority**: Prioridade baseada em função
- **🎯 Multi-level**: Múltiplas prioridades


## 💡 Dicas de Estudo

### 🎓 **Ordem Recomendada**
1. **Conceitos básicos** → [01. Priority Queue](./01.%20Priority%20Queue.md)
2. **Operações fundamentais** → [02. Operações Básicas](./02.%20Operações%20Básicas.md)
3. **Algoritmo de ordenação** → [03. Heap Sort](./03.%20Heap%20Sort.md)
4. **Aplicações práticas** → [04. Aplicações Avançadas](./04.%20Aplicações%20Avançadas.md)

### 🔍 **Para Prática**
1. **Desenhe o heap** antes e depois das operações
2. **Implemente bubble-up/down** separadamente
3. **Teste com casos extremos** (heap vazio, um elemento)
4. **Compare com outras estruturas** (BST, array ordenado)


## 🎯 Próximos Passos

### 📚 **Tópicos Relacionados**
- **Binary Heaps**: Implementação mais comum
- **Fibonacci Heaps**: Para algoritmos avançados
- **Binomial Heaps**: Estrutura alternativa
- **Pairing Heaps**: Implementação simples

### 🔧 **Implementações Práticas**
- **🎮 Game AI**: Pathfinding com A*
- **🌐 Networking**: Pacotes com prioridade
- **📊 Task Scheduler**: Processos com prioridade
- **🔧 Event Systems**: Eventos ordenados por tempo


*💡 **Dica**: Priority Queues são fundamentais para algoritmos de grafos e sistemas de agendamento. Dominar essas estruturas abrirá portas para entender algoritmos como Dijkstra, Prim, e sistemas de processamento em tempo real!* 