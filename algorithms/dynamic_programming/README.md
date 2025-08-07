# Dynamic Programming Algorithms

Este módulo contém implementações de algoritmos de programação dinâmica, demonstrando diferentes técnicas como memoização, tabulação e reconstrução de soluções.

## Algoritmos Implementados

### 1. Rod Cutting (Corte de Barras)
- **Arquivo**: `rod_cutting.py`
- **Técnica**: Programação dinâmica bottom-up
- **Complexidade**: O(n²) tempo, O(n) espaço
- **Aplicação**: Otimização de corte de barras de metal

### 2. Knapsack Problem (Problema da Mochila)
- **Arquivo**: `knapsack.py`
- **Técnica**: Programação dinâmica 2D
- **Complexidade**: O(n·W) tempo, O(n·W) espaço
- **Aplicação**: Otimização de recursos com restrições

### 3. Longest Common Subsequence (LCS)
- **Arquivo**: `longest_common_subsequence.py`
- **Técnica**: Programação dinâmica com reconstrução
- **Complexidade**: O(m·n) tempo, O(m·n) espaço
- **Aplicação**: Análise de sequências biológicas, diff de arquivos

### 4. Optimal Binary Search Tree (BST Ótima)
- **Arquivo**: `optimal_binary_search_tree.py`
- **Técnica**: Programação dinâmica com otimização de Knuth
- **Complexidade**: O(n³) tempo, O(n²) espaço
- **Aplicação**: Construção de árvores de busca otimizadas

### 5. Subset Sum with Memoization (Soma de Subconjuntos)
- **Arquivo**: `subset_sum_memoization.py`
- **Técnica**: Memoização (top-down)
- **Complexidade**: O(n·T) tempo, O(n·T) espaço
- **Aplicação**: Problemas de soma de subconjuntos

### 6. Text Segmentation with Memoization (Segmentação de Texto) ⭐ NOVO
- **Arquivo**: `text_segmentation_memoization.py`
- **Técnica**: Memoização (top-down) e tabulação (bottom-up)
- **Complexidade**: O(n²) tempo, O(n) espaço
- **Aplicação**: Segmentação de texto sem espaços
- **Referência**: Erickson, "Algorithms", Capítulo 3, Seção 3.3, "Interpunctio Verborum Redux"

## Desafio 22: Segmentação de Texto com Memoização

### Visão Geral
O problema de segmentação de texto (Word Break) consiste em determinar se uma string sem espaços pode ser segmentada em uma sequência de palavras válidas usando um dicionário.

### Implementações Disponíveis

#### 1. Memoização (Top-Down)
```python
text_segmentation_memoization(text: str, dictionary: Set[str]) -> Optional[List[str]]
```
- **Estado**: Índice inicial do sufixo da string
- **Complexidade**: O(n²) tempo, O(n) espaço
- **Vantagem**: Evita recálculos com cache

#### 2. Backtracking Puro
```python
text_segmentation_backtracking(text: str, dictionary: Set[str]) -> Optional[List[str]]
```
- **Complexidade**: O(2^n) tempo, O(n) espaço
- **Uso**: Comparação de performance

#### 3. Tabulação (Bottom-Up)
```python
text_segmentation_tabulation(text: str, dictionary: Set[str]) -> Optional[List[str]]
```
- **Complexidade**: O(n²) tempo, O(n) espaço
- **Vantagem**: Sem overhead de recursão

#### 4. Memoização Otimizada
```python
text_segmentation_optimized_memoization(text: str, dictionary: Set[str]) -> Optional[List[str]]
```
- **Otimizações**: Ordenação decrescente de tentativas
- **Benefício**: Pode encontrar soluções mais rapidamente

### Exemplo de Uso

```python
from text_segmentation_memoization import text_segmentation_memoization

# Dicionário de palavras válidas
dictionary = {"i", "like", "gfg", "programming"}

# Texto para segmentar
text = "ilikegfg"

# Segmentação
result = text_segmentation_memoization(text, dictionary)
print(result)  # ['i', 'like', 'gfg']
```

### Análise de Complexidade

#### Subproblemas Sobrepostos
- **Estado**: `dp[i]` = "O sufixo text[i..n] pode ser segmentado?"
- **Estados possíveis**: n (um para cada posição inicial)
- **Sobreposição**: Múltiplos caminhos podem chegar ao mesmo estado

#### Estrutura Ótima
- Se `text[i..j]` é uma palavra válida e `text[j..n]` pode ser segmentado,
  então `text[i..n]` pode ser segmentado
- **Fórmula**: `dp[i] = OR(dp[j] AND is_word(text[i..j]))` para todo j > i

#### Melhoria de Performance
- **Backtracking**: O(2^n) - exponencial
- **Memoização**: O(n²) - quadrático
- **Melhoria**: Reduz de exponencial para polinomial

### Casos de Teste

```python
# Casos básicos
("ilike", {"i", "like", "gfg"}, ["i", "like"])
("ilikegfg", {"i", "like", "gfg"}, ["i", "like", "gfg"])
("ilikemangoes", {"i", "like", "gfg"}, None)

# Casos com múltiplas soluções
("catsanddog", {"cat", "cats", "and", "sand", "dog"}, ["cat", "sand", "dog"])

# Casos extremos
("", {"a", "b"}, [])
("a", {"a"}, ["a"])
("a", {"b"}, None)
```

### Benchmark de Performance

| Tamanho | Backtracking | Memoização | Tabulação | Otimizada |
|---------|-------------|------------|-----------|-----------|
| 10      | 0.0016s     | 0.0000s    | 0.0000s   | 0.0010s   |
| 20      | 0.0000s     | 0.0000s    | 0.0000s   | 0.0000s   |
| 30      | Muito lento | 0.0000s    | 0.0000s   | 0.0000s   |
| 40      | Muito lento | 0.0000s    | 0.0000s   | 0.0000s   |
| 50      | Muito lento | 0.0000s    | 0.0021s   | 0.0015s   |

### Vínculos Conceituais

1. **Erickson, "Algorithms"**: Capítulo 3, Seção 3.3, "Interpunctio Verborum Redux"
2. **GeeksforGeeks**: [Word Break Problem](https://www.geeksforgeeks.org/dsa/word-break-problem-dp-32/)
3. **Tutorial Horizon**: [The Word Break Problem](https://tutorialhorizon.com/algorithms/the-word-break-problem/)

### Arquivos Relacionados

- `text_segmentation_memoization.py` - Implementação principal
- `test_text_segmentation_memoization.py` - Testes unitários
- `example_text_segmentation_memoization.py` - Exemplos de demonstração

## Como Executar

### Testes
```bash
cd algorithms/dynamic_programming
python test_text_segmentation_memoization.py
```

### Exemplo de Demonstração
```bash
cd algorithms/dynamic_programming
python example_text_segmentation_memoization.py
```

### Benchmark
```bash
cd algorithms/dynamic_programming
python text_segmentation_memoization.py
```

## Conceitos Demonstrados

1. **Transição de Backtracking para PD**: O(2^n) → O(n²)
2. **Estado do Subproblema**: Índice inicial do sufixo
3. **Subproblemas Sobrepostos**: Múltiplos caminhos para o mesmo estado
4. **Estrutura Ótima**: Decomposição em subproblemas menores
5. **Técnicas de Otimização**: Ordenação de tentativas, cache eficiente
6. **Análise de Complexidade**: Comparação prática de abordagens

## Contribuições

Este módulo demonstra a evolução de algoritmos de backtracking para programação dinâmica, mostrando como a identificação de subproblemas sobrepostos pode levar a melhorias dramáticas de performance. 