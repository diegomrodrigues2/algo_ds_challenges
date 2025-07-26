# 🔄 Tree Rotations - Mecânica do Auto-Balanceamento

## 📚 Visão Geral

Esta pasta contém **resumos didáticos** sobre rotações de árvores, as operações atômicas que fundamentam todas as árvores auto-balanceadas modernas.

## 🎯 Contexto Conceitual

As rotações são **operações atômicas** que permitem reestruturar uma árvore para reduzir sua altura, preservando a propriedade fundamental da BST. Elas são a **base mecânica** tanto para árvores AVL quanto para Red-Black Trees.

## 📖 Estrutura dos Resumos

### 🔄 [01. Mecânica Rotacional - Operações Atômicas.md](./01.%20Mecânica%20Rotacional%20-%20Operações%20Atômicas.md)
**Fundamentos das Rotações**
- O que são rotações e por que são necessárias
- Operações atômicas: rotate_left e rotate_right
- Preservação da propriedade BST
- Diagramas visuais com Mermaid

### 🎯 [02. Implementações Práticas - Rotações Básicas.md](./02.%20Implementações%20Práticas%20-%20Rotações%20Básicas.md)
**Guias de Implementação**
- Estratégias para `rotate_left.py`
- Algoritmos para `rotate_right.py`
- Pseudocódigo detalhado
- Casos de teste essenciais

### 🔗 [03. Conexões com Auto-Balanceamento.md](./03.%20Conexões%20com%20Auto-Balanceamento.md)
**Políticas de Balanceamento**
- Como AVL Trees usam rotações
- Como Red-Black Trees usam rotações
- Diferentes políticas, mesmas operações atômicas
- Trade-offs entre esquemas

## 🚀 Desafios de Implementação

### 🔄 **Operações Atômicas**
- `rotate_left.py` → [02. Implementações Práticas](./02.%20Implementações%20Práticas%20-%20Rotações%20Básicas.md)
- `rotate_right.py` → [02. Implementações Práticas](./02.%20Implementações%20Práticas%20-%20Rotações%20Básicas.md)

## 🎯 Conceitos-Chave

### 🌟 **Operações Atômicas**
```
Rotação = Reestruturação que preserva propriedade BST
```

### ⚡ **Complexidade**
| Operação | Complexidade | Explicação |
|----------|--------------|------------|
| **rotate_left()** | O(1) | Operação atômica |
| **rotate_right()** | O(1) | Operação atômica |

### 🔄 **Preservação de Propriedades**
- ✅ **Propriedade BST** mantida
- ✅ **Altura** pode ser reduzida
- ✅ **Estrutura hierárquica** reorganizada

## 💡 Dicas de Estudo

### 🎓 **Ordem Recomendada**
1. **Mecânica rotacional** → [01. Mecânica Rotacional](./01.%20Mecânica%20Rotacional%20-%20Operações%20Atômicas.md)
2. **Implementações práticas** → [02. Implementações Práticas](./02.%20Implementações%20Práticas%20-%20Rotações%20Básicas.md)
3. **Conexões conceituais** → [03. Conexões com Auto-Balanceamento](./03.%20Conexões%20com%20Auto-Balanceamento.md)

### 🔍 **Para Prática**
1. **Desenhe as árvores** antes e depois das rotações
2. **Identifique os nós** que mudam de posição
3. **Verifique a propriedade BST** após cada rotação
4. **Teste com casos extremos** (árvore vazia, nó único)

## 🎯 Próximos Passos

### 📚 **Tópicos Relacionados**
- **Árvores AVL**: Balanceamento baseado em altura
- **Red-Black Trees**: Balanceamento baseado em cores
- **Splay Trees**: Rotações para otimização de acesso
- **B-Trees**: Rotações em estruturas multi-filho

### 🔧 **Implementações Práticas**
- **Inserção AVL**: Quando e como aplicar rotações
- **Inserção Red-Black**: Políticas de rebalanceamento
- **Remoção**: Rotações para manter balanceamento
- **Casos especiais**: Rotações duplas e zig-zag

*💡 **Dica**: As rotações são as operações atômicas que transformam BSTs simples em estruturas auto-balanceadas robustas!* 