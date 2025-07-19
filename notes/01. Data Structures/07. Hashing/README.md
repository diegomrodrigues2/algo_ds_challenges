# Hashing

## 📚 Visão Geral

Esta seção cobre os fundamentos teóricos e práticos de **hashing**, desde limites inferiores no modelo de comparação até implementações robustas com hashing universal.

## 🎯 Objetivos de Aprendizado

- Compreender o **limite inferior Ω(log n)** no modelo de comparação
- Implementar **direct access arrays** para operações O(1)
- Dominar **hashing universal** com garantias teóricas
- Comparar estratégias de **resolução de colisões**

## 📖 Conteúdo

### 1. [Comparison Model Lower Bound](01.%20Comparison%20Model%20Lower%20Bound.md)
- **Modelo de comparação**: Operações permitidas e restrições
- **Árvore de decisão**: Representação de algoritmos de busca
- **Limite inferior**: Prova de que Ω(log n) é necessário
- **Superação do limite**: Word RAM Model

### 2. [Direct Access Arrays](02.%20Direct%20Access%20Arrays.md)
- **Conceito básico**: Armazenamento direto por chave
- **Operações O(1)**: find, insert, delete
- **Limitações**: Espaço O(u) e chaves inteiras
- **Trade-offs**: Simplicidade vs eficiência de espaço

### 3. [Universal Hashing](03.%20Universal%20Hashing.md)
- **Família universal**: Definição matemática
- **Função universal**: h(k) = ((a·k + b) mod p) mod m
- **Análise de performance**: Comprimento esperado das cadeias
- **Implementação**: Tabela hash com hashing universal

### 4. [Chaining vs Open Addressing](04.%20Chaining%20vs%20Open%20Addressing.md)
- **Chaining**: Estruturas auxiliares para colisões
- **Open addressing**: Prospecção na própria tabela
- **Comparação**: Vantagens e desvantagens
- **Escolha da estratégia**: Contextos apropriados

## 🔧 Conceitos-Chave

### Modelos de Computação
```python
# Comparison Model
key1 < key2     # Apenas comparações
key1 == key2    # Não pode usar aritmética

# Word RAM Model
array[key]      # Acesso direto à memória
key % size      # Aritmética com chaves
```

### Função Hash Universal
```python
def universal_hash(key, a, b, p, m):
    return ((a * key + b) % p) % m

# Propriedade: Pr[h(k₁) = h(k₂)] ≤ 1/m
```

### Resolução de Colisões
```python
# Chaining
table[index] = [(key1, value1), (key2, value2)]

# Open Addressing
table[index] = (key, value)
# Prospecção: (index + i) % size
```

## 📊 Complexidade

| Estrutura | build | find | insert | delete | Espaço |
|-----------|-------|------|--------|--------|--------|
| **Direct Access** | O(n) | O(1) | O(1) | O(1) | O(u) |
| **Universal Hash** | O(n) | O(1) | O(1) | O(1) | O(n) |
| **Chaining** | O(n) | O(1) | O(1) | O(1) | O(n) |
| **Open Addressing** | O(n) | O(1) | O(1) | O(1) | O(n) |

## 🎯 Aplicações Práticas

### Casos de Uso
- **Dicionários**: Mapeamento chave-valor
- **Conjuntos**: Verificação de pertinência
- **Cache**: Acesso rápido a dados
- **Deduplicação**: Remoção de duplicatas

### Implementações Reais
- **Python dict**: Open addressing
- **Java HashMap**: Chaining
- **C++ unordered_map**: Chaining
- **Redis**: Hashing para estruturas de dados

## 🔍 Análise Teórica

### Limite Inferior
- **Modelo de comparação**: Ω(log n) necessário
- **Árvore de decisão**: n+1 folhas necessárias
- **Altura mínima**: ⌈log₂(n+1)⌉

### Hashing Universal
- **Distribuição uniforme**: Independente dos dados
- **Performance garantida**: O(1) esperado
- **Robustez**: Difícil de atacar

## 🚀 Próximos Passos

### Implementações Práticas
- [Direct Access Array](../algorithms/hashing/direct_access_array.py)
- [Universal Hash Table](../algorithms/hashing/universal_hash_table.py)
- [Chaining Hash Table](../algorithms/hashing/chaining_hash_table.py)
- [Open Addressing Hash Table](../algorithms/hashing/open_addressing_hash_table.py)

### Tópicos Relacionados
- **Árvores de busca**: Alternativa para dados ordenados
- **Tries**: Estruturas para strings
- **Bloom filters**: Aproximação para conjuntos grandes

---

**Anterior**: [Priority Queues](../05.%20Priority%20Queues/)  
**Próximo**: [Árvores de Busca](../08.%20Árvores%20de%20Busca/) 