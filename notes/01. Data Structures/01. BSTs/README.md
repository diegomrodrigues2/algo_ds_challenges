# 🌳 Binary Search Trees (BSTs) - Índice

## 📚 Visão Geral

Esta pasta contém **resumos didáticos** sobre Binary Search Trees, organizados por tópicos específicos.


## 📖 Estrutura dos Resumos

### 🎯 [01. Binary Search Tree.md](./01.%20Binary%20Search%20Tree.md)
**Conceitos Fundamentais**
- O que é uma BST
- Propriedades fundamentais
- Complexidade das operações
- Tipos de árvores balanceadas
- Aplicações práticas

### 🔍 [02. Operações Básicas.md](./02.%20Operações%20Básicas.md)
**Busca, Inserção e Remoção**
- Algoritmos de busca (recursivo e iterativo)
- Estratégias de inserção
- Os três casos de remoção
- Implementações iterativas

### 🌳 [03. Traversal de Árvores.md](./03.%20Traversal%20de%20Árvores.md)
**Percursos em Árvores**
- Pre-order, In-order, Post-order, Level-order
- Implementações iterativas
- Aplicações específicas

### ✅ [04. Validação e Propriedades.md](./04.%20Validação%20e%20Propriedades.md)
**Validação e Verificação**
- Propriedade fundamental da BST
- Algoritmos de validação
- Otimizações e variações

### 🚀 [05. Operações Avançadas.md](./05.%20Operações%20Avançadas.md)
**Funcionalidades Avançadas**
- Lowest Common Ancestor (LCA)
- Cálculo de altura, mínimo e máximo
- Contagem de nós, balanceamento
- Sucessor e predecessor


## 🎯 Problemas Relacionados

Baseado na análise dos arquivos em `algorithms/arvores_binarias/`:

### 🔍 **Busca e Validação**
- `search_bst.py` → [02. Operações Básicas](./02.%20Operações%20Básicas.md)
- `is_valid_bst.py` → [04. Validação e Propriedades](./04.%20Validação%20e%20Propriedades.md)

### 🗑️ **Remoção**
- `delete_bst_node.py` → [02. Operações Básicas](./02.%20Operações%20Básicas.md)

### 🌳 **Traversals**
- `pre_ordem.py`, `in_ordem.py`, `pos_ordem.py`, `nivel_ordem.py` → [03. Traversal de Árvores](./03.%20Traversal%20de%20Árvores.md)

### 🚀 **Operações Avançadas**
- `lowest_common_ancestor.py`, `tree_height.py`, `tree_min_max.py`, `count_nodes.py`, `balance_bst.py` → [05. Operações Avançadas](./05.%20Operações%20Avançadas.md)


## 🎯 Conceitos-Chave

### 🌟 **Propriedade Fundamental**
```
Para qualquer nó N:
- Subárvore esquerda: todos os valores < N.value
- Subárvore direita: todos os valores > N.value
```

### ⚡ **Complexidade**
| Operação | Melhor Caso | Caso Médio | Pior Caso |
|----------|-------------|------------|-----------|
| Busca | O(1) | O(log n) | O(n) |
| Inserção | O(1) | O(log n) | O(n) |
| Remoção | O(1) | O(log n) | O(n) |

### 🔄 **Traversals Importantes**
- **In-order**: Sempre retorna elementos ordenados
- **Pre-order**: Útil para serialização
- **Post-order**: Ideal para deleção
- **Level-order**: BFS, útil para visualização


## 💡 Dicas de Estudo

### 🎓 **Ordem Recomendada**
1. **Conceitos básicos** → [01. Binary Search Tree](./01.%20Binary%20Search%20Tree.md)
2. **Operações fundamentais** → [02. Operações Básicas](./02.%20Operações%20Básicas.md)
3. **Como percorrer** → [03. Traversal de Árvores](./03.%20Traversal%20de%20Árvores.md)
4. **Como validar** → [04. Validação e Propriedades](./04.%20Validação%20e%20Propriedades.md)
5. **Funcionalidades extras** → [05. Operações Avançadas](./05.%20Operações%20Avançadas.md)

### 🔍 **Para Prática**
1. **Implemente cada operação** do zero
2. **Desenhe as árvores** antes e depois das operações
3. **Teste com casos extremos** (árvore vazia, nó único, etc.)
4. **Compare implementações** recursivas e iterativas


## 🎯 Próximos Passos

### 📚 **Tópicos Relacionados**
- **Árvores AVL**: Balanceamento automático
- **Red-Black Trees**: Árvores balanceadas eficientes
- **B-Trees**: Para dados que não cabem na memória
- **Splay Trees**: Auto-organização baseada no uso

### 🔧 **Implementações Práticas**
- **Dicionários ordenados**: Usando BSTs
- **Filas de prioridade**: Com operações de busca
- **Sistemas de cache**: Com expiração baseada em tempo
- **Bancos de dados**: Índices em árvores


*💡 **Dica**: BSTs são uma das estruturas de dados mais importantes em Ciência da Computação. Dominar esses conceitos abrirá portas para entender estruturas mais complexas e algoritmos avançados!* 