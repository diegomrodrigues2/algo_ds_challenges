# 🔴 Algoritmos de Red-Black Trees

## 🎯 Contexto Conceitual

Esta pasta contém implementações práticas de **Red-Black Trees**, estruturas permissivamente balanceadas que usam regras de cores para manter altura limitada, resultando em **menos rotações** e **modificações mais rápidas**.

### 📚 Integração com Notas

Para entender o **contexto conceitual** e **estratégias de implementação**, consulte:
- [📖 Notas sobre AVL vs Red-Black](../../notes/01.%20Data%20Structures/03.%20AVL%20vs%20Red-Black%20Trees/)

## 🚀 Desafios de Implementação

### 🔴 Operações Red-Black Fundamentais

#### `insert_red_black.py` - Inserção com Balanceamento Red-Black
**Objetivo:** Inserir valor mantendo propriedades Red-Black através de regras de cores.

**Estratégia:**
- Inserção BST padrão
- Colorir nó como vermelho
- Corrigir propriedades Red-Black
- Aplicar rotações/recolorações se necessário

**Complexidade:** O(log n) - Altura logarítmica garantida

#### `is_valid_red_black.py` - Verificação de Propriedades Red-Black
**Objetivo:** Verificar se uma árvore satisfaz as propriedades Red-Black.

**Estratégia:**
- Verificar propriedade BST
- Verificar regras de cores
- Verificar altura de nós pretos

**Complexidade:** O(n) - Verificação completa da árvore

## 🔄 Casos de Inserção Red-Black

### 📊 **Caso 1: Tio Vermelho**
```
    P (preto)
   / \
  V   T (vermelho)
 / \
N   N

Solução: Recolorização (sem rotação)
```

### 📊 **Caso 2: Tio Preto - Triângulo**
```
    P (preto)
   /
  V (vermelho)
   \
    N (vermelho)

Solução: rotate_left(V) + rotate_right(P)
```

### 📊 **Caso 3: Tio Preto - Linha**
```
    P (preto)
   /
  V (vermelho)
 /
N (vermelho)

Solução: rotate_right(P) + recolorização
```

## 🧪 Execução dos Testes

### 🎯 Teste Individual
```bash
# Testar inserção Red-Black
pytest algorithms/red_black_trees/test_insert_red_black.py -v

# Testar verificação Red-Black
pytest algorithms/red_black_trees/test_is_valid_red_black.py -v
```

### 🎯 Teste Completo
```bash
# Todos os testes de Red-Black
pytest algorithms/red_black_trees/ -v
```

## 📊 Estrutura de Dados

### 🎯 RBNode Red-Black
```python
class RBNode:
    def __init__(self, value: int, color: str = RED):
        self.value = value
        self.color = color  # RED ou BLACK
        self.left = None
        self.right = None
        self.parent = None  # Necessário para navegação
```

## 🔗 Conexões Conceituais

### 🔴 **Vantagens Red-Black**
| Aspecto | Vantagem | Impacto |
|---------|----------|---------|
| **Menos Rotações** | Máximo 3 por inserção | Modificações mais rápidas |
| **Implementação Robusta** | Menos casos especiais | Código mais simples |
| **Performance Consistente** | Altura limitada | Previsibilidade |

### ❌ **Desvantagens Red-Black**
| Aspecto | Desvantagem | Impacto |
|---------|-------------|---------|
| **Altura Maior** | h ≤ 2×log₂(n+1) | Busca ligeiramente mais lenta |
| **Complexidade Conceitual** | Regras de cores | Mais difícil de entender |
| **Overhead de Cores** | Campo adicional por nó | Uso de memória |

## 💡 Dicas de Implementação

### 🎯 Padrões Comuns
1. **Inserção como vermelho:** Sempre inserir como vermelho primeiro
2. **Correção de propriedades:** Verificar e corrigir após inserção
3. **Navegação com parent:** Usar ponteiros parent para navegação
4. **Recoloração vs rotação:** Preferir recolorização quando possível

### 🔍 Debugging
1. **Desenhe a árvore** com cores antes e depois das operações
2. **Verifique regras de cores** em cada nó
3. **Teste com sequências ordenadas** (pior caso)
4. **Confirme altura de pretos** após cada inserção

## 🚀 Aplicações Práticas

### 🔴 **Write-Heavy Applications**
```python
# Agendador de tarefas com modificações frequentes
class RedBlackScheduler:
    def __init__(self):
        self.root = None
    
    def add_task(self, priority, task):
        # Inserção rápida - O(log n)
        self.root = insert_red_black(self.root, priority)
    
    def remove_task(self, priority):
        # Remoção rápida - O(log n)
        self.root = delete_red_black(self.root, priority)
```

### 📊 **Performance em Cenários Reais**
```python
# Benchmark: Inserção de 1000 elementos
def benchmark_insertion():
    # Construir árvore Red-Black
    root = None
    start = time.time()
    for i in range(1000):
        root = insert_red_black(root, i)
    insertion_time = time.time() - start
    
    return insertion_time

# Resultado típico: ~0.12 segundos (mais rápido que AVL)
```

## 🔗 Comparação com AVL Trees

### ⚖️ **Trade-offs Fundamentais**
| Aspecto | Red-Black Trees | AVL Trees |
|---------|-----------------|-----------|
| **Altura** | ⚠️ Limitada | ✅ Mínima |
| **Rotações** | ✅ Menos frequentes | ❌ Frequentes |
| **Busca** | ⚠️ Ligeiramente mais lenta | ✅ Mais rápida |
| **Inserção** | ✅ Mais rápida | ❌ Mais lenta |

### 🎯 **Escolha de Arquitetura**
- **Red-Black Trees:** Para aplicações **write-heavy**
- **AVL Trees:** Para aplicações **read-heavy**

## 🔗 Implementação nas Bibliotecas

### 📚 **Uso Real**
| Biblioteca | Implementação | Razão |
|------------|---------------|-------|
| **C++ std::map** | Red-Black Trees | Write-heavy |
| **Java TreeMap** | Red-Black Trees | Write-heavy |
| **Python sortedcontainers** | Red-Black Trees | Write-heavy |

### 🎯 **Por que Red-Black nas Bibliotecas?**
1. **Menos rotações** = melhor performance geral
2. **Implementação robusta** = menos bugs
3. **Carga de trabalho típica** = write-heavy

## 💡 Insights Fundamentais

### 🎯 1. Balanceamento Flexível
Red-Black Trees permitem **maior desbalanceamento** que AVL, mas mantêm altura logarítmica.

### 🔄 2. Menos Rotações
**Regras de cores inteligentes** reduzem a necessidade de rotações.

### ⚡ 3. Performance de Modificação
**Menos rotações** se traduz em **modificações mais rápidas**.

### 🎯 4. Trade-off Elegante
**Busca moderada** vs **modificação rápida** - escolha para write-heavy.

## 🚀 Próximos Passos

Após dominar estas implementações:
1. **CFS Scheduler Simulation** - Aplicação real no kernel Linux
2. **AVL Trees** - Alternativa com altura mínima
3. **Splay Trees** - Otimização baseada em acesso
4. **B-Trees** - Otimização para disco
5. **Comparação de Performance** - Testes com cargas reais

**Lição:** Red-Black Trees são a **escolha flexível** para aplicações **write-heavy** onde **performance de modificação** é crítica! 