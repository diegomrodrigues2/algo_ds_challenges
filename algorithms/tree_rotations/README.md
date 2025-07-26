# 🔄 Algoritmos de Rotações de Árvores

## 🎯 Contexto Conceitual

Esta pasta contém implementações práticas das **operações atômicas fundamentais** que permitem reestruturar árvores binárias preservando a propriedade BST. As rotações são a **base mecânica** de todas as árvores auto-balanceadas.

### 📚 Integração com Notas

Para entender o **contexto conceitual** e **estratégias de implementação**, consulte:
- [📖 Notas sobre Rotações](../../notes/01.%20Data%20Structures/02.%20Tree%20Rotations/)

## 🚀 Desafios de Implementação

### 🔄 Operações Atômicas Fundamentais

#### `rotate_left.py` - Rotação à Esquerda
**Objetivo:** Reestruturar árvore reduzindo altura da subárvore direita.

**Estratégia:**
- Identificar novo nó raiz (filho direito)
- Reorganizar ponteiros
- Retornar nova raiz

**Complexidade:** O(1) - Operação atômica

#### `rotate_right.py` - Rotação à Direita
**Objetivo:** Reestruturar árvore reduzindo altura da subárvore esquerda.

**Estratégia:**
- Identificar novo nó raiz (filho esquerdo)
- Reorganizar ponteiros
- Retornar nova raiz

**Complexidade:** O(1) - Operação atômica

## 🔄 Visualização das Transformações

### Rotação à Esquerda
```
Antes:         Y           Depois:        X
              / \                        / \
             X   C                      A   Y
            / \                            / \
           A   B                          B   C
```

### Rotação à Direita
```
Antes:         Y           Depois:        X
              / \                        / \
             X   C                      A   Y
            / \                            / \
           A   B                          B   C
```

## 🧪 Execução dos Testes

### 🎯 Teste Individual
```bash
# Testar rotação à esquerda
pytest algorithms/tree_rotations/test_rotate_left.py -v

# Testar rotação à direita
pytest algorithms/tree_rotations/test_rotate_right.py -v
```

### 🎯 Teste Completo
```bash
# Todos os testes de rotações
pytest algorithms/tree_rotations/ -v
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

### 🌳 Base para Auto-Balanceamento
```
Rotações Atômicas → AVL Trees → Red-Black Trees → Splay Trees
```

### ⚖️ Preservação de Propriedades
| Propriedade | Status | Explicação |
|-------------|--------|------------|
| **BST** | ✅ Preservada | Invariante mantida |
| **Altura** | 🔄 Reduzida | Objetivo da rotação |
| **Estrutura** | 🔄 Reorganizada | Ponteiros modificados |

## 💡 Dicas de Implementação

### 🎯 Padrões Comuns
1. **Verificação de pré-condições:** Sempre verifique se o filho necessário existe
2. **Reorganização de ponteiros:** Mantenha a ordem correta das operações
3. **Retorno da nova raiz:** Sempre retorne o nó que se torna a nova raiz

### 🔍 Debugging
1. **Desenhe a árvore** antes e depois da rotação
2. **Identifique os nós** que mudam de posição
3. **Verifique a propriedade BST** após a rotação
4. **Teste com casos extremos** (árvore vazia, nó único)

## 🚀 Aplicações Práticas

### 🔄 **Redução de Altura**
```python
# Árvore desbalanceada
#   1
#    \
#     2
#      \
#       3
#        \
#         4

# Aplicar rotação à esquerda na raiz
root = rotate_left(root)

# Resultado:
#   2
#  / \
# 1   3
#      \
#       4
```

### 🔄 **Preparação para Auto-Balanceamento**
```python
# Árvore que precisa de balanceamento
#       8
#      /
#     3
#    /
#   1

# Aplicar rotação à direita
root = rotate_right(root)

# Resultado:
#   3
#  / \
# 1   8
```

## 🔗 Conexões com Outras Estruturas

### 🌟 **AVL Trees**
- **Uso:** Rotações baseadas em fator de balanceamento
- **Frequência:** Máximo 2 rotações por inserção
- **Objetivo:** Altura mínima garantida

### 🔴 **Red-Black Trees**
- **Uso:** Rotações + recolorização
- **Frequência:** Máximo 3 rotações por inserção
- **Objetivo:** Menos rotações que AVL

### 🎲 **Splay Trees**
- **Uso:** Rotações para otimização de acesso
- **Frequência:** O(log n) rotações por acesso
- **Objetivo:** Mover nó acessado para a raiz

## 💡 Insights Fundamentais

### 🎯 1. Operações Atômicas
Rotações são **indivisíveis** - ou acontecem completamente ou não acontecem.

### 🔄 2. Preservação de Propriedades
A propriedade BST é **invariante** - mantida antes e depois da rotação.

### ⚡ 3. Eficiência Local
Rotações afetam apenas **3 nós** - operação extremamente eficiente.

### 🎯 4. Universalidade
**Mesmas operações** usadas por diferentes esquemas de balanceamento.

## 🚀 Próximos Passos

Após dominar estas operações atômicas:
1. **Rotações Duplas** - Combinação de rotações simples
2. **AVL Trees** - Rotações baseadas em fator de balanceamento
3. **Red-Black Trees** - Rotações + recolorização
4. **Splay Trees** - Rotações para otimização de acesso

**Lição:** As rotações são as **operações atômicas** que transformam BSTs simples em estruturas auto-balanceadas robustas! 