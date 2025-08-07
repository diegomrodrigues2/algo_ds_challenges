# Algoritmos de Backtracking

Este módulo contém implementações de algoritmos de backtracking clássicos, demonstrando a exploração sistemática de espaços de solução e técnicas de poda para otimização.

## Subset Sum (Soma de Subconjuntos)

### Visão Geral

O problema Subset Sum é um problema NP-completo clássico que consiste em determinar se existe um subconjunto de um conjunto de inteiros positivos cuja soma seja igual a um valor alvo específico.

### Estratégia do Algoritmo

O algoritmo de backtracking funciona da seguinte forma:

1. **Árvore de Decisão Binária**: Para cada elemento, a recursão decide se incluí-lo ou não no subconjunto
2. **Exploração Sistemática**: Explora todas as 2^n possibilidades de forma sistemática
3. **Poda Inteligente**: Usa otimizações para reduzir o espaço de busca
4. **Backtrack**: Se uma ramificação não leva à solução, volta e tenta outra

### Complexidade

- **Tempo**: O(2^n) - explora todos os 2^n subconjuntos possíveis
- **Espaço**: O(n) - profundidade da pilha de recursão
- **NP-Completo**: O problema é NP-completo, mas backtracking é a base para otimizações

### Funções Implementadas

#### `subset_sum_backtracking(numbers, target)`
Resolve o problema Subset Sum usando backtracking recursivo básico.

**Parâmetros:**
- `numbers`: Lista de inteiros positivos
- `target`: Soma alvo a ser encontrada

**Retorna:** Lista com os elementos que somam target, ou None se não existir solução

#### `subset_sum_backtracking_optimized(numbers, target)`
Versão otimizada com podas adicionais e remoção de duplicatas.

#### `subset_sum_count_solutions(numbers, target)`
Conta quantas soluções existem para o problema.

#### `subset_sum_all_solutions(numbers, target)`
Encontra todas as soluções para o problema.

#### `subset_sum_with_memoization(numbers, target)`
Versão com memoização para evitar recálculos.

#### `analyze_subset_sum_complexity(numbers, target)`
Analisa a complexidade do problema para os dados fornecidos.

### Exemplo de Uso

```python
from algorithms.backtracking.subset_sum import subset_sum_backtracking

# Exemplo básico
numbers = [1, 2, 3, 4, 5]
target = 7
result = subset_sum_backtracking(numbers, target)
print(f"Solução: {result}")  # [4, 3] ou [5, 2] ou [3, 2, 2]

# Exemplo sem solução
numbers = [1, 2, 3, 4, 5]
target = 20
result = subset_sum_backtracking(numbers, target)
print(f"Solução: {result}")  # None

# Contar soluções
count = subset_sum_count_solutions([1, 2, 3, 4, 5], 7)
print(f"Número de soluções: {count}")
```

### Referências

- **Erickson, "Algorithms"**: Capítulo 2, Seção 2.3, "Subset Sum"
- **GitHub**: [SubsetSum-BacktrackAlgorithm](https://github.com/parthnan/SubsetSum-BacktrackAlgorithm)
- **UIUC**: [Backtracking Notes](https://courses.grainger.illinois.edu/cs473/sp2010/notes/02-backtracking.pdf)
- **Final Round AI**: [Subset Sum Tutorial](https://www.finalroundai.com/articles/subset-sum-problem)

### Análise da Complexidade

A relação de recorrência é:
```
T(n) = 2 × T(n-1) + O(1)
```

A solução é:
```
T(n) = O(2^n)
```

### Otimizações Implementadas

#### 1. Ordenação Decrescente
```python
sorted_numbers = sorted(numbers, reverse=True)
```
- Encontra soluções mais rapidamente
- Permite podas mais eficientes

#### 2. Poda por Soma Restante
```python
remaining_sum = sum(sorted_numbers[index:])
if current_sum + remaining_sum < target:
    return None
```

#### 3. Poda por Elementos Duplicados
```python
unique_numbers = sorted(set(numbers), reverse=True)
```

#### 4. Early Termination
```python
if target > total_sum:
    return None
if target == total_sum:
    return unique_numbers.copy()
```

### Testes

Execute os testes com:
```bash
pytest algorithms/backtracking/test_subset_sum.py
```

Os testes cobrem:
- Casos básicos e casos extremos
- Todas as implementações (básica, otimizada, memoização)
- Contagem de soluções e todas as soluções
- Análise de complexidade
- Performance e correção
- Casos especiais (target zero, elementos duplicados)

### Aplicações Práticas

1. **Problemas de Alocação**: Distribuição de recursos
2. **Problemas de Corte**: Corte de barras em comprimentos específicos
3. **Problemas de Empacotamento**: Empacotamento em containers
4. **Problemas Financeiros**: Seleção de investimentos
5. **Problemas de Scheduling**: Alocação de tarefas

### Insights Teóricos

1. **NP-Completeness**: O problema é NP-completo
2. **Árvore de Decisão**: Cada nó representa uma decisão binária
3. **Poda Eficiente**: Otimizações podem reduzir drasticamente o tempo
4. **Base para DP**: Backtracking é a base para programação dinâmica
5. **Exploração Sistemática**: Garante encontrar a solução se existir

### Variações do Problema

1. **Subset Sum com Pesos**: Elementos com pesos diferentes
2. **Subset Sum com Restrições**: Limitações adicionais
3. **Subset Sum Aproximado**: Encontrar soma mais próxima do target
4. **Subset Sum Múltiplo**: Múltiplos targets
5. **Subset Sum com Duplicatas**: Elementos podem ser usados múltiplas vezes

## N-Rainhas

### Visão Geral

O problema das N-Rainhas é o exemplo prototípico para ensinar backtracking. Consiste em posicionar N rainhas de xadrez em um tabuleiro N×N de forma que nenhuma rainha ameace outra. Uma rainha pode atacar na horizontal, vertical e diagonal.

### Estratégia do Algoritmo

O algoritmo de backtracking funciona da seguinte forma:

1. **Colocar rainhas linha por linha**: Começamos na primeira linha e tentamos colocar uma rainha em cada coluna
2. **Verificar segurança**: Para cada posição candidata, verificamos se é seguro colocar uma rainha
3. **Recursão**: Se é seguro, colocamos a rainha e recursivamente tentamos colocar na próxima linha
4. **Backtrack**: Se não conseguimos colocar na linha atual, voltamos e tentamos a próxima posição
5. **Solução completa**: Quando colocamos N rainhas, encontramos uma solução

### Complexidade

- **Tempo**: O(n!) no pior caso - mas com podas eficientes, muito melhor na prática
- **Espaço**: O(n) - altura da árvore de recursão
- **Soluções**: Para n=8, existem 92 soluções únicas

### Funções Implementadas

#### `solve_n_queens(n)`
Resolve o problema das N-Rainhas usando backtracking.

**Parâmetros:**
- `n`: Tamanho do tabuleiro (n x n)

**Retorna:** Lista de todas as soluções válidas, onde cada solução é uma lista de strings representando o tabuleiro

#### `solve_n_queens_backtracking(n)`
Implementa o algoritmo de backtracking clássico.

#### `is_safe(board, row, col)`
Verifica se é seguro colocar uma rainha na posição (row, col).

#### `is_safe_optimized(cols, row, col)`
Versão otimizada usando arrays auxiliares para rastrear colunas e diagonais.

#### `solve_n_queens_optimized(n)`
Versão otimizada usando arrays auxiliares para melhor performance.

#### `solve_n_queens_count_only(n)`
Conta apenas o número de soluções sem armazená-las.

#### `solve_n_queens_one_solution(n)`
Encontra apenas uma solução válida.

#### `solve_n_queens_symmetry_breaking(n)`
Usa quebra de simetria para reduzir o espaço de busca.

#### `solve_n_queens_iterative(n)`
Versão iterativa usando pilha para simular recursão.

#### `solve_n_queens_with_constraints(n, fixed_queens)`
Resolve N-Rainhas com rainhas fixas em posições específicas.

#### `validate_solution(board)`
Valida se uma solução é correta.

#### `print_board(board)`
Imprime o tabuleiro de forma legível.

### Exemplo de Uso

```python
from algorithms.backtracking.n_queens import solve_n_queens

# Resolver para n = 4
solutions = solve_n_queens(4)
print(f"Número de soluções: {len(solutions)}")

# Imprimir primeira solução
if solutions:
    print("Primeira solução:")
    for row in solutions[0]:
        print(row)

# Saída:
# Número de soluções: 2
# Primeira solução:
# .Q..
# ...Q
# Q...
# ..Q.
```

### Referências

- **Erickson, "Algorithms"**: Capítulo 2, Seção 2.1, "N Queens"
- **Jeff Erickson**: [Backtracking Chapter](https://jeffe.cs.illinois.edu/teaching/algorithms/book/02-backtracking.pdf)
- **GitHub**: [N-Queen Problem Implementation](https://github.com/waqqasiq/n-queen-problem-using-backtracking)
- **Research Paper**: [Complexity of N-Queens Completion](https://www-users.york.ac.uk/~pwn503/n-queens-jair.pdf)

### Análise da Complexidade

A relação de recorrência é:
```
T(n) = n × T(n-1) + O(n)
```

A solução é:
```
T(n) = O(n!)
```

### Variações Implementadas

1. **Versão Recursiva Clássica**: Demonstra o paradigma de backtracking
2. **Versão Otimizada**: Usa arrays auxiliares para verificação O(1)
3. **Versão Iterativa**: Evita overhead de recursão
4. **Quebra de Simetria**: Reduz o espaço de busca
5. **Contagem Apenas**: Economiza memória para n grandes
6. **Restrições**: Permite rainhas fixas
7. **Versão Paralela**: Aproveita múltiplas threads
8. **Algoritmos Heurísticos**: Hill climbing, mínimos conflitos
9. **Algoritmo Genético**: Usa evolução para encontrar soluções
10. **Redução SAT**: Converte para problema de satisfabilidade

### Otimizações Implementadas

#### 1. Verificação O(1)
```python
def is_safe_optimized(cols, row, col):
    # Verificar coluna
    for i in range(row):
        if cols[i] == col:
            return False
    
    # Verificar diagonais
    for i in range(row):
        if abs(cols[i] - col) == abs(i - row):
            return False
    
    return True
```

#### 2. Quebra de Simetria
- **Rotação**: Apenas uma solução por classe de rotação
- **Reflexão**: Apenas uma solução por classe de reflexão
- **Redução**: Reduz o espaço de busca significativamente

#### 3. Arrays Auxiliares
```python
cols = [-1] * n  # cols[i] = coluna da rainha na linha i
diag1 = [False] * (2*n-1)  # Diagonal principal
diag2 = [False] * (2*n-1)  # Diagonal secundária
```

### Testes

Execute os testes com:
```bash
pytest algorithms/backtracking/test_n_queens.py
```

Os testes cobrem:
- Casos básicos (n=1, 2, 3, 4, 5, 6, 8)
- Todas as variações implementadas
- Validação de soluções
- Performance e análise de complexidade
- Casos extremos (n grande, restrições)
- Consistência entre diferentes implementações
- Análise de simetrias e limites teóricos

### Aplicações Práticas

1. **Puzzle Games**: Sudoku, Kakuro, etc.
2. **Scheduling**: Alocação de recursos sem conflitos
3. **Circuit Design**: Layout de circuitos
4. **AI Planning**: Planejamento de ações
5. **Constraint Satisfaction**: Problemas de satisfação de restrições

### Insights Teóricos

1. **Exploração Sistemática**: Backtracking explora todo o espaço de soluções
2. **Poda Inteligente**: Verificações eficientes reduzem drasticamente o tempo
3. **Simetrias**: Quebra de simetria pode reduzir o espaço de busca
4. **Heurísticas**: Algoritmos heurísticos podem encontrar soluções rapidamente
5. **NP-Completeness**: O problema de completude é NP-completo

### Limites Teóricos

- **Número de Soluções**: Cresce exponencialmente com n
- **Complexidade**: O(n!) no pior caso
- **Soluções Conhecidas**: 
  - n=1: 1 solução
  - n=4: 2 soluções
  - n=5: 10 soluções
  - n=6: 4 soluções
  - n=7: 40 soluções
  - n=8: 92 soluções
  - n=9: 352 soluções
  - n=10: 724 soluções

### Variações do Problema

1. **N-Rainhas com Restrições**: Rainhas fixas em posições específicas
2. **N-Rainhas com Pesos**: Maximizar peso total das rainhas
3. **N-Rainhas Máximo**: Máximo número de rainhas sem conflitos
4. **N-Rainhas Completude**: Completar tabuleiro parcial
5. **N-Rainhas Toroidal**: Tabuleiro com bordas conectadas
6. **N-Rainhas 3D**: Extensão para três dimensões

## Text Segmentation (Segmentação de Texto)

### Visão Geral

O problema de Segmentação de Texto (Word Break) consiste em determinar se uma string sem espaços pode ser segmentada em uma sequência de palavras válidas, usando uma função `is_word(substring)` que verifica se uma substring é uma palavra válida.

### Estratégia do Algoritmo

O algoritmo de backtracking funciona da seguinte forma:

1. **Exploração de Prefixos**: Para cada posição, tenta todos os prefixos possíveis
2. **Verificação de Palavras**: Usa a função `is_word()` para verificar se o prefixo é válido
3. **Recursão**: Se o prefixo é válido, recursivamente tenta segmentar o restante
4. **Backtrack**: Se uma ramificação não leva à solução, volta e tenta outro prefixo
5. **Memoização**: Evita recálculo de subproblemas já resolvidos

### Complexidade

- **Tempo**: O(2^n) no pior caso - mas com memoização, O(n²) na prática
- **Espaço**: O(n) - profundidade da pilha de recursão + memoização
- **Subproblemas Sobrepostos**: Ideal para memoização e programação dinâmica

### Funções Implementadas

#### `text_segmentation_backtracking(text, is_word_func)`
Resolve o problema de segmentação de texto usando backtracking recursivo básico.

**Parâmetros:**
- `text`: String sem espaços para segmentar
- `is_word_func`: Função que retorna True se a substring for uma palavra válida

**Retorna:** Lista de palavras se a segmentação for possível, None caso contrário

#### `text_segmentation_with_memoization(text, is_word_func)`
Versão com memoização para evitar recálculo de subproblemas.

#### `text_segmentation_all_solutions(text, is_word_func)`
Encontra todas as possíveis segmentações da string.

#### `text_segmentation_count_solutions(text, is_word_func)`
Conta o número total de segmentações possíveis.

#### `text_segmentation_optimized(text, is_word_func)`
Versão otimizada com poda e ordenação de tentativas.

#### `analyze_text_segmentation_complexity(text, is_word_func)`
Analisa a complexidade do problema para os dados fornecidos.

### Exemplo de Uso

```python
from algorithms.backtracking.text_segmentation import text_segmentation_backtracking

# Exemplo básico
def is_word(s): return s in ["hello", "world"]
result = text_segmentation_backtracking("helloworld", is_word)
print(f"Solução: {result}")  # ["hello", "world"]

# Exemplo complexo
def is_word2(s): return s in ["i", "am", "a", "student"]
result = text_segmentation_backtracking("iamastudent", is_word2)
print(f"Solução: {result}")  # ["i", "am", "a", "student"]

# Exemplo sem solução
result = text_segmentation_backtracking("helloworldx", is_word)
print(f"Solução: {result}")  # None

# Todas as soluções
def is_word3(s): return s in ["a", "aa", "aaa"]
all_solutions = text_segmentation_all_solutions("aaa", is_word3)
print(f"Todas as soluções: {all_solutions}")
```

### Referências

- **Erickson, "Algorithms"**: Capítulo 2, Seção 2.5, "Text Segmentation"
- **GitHub**: [LeetcodePython/word_break.py](https://github.com/lilianweng/LeetcodePython/blob/master/word_break.py)
- **UIUC**: [Backtracking Notes](https://courses.grainger.illinois.edu/cs374/sp2018/a/notes/02-backtracking.pdf)
- **Tutorial Horizon**: [Word Break Problem](https://tutorialhorizon.com/algorithms/the-word-break-problem/)

### Análise da Complexidade

A relação de recorrência é:
```
T(n) = Σ T(n-i) para i de 1 a n
```

A solução é:
```
T(n) = O(2^n) sem memoização
T(n) = O(n²) com memoização
```

### Otimizações Implementadas

#### 1. Memoização
```python
memo: Dict[int, Optional[List[str]]] = {}
if start in memo:
    return memo[start]
```

#### 2. Ordenação de Tentativas
```python
# Tenta prefixos em ordem decrescente de tamanho
for end in range(len(text), start, -1):
```

#### 3. Early Termination
```python
if start == len(text):
    return []  # Caso base
```

### Testes

Execute os testes com:
```bash
pytest algorithms/backtracking/test_text_segmentation.py
```

Os testes cobrem:
- Casos básicos e casos extremos
- Todas as implementações (básica, memoização, otimizada)
- Encontrar todas as soluções e contagem
- Análise de complexidade
- Performance e correção
- Casos especiais (string vazia, caracteres únicos)

### Aplicações Práticas

1. **Processamento de Linguagem Natural**: Segmentação de texto sem espaços
2. **Reconhecimento de Padrões**: Identificação de palavras em texto contínuo
3. **Compressão de Dados**: Segmentação para compressão
4. **Análise de Texto**: Processamento de documentos
5. **Sistemas de Busca**: Indexação de texto

### Insights Teóricos

1. **Subproblemas Sobrepostos**: Ideal para memoização
2. **Exploração de Prefixos**: Cada posição tenta todos os prefixos possíveis
3. **Recursão Natural**: A definição recursiva é intuitiva
4. **Base para DP**: Backtracking é a base para programação dinâmica
5. **Complexidade Variável**: Depende muito da estrutura do dicionário

### Variações do Problema

1. **Segmentação com Pesos**: Palavras com pesos diferentes
2. **Segmentação Mínima**: Menor número de palavras
3. **Segmentação com Restrições**: Limitações adicionais
4. **Segmentação Probabilística**: Probabilidades para palavras
5. **Segmentação Múltipla**: Múltiplos dicionários

## Longest Increasing Subsequence (LIS) - Versão Backtracking

### Visão Geral

O problema da Subsequência Crescente Mais Longa (LIS) consiste em encontrar a subsequência mais longa de uma sequência de números onde cada elemento é maior que o anterior. A versão backtracking implementa a formulação de Erickson: LISbigger(prev, A[j..n]).

### Estratégia do Algoritmo

O algoritmo de backtracking funciona da seguinte forma:

1. **Formulação de Erickson**: LISbigger(prev, A[j..n]) - qual é o comprimento da LIS no restante do array, onde todos os elementos devem ser maiores que prev
2. **Decisão Binária**: Para cada elemento A[j], a recursão decide se o inclui (se A[j] > prev) ou o ignora
3. **Exploração Sistemática**: Explora todas as 2^n possibilidades de forma sistemática
4. **Estrutura de Decisão**: Cada nó na árvore representa uma decisão binária (incluir ou não)
5. **Complexidade Exponencial**: Leva à complexidade exponencial, servindo como base para memoização

### Complexidade

- **Tempo**: O(2^n) - exponencial devido às decisões binárias
- **Espaço**: O(n) - profundidade da pilha de recursão
- **Com Memoização**: O(n²) - memoização reduz drasticamente a complexidade

### Funções Implementadas

#### `lis_backtracking(sequence)`
Resolve o problema LIS usando backtracking recursivo básico.

**Parâmetros:**
- `sequence`: Lista de inteiros

**Retorna:** Comprimento da subsequência crescente mais longa

#### `lis_backtracking_with_memoization(sequence)`
Versão com memoização para evitar recálculo de subproblemas.

#### `lis_backtracking_all_solutions(sequence)`
Encontra todas as subsequências crescentes mais longas.

#### `lis_backtracking_count_solutions(sequence)`
Conta o número de subsequências crescentes mais longas.

#### `lis_backtracking_optimized(sequence)`
Versão otimizada com early termination e melhor poda.

#### `lis_backtracking_with_path(sequence)`
Encontra o comprimento e um exemplo da subsequência crescente mais longa.

#### `lis_backtracking_erickson_formulation(sequence)`
Implementação direta da formulação de Erickson LISbigger(prev, A[j..n]).

#### `lis_backtracking_erickson_memoized(sequence)`
Formulação de Erickson com memoização.

#### `analyze_lis_complexity(sequence)`
Analisa a complexidade e performance de diferentes implementações LIS.

### Exemplo de Uso

```python
from algorithms.backtracking.lis_backtracking import lis_backtracking

# Exemplo básico
sequence = [10, 22, 9, 33, 21, 50, 41, 60]
result = lis_backtracking(sequence)
print(f"LIS length: {result}")  # 5

# Exemplo com path
length, path = lis_backtracking_with_path(sequence)
print(f"LIS path: {path}")  # [10, 22, 33, 50, 60]

# Todas as soluções
solutions = lis_backtracking_all_solutions(sequence)
print(f"Number of LIS: {len(solutions)}")

# Contar soluções
length, count = lis_backtracking_count_solutions(sequence)
print(f"LIS length: {length}, count: {count}")
```

### Referências

- **Erickson, "Algorithms"**: Capítulo 2, Seção 2.6, "Longest Increasing Subsequence"
- **GeeksforGeeks**: [Python Program for LIS](https://www.geeksforgeeks.org/dsa/python-program-for-longest-increasing-subsequence/)
- **GitHub**: [LeetCode LIS Solution](https://github.com/neetcode-gh/leetcode/blob/main/python%2F0300-longest-increasing-subsequence.py)
- **Otfried**: [Dynamic Programming Notes](https://otfried.org/courses/cs300/notes/dynamic-programming.pdf)

### Análise da Complexidade

A relação de recorrência é:
```
T(n) = 2 × T(n-1) + O(1)
```

A solução é:
```
T(n) = O(2^n) sem memoização
T(n) = O(n²) com memoização
```

### Otimizações Implementadas

#### 1. Memoização
```python
memo: Dict[Tuple[int, int], int] = {}
state = (index, prev)
if state in memo:
    return memo[state]
```

#### 2. Early Termination
```python
remaining = n - index
if current_length + remaining <= best_length:
    return
```

#### 3. Formulação de Erickson
```python
def lis_bigger(prev: int, start: int) -> int:
    # Skip current element: LISbigger(prev, A[start+1..n])
    skip = lis_bigger(prev, start + 1)
    
    # Include current element if it's greater than prev
    include = 0
    if sequence[start] > prev:
        include = 1 + lis_bigger(sequence[start], start + 1)
    
    return max(skip, include)
```

### Testes

Execute os testes com:
```bash
pytest algorithms/backtracking/test_lis_backtracking.py
```

Os testes cobrem:
- Casos básicos e casos extremos
- Todas as implementações (básica, memoização, otimizada, Erickson)
- Encontrar todas as soluções e contagem
- Análise de complexidade
- Performance e correção
- Casos especiais (sequência vazia, elementos únicos, números negativos)

### Aplicações Práticas

1. **Bioinformática**: Análise de sequências de DNA
2. **Processamento de Sinais**: Análise de tendências
3. **Machine Learning**: Feature selection
4. **Análise Financeira**: Identificação de tendências de mercado
5. **Processamento de Texto**: Análise de sequências de caracteres

### Insights Teóricos

1. **Estrutura de Decisão Binária**: Cada elemento é incluído ou não
2. **Subproblemas Sobrepostos**: Ideal para memoização
3. **Base para DP**: Backtracking é a base para programação dinâmica
4. **Formulação de Erickson**: LISbigger(prev, A[j..n]) é intuitiva
5. **Complexidade Exponencial**: Demonstra a necessidade de otimização

### Variações do Problema

1. **LIS com Pesos**: Elementos com pesos diferentes
2. **LIS com Restrições**: Limitações adicionais
3. **LIS Aproximado**: Encontrar subsequência próxima da ideal
4. **LIS Múltiplo**: Múltiplas sequências
5. **LIS com Duplicatas**: Elementos podem ser repetidos

## Optimal Binary Search Tree (OBST) - Versão Backtracking

### Visão Geral

O problema da Árvore de Busca Binária Ótima (OBST) consiste em construir uma árvore de busca binária que minimize o custo total de todas as buscas, dado um array ordenado de chaves e suas frequências de busca.

### Estratégia do Algoritmo

O algoritmo de backtracking funciona da seguinte forma:

1. **Formulação de Erickson**: OptCost(i, k) = min(OptCost(i, r-1) + OptCost(r+1, k) + fsum) para r em [i, k]
2. **Teste de Todas as Raízes**: Para cada intervalo [i, k], testa todas as possíveis raízes r
3. **Divisão em Subproblemas**: Para cada raiz r, resolve recursivamente os subproblemas [i, r-1] e [r+1, k]
4. **Sobreposição de Subproblemas**: Muitos subproblemas são recalculados, tornando ideal para memoização
5. **Complexidade Exponencial**: Leva à complexidade exponencial, servindo como base para DP

### Complexidade

- **Tempo**: O(n * 2^n) - exponencial devido ao teste de todas as possíveis raízes
- **Espaço**: O(n) - profundidade da pilha de recursão
- **Com Memoização**: O(n³) - memoização reduz drasticamente a complexidade

### Funções Implementadas

#### `obst_backtracking(keys, freq)`
Resolve o problema OBST usando backtracking recursivo básico.

**Parâmetros:**
- `keys`: Array ordenado de chaves de busca
- `freq`: Array de frequências de busca para cada chave

**Retorna:** Custo mínimo da árvore de busca binária ótima

#### `obst_backtracking_with_memoization(keys, freq)`
Versão com memoização para evitar recálculo de subproblemas.

#### `obst_backtracking_with_structure(keys, freq)`
Encontra o custo ótimo e a estrutura de raízes da OBST.

#### `obst_backtracking_all_structures(keys, freq)`
Encontra todas as estruturas ótimas possíveis (quando há empates).

#### `obst_backtracking_count_structures(keys, freq)`
Conta o número de estruturas ótimas possíveis.

#### `obst_backtracking_optimized(keys, freq)`
Versão otimizada com early termination e melhor poda.

#### `obst_backtracking_with_tree_building(keys, freq)`
Encontra o custo ótimo e constrói a estrutura da árvore.

#### `obst_backtracking_erickson_formulation(keys, freq)`
Implementação direta da formulação de Erickson OptCost(i, k).

#### `obst_backtracking_erickson_memoized(keys, freq)`
Formulação de Erickson com memoização.

#### `analyze_obst_complexity(keys, freq)`
Analisa a complexidade e performance de diferentes implementações OBST.

### Exemplo de Uso

```python
from algorithms.backtracking.obst_backtracking import obst_backtracking

# Exemplo básico
keys = [10, 12, 20]
freq = [34, 8, 50]
result = obst_backtracking(keys, freq)
print(f"OBST cost: {result}")  # 142

# Exemplo com estrutura
cost, structure = obst_backtracking_with_structure(keys, freq)
print(f"Optimal cost: {cost}")
print(f"Root structure: {structure}")

# Construir árvore
cost, tree = obst_backtracking_with_tree_building(keys, freq)
print(f"Tree structure: {tree}")

# Contar estruturas
cost, count = obst_backtracking_count_structures(keys, freq)
print(f"Number of optimal structures: {count}")
```

### Referências

- **Erickson, "Algorithms"**: Capítulo 2, Seção 2.8, "Optimal Binary Search Trees"
- **GeeksforGeeks**: [Optimal Binary Search Tree](https://www.geeksforgeeks.org/dsa/optimal-binary-search-tree-dp-24/)
- **GitHub**: [TheAlgorithms/Python OBST](https://github.com/TheAlgorithms/Python/blob/master/dynamic_programming/optimal_binary_search_tree.py)
- **Jeff Erickson**: [Dynamic Programming Notes](https://jeffe.cs.illinois.edu/teaching/algorithms/book/03-dynprog.pdf)

### Análise da Complexidade

A relação de recorrência é:
```
T(n) = Σ T(r-1) × T(n-r) para r de 1 a n
```

A solução é:
```
T(n) = O(n * 2^n) sem memoização
T(n) = O(n³) com memoização
```

### Otimizações Implementadas

#### 1. Memoização
```python
memo: Dict[Tuple[int, int], int] = {}
state = (i, j)
if state in memo:
    return memo[state]
```

#### 2. Ordenação de Tentativas
```python
# Tenta elementos do meio primeiro (frequentemente melhores)
mid = (i + j) // 2
for offset in range(j - i + 1):
    r = mid + offset if mid + offset <= j else i + (mid + offset - j - 1)
```

#### 3. Formulação de Erickson
```python
def opt_cost(i: int, k: int) -> int:
    # Cost = left subtree + right subtree + frequency sum
    cost = opt_cost(i, r - 1) + opt_cost(r + 1, k)
    return min_cost + fsum
```

### Testes

Execute os testes com:
```bash
pytest algorithms/backtracking/test_obst_backtracking.py
```

Os testes cobrem:
- Casos básicos e casos extremos
- Todas as implementações (básica, memoização, otimizada, Erickson)
- Encontrar estruturas ótimas e contagem
- Análise de complexidade
- Performance e correção
- Casos especiais (entrada vazia, frequências zero, chaves duplicadas)

### Aplicações Práticas

1. **Compiladores**: Otimização de tabelas de símbolos
2. **Sistemas de Banco de Dados**: Índices otimizados
3. **Processamento de Linguagem Natural**: Dicionários otimizados
4. **Sistemas de Busca**: Estruturas de dados otimizadas
5. **Compressão de Dados**: Árvores Huffman otimizadas

### Insights Teóricos

1. **Sobreposição de Subproblemas**: Ideal para memoização
2. **Teste de Todas as Raízes**: Cada intervalo testa todas as possíveis raízes
3. **Base para DP**: Backtracking é a base para programação dinâmica
4. **Formulação de Erickson**: OptCost(i, k) é intuitiva
5. **Complexidade Exponencial**: Demonstra a necessidade de otimização

### Variações do Problema

1. **OBST com Pesos**: Chaves com pesos diferentes
2. **OBST com Restrições**: Limitações adicionais na estrutura
3. **OBST Aproximado**: Encontrar árvore próxima da ótima
4. **OBST Múltiplo**: Múltiplas árvores
5. **OBST com Duplicatas**: Chaves podem ser repetidas

## Subset Generation (Geração de Subconjuntos)

### Visão Geral

O problema de Geração de Subconjuntos (Power Set) consiste em enumerar todos os subconjuntos possíveis de um conjunto dado. É um problema fundamental de enumeração combinatória que demonstra a estrutura de decisão binária (incluir/excluir) relacionada ao problema Subset Sum.

### Estratégia do Algoritmo

O algoritmo de backtracking funciona da seguinte forma:

1. **Árvore de Decisão Binária**: Para cada elemento, a recursão explora dois caminhos: incluir ou excluir o elemento
2. **Exploração Sistemática**: Explora todas as 2^n possibilidades de forma sistemática
3. **Estrutura de Decisão**: Cada nó na árvore representa uma decisão binária (incluir/excluir)
4. **Backtrack**: Após explorar uma ramificação, volta e explora a alternativa
5. **Alternativa Bitmask**: Mapeia cada inteiro de 0 a 2^n-1 para um subconjunto

### Complexidade

- **Tempo**: O(2^n) - explora todos os 2^n subconjuntos possíveis
- **Espaço**: O(n) - profundidade da pilha de recursão + O(2^n) para resultado
- **Bitmask**: O(n * 2^n) - mas mais eficiente em implementações de baixo nível

### Funções Implementadas

#### `subset_generation_backtracking(elements)`
Gera todos os subconjuntos usando backtracking recursivo básico.

**Parâmetros:**
- `elements`: Lista de elementos para gerar subconjuntos

**Retorna:** Lista de todos os subconjuntos possíveis

#### `subset_generation_iterative_bitmask(elements)`
Gera todos os subconjuntos usando abordagem iterativa com bitmask.

#### `subset_generation_with_constraints(elements, min_size, max_size)`
Gera subconjuntos com restrições de tamanho.

#### `subset_generation_with_sum_constraint(elements, target_sum)`
Gera subconjuntos que somam exatamente o valor alvo.

#### `subset_generation_with_memoization(elements)`
Versão com memoização (menos eficaz, mas demonstra o conceito).

#### `subset_generation_lexicographic(elements)`
Gera subconjuntos em ordem lexicográfica.

#### `subset_generation_count_only(elements)`
Conta o número total de subconjuntos sem gerá-los.

#### `subset_generation_with_duplicates(elements)`
Gera subconjuntos únicos quando há elementos duplicados.

#### `subset_generation_optimized(elements)`
Versão otimizada com melhor performance.

#### `analyze_subset_generation_complexity(elements)`
Analisa a complexidade e performance de diferentes implementações.

### Exemplo de Uso

```python
from algorithms.backtracking.subset_generation import subset_generation_backtracking

# Exemplo básico
elements = [1, 2, 3]
result = subset_generation_backtracking(elements)
print(f"Subconjuntos: {result}")
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# Com restrições de tamanho
size_constrained = subset_generation_with_constraints(elements, 1, 2)
print(f"Tamanho 1-2: {size_constrained}")
# [[1], [2], [1, 2], [3], [1, 3], [2, 3]]

# Com restrições de soma
sum_constrained = subset_generation_with_sum_constraint(elements, 3)
print(f"Soma 3: {sum_constrained}")
# [[3], [1, 2]]

# Contagem sem gerar
count = subset_generation_count_only(elements)
print(f"Total: {count}")  # 8
```

### Referências

- **Erickson, "Algorithms"**: Capítulo 2, Seção 2.3 (estrutura de decisão)
- **GeeksforGeeks**: [Backtracking to find all subsets](https://www.geeksforgeeks.org/dsa/backtracking-to-find-all-subsets/)
- **Simon Hessner**: [Calculate power set without recursion](https://simonhessner.de/calculate-power-set-set-of-all-subsets-in-python-without-recursion/)
- **The Algorists**: [PowerSet Tutorial](https://thealgorists.com/Algo/Backtracking/PowerSet)
- **Finxter**: [Python Powerset](https://blog.finxter.com/python-powerset-how-to-get-all-subsets-of-a-set/)

### Análise da Complexidade

A relação de recorrência é:
```
T(n) = 2 × T(n-1) + O(1)
```

A solução é:
```
T(n) = O(2^n)
```

### Otimizações Implementadas

#### 1. Abordagem Bitmask
```python
for i in range(2**n):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(elements[j])
    result.append(subset)
```

#### 2. Geração Lexicográfica
```python
def backtrack(index: int, current_subset: List) -> None:
    result.append(current_subset[:])
    for i in range(index, len(sorted_elements)):
        current_subset.append(sorted_elements[i])
        backtrack(i + 1, current_subset)
        current_subset.pop()
```

#### 3. Tratamento de Duplicatas
```python
if i > index and sorted_elements[i] == sorted_elements[i - 1]:
    continue  # Pular duplicatas consecutivas
```

#### 4. Restrições de Tamanho
```python
if min_size <= len(current_subset) <= max_size:
    result.append(current_subset[:])
```

### Testes

Execute os testes com:
```bash
pytest algorithms/backtracking/test_subset_generation.py
```

Os testes cobrem:
- Casos básicos e casos extremos
- Todas as implementações (backtracking, bitmask, otimizada)
- Geração com restrições e contagem
- Análise de complexidade
- Performance e correção
- Casos especiais (conjunto vazio, duplicatas, tipos diferentes)

### Aplicações Práticas

1. **Problemas de Seleção**: Escolher itens de um conjunto
2. **Problemas de Combinação**: Gerar todas as combinações possíveis
3. **Problemas de Permutação**: Base para algoritmos de permutação
4. **Problemas de Otimização**: Explorar todas as possibilidades
5. **Problemas de Enumeração**: Contar ou listar todas as opções

### Insights Teóricos

1. **Estrutura de Decisão Binária**: Cada elemento é incluído ou não
2. **Conectividade com Subset Sum**: Mesma estrutura de decisão
3. **Representação Binária**: Bitmask demonstra conexão entre combinatória e representação binária
4. **Enumeração Sistemática**: Garante que todos os subconjuntos sejam gerados
5. **Base para Outros Problemas**: Fundamento para problemas mais complexos

### Variações do Problema

1. **Subconjuntos com Restrições**: Limitações de tamanho ou soma
2. **Subconjuntos com Duplicatas**: Tratamento de elementos repetidos
3. **Subconjuntos Lexicográficos**: Ordem específica de geração
4. **Subconjuntos com Pesos**: Elementos com pesos diferentes
5. **Subconjuntos Múltiplos**: Múltiplos conjuntos de entrada

## Permutation Generation (Geração de Permutações)

### Visão Geral

O problema de Geração de Permutações consiste em enumerar todas as possíveis ordenações de elementos em um conjunto ou string. É um problema clássico de backtracking onde a cada passo recursivo, um elemento ainda não utilizado é escolhido.

### Estratégia do Algoritmo

O algoritmo de backtracking funciona da seguinte forma:

1. **Escolha de Elementos**: Para cada posição, escolhe um elemento ainda não utilizado
2. **Exploração Sistemática**: Explora todas as n! possibilidades de forma sistemática
3. **Estrutura de Decisão**: Cada nó na árvore representa a escolha de um elemento para uma posição
4. **Backtrack**: Após explorar uma ramificação, volta e tenta outra escolha
5. **Abordagens Alternativas**: In-place swapping ou lista de elementos restantes

### Complexidade

- **Tempo**: O(n!) - explora todas as n! permutações possíveis
- **Espaço**: O(n) - profundidade da pilha de recursão + O(n!) para resultado
- **In-place Swap**: O(n!) - mas mais eficiente em termos de espaço

### Funções Implementadas

#### `permutation_generation_backtracking(elements)`
Gera todas as permutações usando backtracking com lista de elementos restantes.

**Parâmetros:**
- `elements`: Lista de elementos para permutar

**Retorna:** Lista de todas as permutações possíveis

#### `permutation_generation_inplace_swap(elements)`
Gera todas as permutações usando abordagem in-place com trocas.

#### `permutation_generation_with_duplicates(elements)`
Gera permutações únicas quando há elementos duplicados.

#### `permutation_generation_lexicographic(elements)`
Gera permutações em ordem lexicográfica.

#### `permutation_generation_count_only(n)`
Conta o número total de permutações sem gerá-las.

#### `permutation_generation_with_constraints(elements, constraint_func)`
Gera permutações que satisfazem uma restrição específica.

#### `permutation_generation_optimized(elements)`
Versão otimizada com alocações mínimas.

#### `permutation_generation_with_memoization(elements)`
Versão com memoização (menos eficaz, mas demonstra o conceito).

#### `analyze_permutation_complexity(elements)`
Analisa a complexidade e performance de diferentes implementações.

### Exemplo de Uso

```python
from algorithms.backtracking.permutation_generation import permutation_generation_backtracking

# Exemplo básico
elements = [1, 2, 3]
result = permutation_generation_backtracking(elements)
print(f"Permutações: {result}")
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

# Com duplicatas
elements_with_dups = [1, 1, 2]
unique_result = permutation_generation_with_duplicates(elements_with_dups)
print(f"Permutações únicas: {unique_result}")
# [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

# Lexicográfica
lex_result = permutation_generation_lexicographic(elements)
print(f"Lexicográfica: {lex_result}")

# Contagem
count = permutation_generation_count_only(3)
print(f"Total: {count}")  # 6
```

### Referências

- **Erickson, "Algorithms"**: Capítulo 2, Seção 2.4 (Backtracking)
- **GeeksforGeeks**: [Print all permutations of a given string](https://www.geeksforgeeks.org/dsa/write-a-c-program-to-print-all-permutations-of-a-given-string/)
- **GeeksforGeeks**: [Generate all the permutation of a list in Python](https://www.geeksforgeeks.org/python/generate-all-the-permutation-of-a-list-in-python/)
- **Medium**: [Permutation Algorithm via Backtracking](https://medium.com/@guguru/permutation-algorithm-via-backtracking-39fc1bf07a33)
- **YouTube**: [Permutation Algorithm Tutorial](https://www.youtube.com/watch?v=s7AvT7cGdSo)

### Análise da Complexidade

A relação de recorrência é:
```
T(n) = n × T(n-1) + O(n)
```

A solução é:
```
T(n) = O(n!)
```

### Otimizações Implementadas

#### 1. Abordagem In-place Swap
```python
def backtrack(start: int) -> None:
    if start == len(elements_copy):
        result.append(elements_copy[:])
        return
    
    for i in range(start, len(elements_copy)):
        elements_copy[start], elements_copy[i] = elements_copy[i], elements_copy[start]
        backtrack(start + 1)
        elements_copy[start], elements_copy[i] = elements_copy[i], elements_copy[start]
```

#### 2. Tratamento de Duplicatas
```python
freq = Counter(elements)
for num in freq:
    if freq[num] > 0:
        freq[num] -= 1
        current.append(num)
        backtrack(current)
        current.pop()
        freq[num] += 1
```

#### 3. Geração Lexicográfica
```python
def next_permutation() -> bool:
    # Encontra o maior índice k tal que a[k] < a[k + 1]
    k = n - 2
    while k >= 0 and elements_copy[k] >= elements_copy[k + 1]:
        k -= 1
    
    if k < 0:
        return False  # Não há mais permutações
    
    # Encontra o maior índice l tal que a[k] < a[l]
    l = n - 1
    while elements_copy[k] >= elements_copy[l]:
        l -= 1
    
    # Troca a[k] e a[l]
    elements_copy[k], elements_copy[l] = elements_copy[l], elements_copy[k]
    
    # Inverte a sequência de a[k + 1] até a[n - 1]
    left = k + 1
    right = n - 1
    while left < right:
        elements_copy[left], elements_copy[right] = elements_copy[right], elements_copy[left]
        left += 1
        right -= 1
    
    return True
```

#### 4. Restrições
```python
def backtrack(remaining: List, current: List) -> None:
    if not remaining:
        result.append(current[:])
        return
    
    for i in range(len(remaining)):
        chosen = remaining[i]
        current.append(chosen)
        
        # Verifica se a solução parcial pode ser estendida
        if constraint_func(current):
            new_remaining = remaining[:i] + remaining[i+1:]
            backtrack(new_remaining, current)
        
        current.pop()
```

### Testes

Execute os testes com:
```bash
pytest algorithms/backtracking/test_permutation_generation.py
```

Os testes cobrem:
- Casos básicos e casos extremos
- Todas as implementações (backtracking, in-place swap, otimizada)
- Geração com restrições e contagem
- Análise de complexidade
- Performance e correção
- Casos especiais (lista vazia, duplicatas, tipos diferentes)

### Aplicações Práticas

1. **Problemas de Arranjo**: Organizar itens em diferentes ordens
2. **Problemas de Scheduling**: Ordenar tarefas ou eventos
3. **Problemas de Criptografia**: Gerar chaves ou senhas
4. **Problemas de Jogos**: Gerar movimentos ou configurações
5. **Problemas de Otimização**: Explorar todas as ordenações possíveis

### Insights Teóricos

1. **Estrutura de Decisão**: Cada posição escolhe um elemento não utilizado
2. **Exploração Sistemática**: Garante que todas as permutações sejam geradas
3. **Abordagens Alternativas**: In-place swapping vs. lista de restantes
4. **Tratamento de Duplicatas**: Evita permutações idênticas
5. **Base para Outros Problemas**: Fundamento para problemas mais complexos

### Variações do Problema

1. **Permutações com Restrições**: Limitações na ordem dos elementos
2. **Permutações com Duplicatas**: Tratamento de elementos repetidos
3. **Permutações Lexicográficas**: Ordem específica de geração
4. **Permutações Parciais**: k-permutações de n elementos
5. **Permutações Circulares**: Permutações em anel 

## Graph Coloring (Coloração de Grafos)

### Visão Geral

O problema de Coloração de Grafos é um problema NP-completo clássico que envolve atribuir cores aos vértices de um grafo de forma que vértices adjacentes tenham cores diferentes. É uma aplicação direta do backtracking para resolver problemas de satisfação de restrições em grafos.

### Estratégia do Algoritmo

O algoritmo de backtracking funciona da seguinte forma:

1. **Exploração Sistemática**: Para cada vértice, tenta atribuir uma cor de 1 a m
2. **Verificação de Validade**: Verifica se a cor é válida em relação aos vizinhos já coloridos
3. **Backtrack Inteligente**: Se uma atribuição falha, volta e tenta outra cor
4. **Poda por Restrições**: Elimina ramificações inválidas precocemente

### Complexidade

- **Tempo**: O(m^V) - no pior caso, tenta m cores para cada vértice
- **Espaço**: O(V) - profundidade da pilha de recursão
- **NP-Completo**: O problema é NP-completo, mas backtracking é a base para otimizações

### Funções Implementadas

#### `graph_coloring_backtracking(graph, m)`
Resolve o problema de coloração de grafos usando backtracking recursivo básico.

**Parâmetros:**
- `graph`: Matriz de adjacência do grafo (V x V)
- `m`: Número máximo de cores disponíveis

**Retorna:** Lista de cores atribuídas aos vértices (1 a m), ou None se não for possível

#### `graph_coloring_optimized(graph, m)`
Versão otimizada com ordenação de vértices por grau e heurísticas.

#### `graph_coloring_count_solutions(graph, m)`
Conta quantas soluções existem para o problema.

#### `graph_coloring_all_solutions(graph, m)`
Encontra todas as soluções para o problema.

#### `graph_coloring_with_memoization(graph, m)`
Versão com memoização para evitar recálculos.

#### `analyze_graph_coloring_complexity(graph, m)`
Analisa a complexidade do problema para os dados fornecidos.

### Exemplo de Uso

```python
from algorithms.backtracking.graph_coloring import graph_coloring_backtracking

# Exemplo básico
graph = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]
m = 2
result = graph_coloring_backtracking(graph, m)
print(f"Coloração: {result}")  # [1, 2, 1, 2] ou similar

# Exemplo sem solução
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
m = 2
result = graph_coloring_backtracking(graph, m)
print(f"Coloração: {result}")  # None

# Contar soluções
count = graph_coloring_count_solutions(graph, 3)
print(f"Número de soluções: {count}")
```

### Referências

- **InterviewBit**: [Graph Coloring Algorithm using Backtracking](https://www.interviewbit.com/courses/programming/backtracking/graph-coloring-algorithm-using-backtracking/)
- **GeeksforGeeks**: [M-Coloring Problem](https://www.geeksforgeeks.org/dsa/m-coloring-problem-in-python/)
- **TheAlgorithms/Python**: [coloring.py](https://github.com/TheAlgorithms/Python/blob/master/backtracking/coloring.py)
- **CSP Map Coloring**: [CSP-Map-coloring-using-Backtracking](https://github.com/jaiswalchitransh/CSP-Map-coloring-using-Backtracking)

### Análise da Complexidade

A relação de recorrência é:
```
T(V) = m × T(V-1) + O(V)
```

A solução é:
```
T(V) = O(m^V)
```

### Otimizações Implementadas

#### 1. Ordenação por Grau
```python
degrees = [sum(graph[i]) for i in range(V)]
vertex_order = sorted(range(V), key=lambda x: degrees[x], reverse=True)
```
- Colore vértices de maior grau primeiro
- Reduz o número de backtrackings necessários

#### 2. Verificação Eficiente
```python
def is_safe(vertex, color):
    for i in range(V):
        if graph[vertex][i] == 1 and colors[i] == color:
            return False
    return True
```
- Verifica apenas vértices adjacentes
- Early termination quando possível

#### 3. Memoização
```python
def get_state_key(vertex):
    return f"{vertex}:{tuple(colors[:vertex])}"
```
- Evita recálculos de estados já visitados
- Melhora performance para grafos com padrões repetitivos

### Aplicações Práticas

1. **Coloração de Mapas**: Países vizinhos com cores diferentes
2. **Agendamento de Exames**: Exames simultâneos com horários diferentes
3. **Alocação de Registradores**: Variáveis simultâneas em registradores diferentes
4. **Problema do Sudoku**: Células na mesma linha/coluna/bloco com números diferentes
5. **Design de Redes**: Canais de comunicação sem interferência

### Insights Teóricos

1. **Número Cromático**: Menor número de cores necessárias
2. **Grafo Bipartido**: Grafos que podem ser coloridos com 2 cores
3. **Teorema das Quatro Cores**: Qualquer mapa planar pode ser colorido com 4 cores
4. **Heurísticas de Coloração**: Estratégias para melhorar a eficiência
5. **Conexão com CSP**: Problema de Satisfação de Restrições

### Variações do Problema

1. **Coloração de Arestas**: Colorir arestas em vez de vértices
2. **Coloração Lista**: Cada vértice tem uma lista de cores permitidas
3. **Coloração Total**: Colorir vértices e arestas simultaneamente
4. **Coloração com Pesos**: Minimizar custo total das cores usadas
5. **Coloração Online**: Decidir cores sem conhecer o grafo completo

## Hamiltonian Path (Caminho Hamiltoniano)

### Visão Geral

O problema do Caminho Hamiltoniano é um problema NP-completo clássico que envolve encontrar um caminho em um grafo que visite todos os vértices exatamente uma vez. É uma aplicação direta do backtracking para resolver problemas de busca em grafos.

### Estratégia do Algoritmo

O algoritmo de backtracking funciona da seguinte forma:

1. **Exploração Sistemática**: Constrói um caminho passo a passo
2. **Verificação de Adjacência**: Tenta adicionar vértices adjacentes não visitados
3. **Backtrack Inteligente**: Se um caminho não pode ser estendido, volta e tenta outro vizinho
4. **Poda por Visitação**: Elimina vértices já visitados

### Complexidade

- **Tempo**: O(V!) - no pior caso, explora todas as permutações possíveis
- **Espaço**: O(V) - profundidade da pilha de recursão
- **NP-Completo**: O problema é NP-completo, mas backtracking é a base para otimizações

### Funções Implementadas

#### `hamiltonian_path_backtracking(graph)`
Resolve o problema do Caminho Hamiltoniano usando backtracking recursivo básico.

**Parâmetros:**
- `graph`: Matriz de adjacência do grafo (V x V)

**Retorna:** Lista com a ordem dos vértices no caminho Hamiltoniano, ou None se não existir

#### `hamiltonian_cycle_backtracking(graph)`
Resolve o problema do Ciclo Hamiltoniano (caminho que forma um ciclo).

#### `hamiltonian_path_optimized(graph)`
Versão otimizada com ordenação de vértices por grau e heurísticas.

#### `hamiltonian_path_count_solutions(graph)`
Conta quantas soluções existem para o problema.

#### `hamiltonian_path_all_solutions(graph)`
Encontra todas as soluções para o problema.

#### `hamiltonian_path_with_memoization(graph)`
Versão com memoização para evitar recálculos.

#### `analyze_hamiltonian_path_complexity(graph)`
Analisa a complexidade do problema para os dados fornecidos.

### Exemplo de Uso

```python
from algorithms.backtracking.hamiltonian_path import hamiltonian_path_backtracking

# Exemplo básico
graph = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]
result = hamiltonian_path_backtracking(graph)
print(f"Caminho Hamiltoniano: {result}")  # [0, 1, 2, 3] ou similar

# Exemplo sem solução
graph = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]
result = hamiltonian_path_backtracking(graph)
print(f"Caminho Hamiltoniano: {result}")  # None

# Contar soluções
count = hamiltonian_path_count_solutions(graph)
print(f"Número de soluções: {count}")
```

### Referências

- **Wikipedia**: [Hamiltonian path problem](https://en.wikipedia.org/wiki/Hamiltonian_path_problem)
- **HackerEarth**: [Hamiltonian Path Tutorial](https://www.hackerearth.com/practice/algorithms/graphs/hamiltonian-path/tutorial/)
- **TheAlgorithms/Python**: [hamiltonian_cycle.py](https://github.com/TheAlgorithms/Python/blob/master/backtracking/hamiltonian_cycle.py)
- **NetworkX Implementation**: [mikkelam/hamilton.py](https://gist.github.com/mikkelam/ab7966e7ab1c441f947b)

### Análise da Complexidade

A relação de recorrência é:
```
T(V) = V × T(V-1) + O(V)
```

A solução é:
```
T(V) = O(V!)
```

### Otimizações Implementadas

#### 1. Ordenação por Grau
```python
degrees = [sum(graph[i]) for i in range(V)]
vertex_order = sorted(range(V), key=lambda x: degrees[x], reverse=True)
```
- Tenta vértices de maior grau primeiro
- Reduz o número de backtrackings necessários
- Aproveita vértices mais conectados cedo

#### 2. Verificação Eficiente
```python
if (graph[vertex][next_vertex] == 1 and 
    not visited[next_vertex]):
```
- Verifica adjacência e visitação em O(1)
- Early termination quando possível
- Evita tentativas desnecessárias

#### 3. Memoização
```python
def get_state_key(vertex, path_count):
    return f"{vertex}:{path_count}:{tuple(visited)}"
```
- Evita recálculos de estados já visitados
- Melhora performance para grafos com padrões repetitivos
- Trade-off entre tempo e espaço

### Aplicações Práticas

1. **Problema do Caixeiro Viajante (TSP)**: Encontrar rota mais curta visitando todas as cidades
2. **Sequenciamento de DNA**: Reconstruir sequência genética a partir de fragmentos
3. **Design de Circuitos**: Conectar componentes sem cruzar fios
4. **Agendamento de Tarefas**: Ordenar tarefas com dependências
5. **Roteamento de Pacotes**: Encontrar rota ótima em rede de computadores

### Insights Teóricos

1. **Condições Necessárias**: Grau mínimo ≥ 1 para caminho, ≥ 2 para ciclo
2. **Condições Suficientes**: Grafo completo sempre tem caminho Hamiltoniano
3. **Conexão com TSP**: Caminho Hamiltoniano é caso especial do TSP
4. **Heurísticas**: Ordenação por grau melhora performance prática
5. **Conexão com Permutações**: Cada caminho é uma permutação dos vértices

### Variações do Problema

1. **Ciclo Hamiltoniano**: Caminho que forma um ciclo
2. **Caminho Hamiltoniano Direcionado**: Em grafos direcionados
3. **Caminho Hamiltoniano com Pesos**: Minimizar custo total
4. **Caminho Hamiltoniano com Restrições**: Limitações na ordem de visitação
5. **Caminho Hamiltoniano Online**: Decidir sem conhecer o grafo completo