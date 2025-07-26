# 🌳 Algoritmos de Árvores Binárias

## 🎯 Contexto Conceitual

Esta pasta contém implementações práticas de algoritmos para **Binary Search Trees (BSTs)**, a estrutura ancestral de todas as árvores balanceadas modernas.

### 📚 Integração com Notas

Para entender o **contexto conceitual** e **estratégias de implementação**, consulte:
- [📖 Notas sobre BSTs](../../notes/01.%20Data%20Structures/01.%20BSTs/)

## 🚀 Desafios de Implementação

### 🔍 Operações Fundamentais

#### `search_bst.py` - Busca Eficiente
**Objetivo:** Implementar busca que aproveita a propriedade BST para eliminar metade da árvore a cada comparação.

**Estratégia:**
- Compare com raiz atual
- Elimine subárvore apropriada
- Recursão na subárvore restante

**Complexidade:** O(log n) no caso médio, O(n) no pior caso

#### `tree_min_max.py` - Extremidades da Árvore
**Objetivo:** Encontrar o menor e maior valor na BST.

**Estratégia:**
- **Mínimo:** Siga sempre à esquerda
- **Máximo:** Siga sempre à direita

**Complexidade:** O(h) onde h = altura da árvore

### 🌳 Traversals (Percursos)

#### `pre_ordem.py` - Pré-ordem
**Padrão:** Raiz → Esquerda → Direita
**Aplicação:** Serialização de árvores

#### `in_ordem.py` - Em-ordem
**Padrão:** Esquerda → Raiz → Direita
**Aplicação:** Retorna elementos ordenados

#### `pos_ordem.py` - Pós-ordem
**Padrão:** Esquerda → Direita → Raiz
**Aplicação:** Deleção segura de árvores

#### `nivel_ordem.py` - Por Nível
**Padrão:** BFS (Breadth-First Search)
**Aplicação:** Visualização e análise por camadas

### ✅ Validação e Propriedades

#### `is_valid_bst.py` - Validação de BST
**Objetivo:** Verificar se uma árvore binária satisfaz a propriedade BST.

**Estratégia:** Verificar limites recursivamente

#### `count_nodes.py` - Contagem de Nós
**Objetivo:** Contar total de nós na árvore.

### 🗑️ Operações de Modificação

#### `delete_bst_node.py` - Remoção de Nós
**Objetivo:** Remover nó mantendo propriedade BST.

**Casos:**
1. Nó folha → Remoção direta
2. Nó com um filho → Substituição
3. Nó com dois filhos → Sucessor in-order

### 🚀 Operações Avançadas

#### `lowest_common_ancestor.py` - Ancestral Comum
**Objetivo:** Encontrar o ancestral comum mais baixo de dois nós.

#### `tree_height.py` - Altura da Árvore
**Objetivo:** Calcular altura máxima da árvore.

#### `balance_bst.py` - Balanceamento
**Objetivo:** Converter BST desbalanceada em balanceada.

## 🧪 Execução dos Testes

### 🎯 Teste Individual
```bash
# Testar busca BST
pytest algorithms/arvores_binarias/test_search_bst.py -v

# Testar min/max
pytest algorithms/arvores_binarias/test_tree_min_max.py -v
```

### 🎯 Teste Completo
```bash
# Todos os testes de árvores binárias
pytest algorithms/arvores_binarias/ -v
```

## 📊 Estrutura de Dados

### 🎯 TreeNode
```python
class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
```

## 🔗 Conexões Conceituais

### 🌳 Evolução das Árvores
```
BST Simples → AVL Trees → Red-Black Trees → B-Trees
```

### ⚖️ Trade-offs
| Aspecto | BST Simples | Árvores Balanceadas |
|---------|-------------|-------------------|
| **Implementação** | 🎯 Simples | 🔧 Complexa |
| **Performance** | ⚠️ O(n) pior caso | ✅ O(log n) garantido |
| **Manutenção** | 🔄 Manual | 🤖 Automática |

## 💡 Dicas de Implementação

### 🎯 Padrões Comuns
1. **Recursão vs Iteração:** Use recursão para clareza, iteração para eficiência
2. **Casos Base:** Sempre trate árvore vazia (None)
3. **Propriedade BST:** Mantenha a invariante em todas as operações

### 🔍 Debugging
1. **Desenhe a árvore** antes e depois das operações
2. **Teste casos extremos:** árvore vazia, nó único, lista ligada
3. **Verifique propriedade BST** após modificações

## 🚀 Próximos Passos

Após dominar estas implementações:
1. **Árvores AVL** - Balanceamento automático
2. **Red-Black Trees** - Estruturas robustas
3. **B-Trees** - Otimização para disco
4. **Splay Trees** - Auto-organização

**Lição:** A BST é a **base conceitual** que conecta todas as árvores balanceadas modernas. 