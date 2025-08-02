# 🔄 Queues - Índice

## 📚 Visão Geral

Esta pasta contém **resumos didáticos** sobre Queues (Filas), organizados por tópicos específicos.


## 📖 Estrutura dos Resumos

### 🎯 [01. Queue.md](./01.%20Queue.md)
**Conceitos Fundamentais**
- O que é uma Queue
- Propriedades FIFO
- Operações básicas
- Implementação com array
- Complexidade das operações

### 🔄 [02. Operações Básicas.md](./02.%20Operações%20Básicas.md)
**Enqueue, Dequeue e Acesso**
- Algoritmos de inserção (enqueue)
- Algoritmos de remoção (dequeue)
- Operações de peek/front
- Verificação de estado (empty, size)
- Implementações iterativas

### 🔄 [03. Implementações Especializadas.md](./03.%20Implementações%20Especializadas.md)
**Circular Queue e Queue com Stacks**
- Circular Queue (capacidade fixa)
- Queue implementada com duas stacks
- Deque (double-ended queue)
- Implementações otimizadas

### 🔧 [04. Aplicações Avançadas.md](./04.%20Aplicações%20Avançadas.md)
**Casos de Uso Específicos**
- Breadth-First Search (BFS)
- Sistemas de agendamento
- Buffer de processamento
- Simulação de eventos


## 🎯 Problemas Relacionados

Baseado na análise dos arquivos em `algorithms/queues/`:

### 🔄 **Implementações Básicas**
- `simple_queue.py` → [02. Operações Básicas](./02.%20Operações%20Básicas.md)

### 🔄 **Implementações Especializadas**
- `circular_queue.py` → [03. Implementações Especializadas](./03.%20Implementações%20Especializadas.md)
- `queue_two_stacks.py` → [03. Implementações Especializadas](./03.%20Implementações%20Especializadas.md)


## 🎯 Conceitos-Chave

### 🌟 **Propriedade Fundamental**
```
FIFO: First In, First Out
- Primeiro elemento inserido é o primeiro a ser removido
- Como uma fila de pessoas ou carros
```

### ⚡ **Complexidade**
| Operação | Complexidade | Explicação |
|----------|--------------|------------|
| Enqueue | O(1) | Inserção no final |
| Dequeue | O(1) | Remoção do início |
| Peek/Front | O(1) | Acesso ao primeiro |
| Empty | O(1) | Verificação de tamanho |
| Size | O(1) | Contador mantido |

### 🔄 **Operações Principais**
- **📤 Enqueue**: Adiciona elemento no final
- **📥 Dequeue**: Remove elemento do início
- **👀 Peek/Front**: Visualiza primeiro elemento
- **📏 Size**: Retorna número de elementos
- **🔍 Empty**: Verifica se está vazia

### 🎯 **Tipos de Queue**
- **🔄 Queue simples**: Operações básicas
- **🔄 Circular Queue**: Capacidade fixa
- **📦 Queue com stacks**: Implementação alternativa
- **🔄 Deque**: Inserção/remoção em ambas as extremidades


## 💡 Dicas de Estudo

### 🎓 **Ordem Recomendada**
1. **Conceitos básicos** → [01. Queue](./01.%20Queue.md)
2. **Operações fundamentais** → [02. Operações Básicas](./02.%20Operações%20Básicas.md)
3. **Implementações especiais** → [03. Implementações Especializadas](./03.%20Implementações%20Especializadas.md)
4. **Aplicações práticas** → [04. Aplicações Avançadas](./04.%20Aplicações%20Avançadas.md)

### 🔍 **Para Prática**
1. **Desenhe a fila** antes e depois das operações
2. **Implemente enqueue/dequeue** separadamente
3. **Teste com casos extremos** (fila vazia, um elemento)
4. **Compare com outras estruturas** (stack, deque)


## 🎯 Próximos Passos

### 📚 **Tópicos Relacionados**
- **Priority Queues**: Filas com prioridade
- **Deques**: Filas duplas
- **Circular Buffers**: Para streaming de dados
- **Message Queues**: Sistemas distribuídos

### 🔧 **Implementações Práticas**
- **🌐 Networking**: Pacotes de rede
- **🎮 Game Loops**: Processamento de eventos
- **📊 Print Spooler**: Impressão de documentos
- **🔧 Task Scheduler**: Sistemas operacionais


*💡 **Dica**: Queues são fundamentais para algoritmos de busca em largura e sistemas de processamento sequencial. Dominar essas estruturas abrirá portas para entender sistemas distribuídos e algoritmos de grafos!* 