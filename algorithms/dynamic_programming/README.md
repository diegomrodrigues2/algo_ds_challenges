# 🧠 Programação Dinâmica

Esta pasta contém implementações de algoritmos clássicos de programação dinâmica, demonstrando diferentes técnicas e padrões de otimização.

## 📁 Estrutura dos Arquivos

### 🔪 Rod Cutting (`rod_cutting.py`)
**Problema**: Maximizar o lucro ao cortar uma barra de comprimento `n` em pedaços menores.

**Funções a implementar**:
- `rod_cutting_recursive(prices, n)` - Solução recursiva
- `rod_cutting_dp(prices, n)` - Programação dinâmica com memoização
- `rod_cutting_bottom_up(prices, n)` - Abordagem bottom-up
- `rod_cutting_with_solution(prices, n)` - Retorna cortes ótimos

**Exemplo**:
```python
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
n = 4
# Solução: 2 + 2 = 5 + 5 = 10 (lucro máximo)
```

### 🎒 Knapsack (`knapsack.py`)
**Problema**: Selecionar itens com pesos e valores para maximizar valor total sem exceder capacidade.

**Funções a implementar**:
- `knapsack_recursive(weights, values, capacity)` - Solução recursiva
- `knapsack_dp(weights, values, capacity)` - Programação dinâmica
- `knapsack_01(weights, values, capacity)` - Mochila 0/1 (sem repetição)
- `knapsack_fractional(weights, values, capacity)` - Mochila fracionária
- `knapsack_with_items(weights, values, capacity)` - Retorna itens selecionados

**Exemplo**:
```python
weights = [1, 2, 3]
values = [10, 15, 20]
capacity = 4
# Solução: itens 1 e 2 (peso=3, valor=25)
```

### 📝 Longest Common Subsequence (`longest_common_subsequence.py`)
**Problema**: Encontrar a subsequência comum mais longa entre duas strings.

**Funções a implementar**:
- `lcs_recursive(str1, str2)` - Solução recursiva
- `lcs_dp(str1, str2)` - Programação dinâmica
- `lcs_with_string(str1, str2)` - Retorna a subsequência
- `lcs_three_strings(str1, str2, str3)` - LCS para três strings
- `lcs_palindrome(str1)` - Subsequência palíndroma mais longa

**Exemplo**:
```python
str1 = "ABCDGH"
str2 = "AEDFHR"
# LCS: "ADH" (comprimento 3)
```

### 🌳 Optimal Binary Search Tree (`optimal_binary_search_tree.py`)
**Problema**: Construir árvore binária de busca que minimize custo médio de busca.

**Funções a implementar**:
- `optimal_bst_basic(keys, probabilities)` - Solução básica
- `optimal_bst_with_tree(keys, probabilities)` - Retorna árvore ótima
- `optimal_bst_knuth_optimization(keys, probabilities)` - Otimização de Knuth
- `optimal_bst_space_optimized(keys, probabilities)` - Otimização de espaço

**Exemplo**:
```python
keys = [10, 20, 30, 40]
probabilities = [0.1, 0.3, 0.2, 0.4]
# Custo mínimo: 1.9 (árvore com 20 como raiz)
```

## 🧪 Execução dos Testes

Para executar todos os testes de programação dinâmica:
```bash
pytest algorithms/dynamic_programming/
```

Para executar testes específicos:
```bash
# Apenas rod cutting
pytest algorithms/dynamic_programming/test_rod_cutting.py

# Apenas knapsack
pytest algorithms/dynamic_programming/test_knapsack.py

# Apenas LCS
pytest algorithms/dynamic_programming/test_longest_common_subsequence.py
```

## 🎯 Conceitos Aprendidos

### 📊 Padrões de Programação Dinâmica
- **Subestrutura Ótima**: Solução ótima contém soluções ótimas dos subproblemas
- **Subproblemas Sobrepostos**: Mesmos subproblemas aparecem múltiplas vezes
- **Memoização**: Armazenar resultados para evitar recálculos

### 🔄 Estratégias de Implementação
- **Top-Down**: Recursiva com memoização
- **Bottom-Up**: Iterativa com tabela de resultados
- **Reconstrução**: Rastrear escolhas para reconstruir solução

### ⚡ Otimizações
- **Espaço**: Reduzir uso de memória (apenas últimas linhas/colunas)
- **Tempo**: Early termination em condições específicas
- **Cache**: Estruturas eficientes para memoização

## 📚 Recursos Adicionais

- **Notas Teóricas**: `notes/03. Algoritmos de Programação Dinâmica/`
- **Exemplos Práticos**: Cada arquivo contém exemplos comentados
- **Casos de Teste**: Cobertura abrangente incluindo casos extremos 