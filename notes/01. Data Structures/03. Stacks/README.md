# 📦 Stacks - Índice

## 📚 Visão Geral

Esta pasta contém **resumos didáticos** sobre Stacks (Pilhas), organizados por tópicos específicos.


## 📖 Estrutura dos Resumos

### 🎯 [01. Stack.md](./01.%20Stack.md)
**Conceitos Fundamentais**
- O que é uma Stack
- Propriedades LIFO
- Operações básicas
- Implementação com array
- Complexidade das operações

### 🔄 [02. Operações Básicas.md](./02.%20Operações%20Básicas.md)
**Push, Pop e Acesso**
- Algoritmos de inserção (push)
- Algoritmos de remoção (pop)
- Operações de peek/top
- Verificação de estado (empty, size)
- Implementações iterativas

### 🎨 [03. Stacks Especializadas.md](./03.%20Stacks%20Especializadas.md)
**Min Stack, Max Stack e Variações**
- Min Stack (menor elemento em O(1))
- Max Stack (maior elemento em O(1))
- Min-Max Stack (ambos em O(1))
- Pair Stack (pares de valores)
- Implementações otimizadas

### 🔧 [04. Aplicações Avançadas.md](./04.%20Aplicações%20Avançadas.md)
**Casos de Uso Específicos**
- Validação de parênteses
- Avaliação de expressões pós-fixas
- Equal stacks (equalização de pilhas)
- Conversão de notações
- Algoritmos de backtracking


## 🎯 Problemas Relacionados

Baseado na análise dos arquivos em `algorithms/stacks/`:

### 🔄 **Implementações Básicas**
- `min_stack.py` → [03. Stacks Especializadas](./03.%20Stacks%20Especializadas.md)
- `min_max_stack.py` → [03. Stacks Especializadas](./03.%20Stacks%20Especializadas.md)
- `pair_stack.py` → [03. Stacks Especializadas](./03.%20Stacks%20Especializadas.md)

### 🔧 **Aplicações**
- `validate_parentheses.py` → [04. Aplicações Avançadas](./04.%20Aplicações%20Avançadas.md)
- `evaluate_postfix.py` → [04. Aplicações Avançadas](./04.%20Aplicações%20Avançadas.md)
- `equal_stacks.py` → [04. Aplicações Avançadas](./04.%20Aplicações%20Avançadas.md)


## 🎯 Conceitos-Chave

### 🌟 **Propriedade Fundamental**
```
LIFO: Last In, First Out
- Último elemento inserido é o primeiro a ser removido
- Como uma pilha de pratos ou livros
```

### ⚡ **Complexidade**
| Operação | Complexidade | Explicação |
|----------|--------------|------------|
| Push | O(1) | Inserção no final |
| Pop | O(1) | Remoção do final |
| Peek/Top | O(1) | Acesso ao último |
| Empty | O(1) | Verificação de tamanho |
| Size | O(1) | Contador mantido |

### 🔄 **Operações Principais**
- **📤 Push**: Adiciona elemento no topo
- **📥 Pop**: Remove elemento do topo
- **👀 Peek/Top**: Visualiza elemento do topo
- **📏 Size**: Retorna número de elementos
- **🔍 Empty**: Verifica se está vazia

### 🎯 **Tipos de Stack**
- **📦 Stack simples**: Operações básicas
- **📉 Min Stack**: Mantém menor elemento
- **📈 Max Stack**: Mantém maior elemento
- **📊 Min-Max Stack**: Ambos extremos
- **🔗 Pair Stack**: Pares de valores


## 💡 Dicas de Estudo

### 🎓 **Ordem Recomendada**
1. **Conceitos básicos** → [01. Stack](./01.%20Stack.md)
2. **Operações fundamentais** → [02. Operações Básicas](./02.%20Operações%20Básicas.md)
3. **Implementações especiais** → [03. Stacks Especializadas](./03.%20Stacks%20Especializadas.md)
4. **Aplicações práticas** → [04. Aplicações Avançadas](./04.%20Aplicações%20Avançadas.md)

### 🔍 **Para Prática**
1. **Desenhe a pilha** antes e depois das operações
2. **Implemente push/pop** separadamente
3. **Teste com casos extremos** (pilha vazia, um elemento)
4. **Compare com outras estruturas** (queue, deque)


## 🎯 Próximos Passos

### 📚 **Tópicos Relacionados**
- **Queues**: Estrutura FIFO
- **Deques**: Inserção/remoção em ambas as extremidades
- **Monotonic Stacks**: Para problemas de próximo maior/menor
- **Expression Parsing**: Análise de expressões matemáticas

### 🔧 **Implementações Práticas**
- **Call Stack**: Gerenciamento de funções
- **Undo/Redo**: Sistemas de desfazer
- **Browser History**: Navegação web
- **Expression Evaluation**: Calculadoras


*💡 **Dica**: Stacks são fundamentais para algoritmos de parsing e backtracking. Dominar essas estruturas abrirá portas para entender compiladores, interpretadores e algoritmos de busca!* 