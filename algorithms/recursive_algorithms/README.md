# Algoritmos Recursivos

Este módulo contém implementações de algoritmos recursivos fundamentais, demonstrando o conceito da "fé recursiva" e estratégias de divisão e conquista.

## Torre de Hanói

### Visão Geral

A Torre de Hanói é o exemplo canônico da recursão, demonstrando o conceito fundamental da "fé recursiva": acreditar que a solução para um subproblema simplesmente funciona.

### Estratégia Recursiva

Para mover n discos da origem para o destino:

1. **Mover recursivamente** n-1 discos da origem para o pino auxiliar
2. **Mover o disco n** da origem para o destino
3. **Mover recursivamente** n-1 discos do pino auxiliar para o destino

### Complexidade

- **Tempo**: O(2^n) - exponencial devido à natureza do problema
- **Espaço**: O(n) - altura da pilha de recursão

### Funções Implementadas

#### `tower_of_hanoi(n, source, destination, auxiliary)`
Resolve o quebra-cabeça da Torre de Hanói recursivamente.

**Parâmetros:**
- `n`: Número de discos
- `source`: Pino de origem (ex: 'A')
- `destination`: Pino de destino (ex: 'C')
- `auxiliary`: Pino auxiliar (ex: 'B')

**Retorna:** Lista de movimentos no formato "Mover disco X do pino Y para o pino Z"

#### `count_moves(n)`
Calcula o número mínimo de movimentos necessários.

**Fórmula:** 2^n - 1

#### `tower_of_hanoi_iterative(n, source, destination, auxiliary)`
Versão iterativa usando pilha para simular a recursão.

#### `validate_tower_state(pegs)`
Valida se um estado das torres é válido (discos em ordem decrescente).

### Exemplo de Uso

```python
from algorithms.recursive_algorithms.tower_of_hanoi import tower_of_hanoi

# Resolver para 3 discos
moves = tower_of_hanoi(3, 'A', 'C', 'B')
for move in moves:
    print(move)

# Saída:
# Mover disco 1 do pino A para o pino C
# Mover disco 2 do pino A para o pino B
# Mover disco 1 do pino C para o pino B
# Mover disco 3 do pino A para o pino C
# Mover disco 1 do pino B para o pino A
# Mover disco 2 do pino B para o pino C
# Mover disco 1 do pino A para o pino C
```

### Referências

- **Erickson, "Algorithms"**: Capítulo 1, Seção 1.3, "Tower of Hanoi"
- **HackerEarth**: [Tower of Hanoi recursion game algorithm explained](https://www.hackerearth.com/blog/tower-hanoi-recursion-game-algorithm-explained/)
- **Lancaster University**: [Solving the Tower of Hanoi puzzle using recursion](https://www.lancaster.ac.uk/stor-i-student-sites/jack-trainer/solving-the-tower-of-hanoi-puzzle-using-recursion/)

### Análise da Complexidade

A relação de recorrência é:
```
T(n) = 2T(n-1) + 1
```

A solução fechada é:
```
T(n) = 2^n - 1
```

### Propriedades Matemáticas

- O número mínimo de movimentos para n discos é sempre 2^n - 1
- Para 64 discos (como na lenda), seriam necessários 2^64 - 1 movimentos
- Se os sacerdotes movessem 1 disco por segundo, levariam aproximadamente 580 bilhões de anos

### Variações Implementadas

1. **Versão Recursiva Clássica**: Demonstra a "fé recursiva" em sua forma mais pura
2. **Versão Iterativa**: Usa pilha para simular a recursão
3. **Validação de Estados**: Verifica se uma configuração das torres é válida
4. **Cálculo de Movimentos**: Implementa a fórmula matemática diretamente

### Testes

Execute os testes com:
```bash
pytest algorithms/recursive_algorithms/test_tower_of_hanoi.py
```

Os testes cobrem:
- Casos básicos (0, 1, 2, 3 discos)
- Casos extremos (números negativos, pinos iguais)
- Validação de estados
- Consistência entre versões recursiva e iterativa
- Performance com números grandes

## Contagem de Inversões

### Visão Geral

A contagem de inversões é uma aplicação clássica do paradigma de divisão e conquista, demonstrando como adaptar o Mergesort para resolver problemas além da ordenação. Uma inversão é um par de índices (i,j) tal que i < j e A[i] > A[j].

### Estratégia do Algoritmo

O algoritmo eficiente O(n log n) baseia-se na observação de que, durante a mesclagem de duas sub-listas ordenadas, se um elemento da sub-lista direita é movido para o array final antes de um elemento da sub-lista esquerda, então este elemento da direita forma uma inversão com todos os elementos restantes na sub-lista esquerda.

### Complexidade

- **Força Bruta**: O(n²) - verificação de todos os pares
- **Mergesort Modificado**: O(n log n) - mesma do Mergesort
- **Fenwick Tree**: O(n log n) - para arrays com valores em intervalo conhecido

### Funções Implementadas

#### `count_inversions_brute_force(arr)`
Conta inversões usando força bruta - O(n²).

#### `count_inversions_merge_sort(arr)`
Conta inversões usando variação do Mergesort - O(n log n).

#### `count_inversions_fenwick_tree(arr)`
Conta inversões usando Fenwick Tree - O(n log n).

#### `find_inversion_pairs(arr)`
Encontra todos os pares de inversões (i, j).

#### `validate_inversion_count(arr, count)`
Valida se a contagem de inversões está correta.

### Exemplo de Uso

```python
from algorithms.recursive_algorithms.count_inversions import count_inversions_merge_sort

# Contar inversões
arr = [8, 4, 2, 1]
inversions = count_inversions_merge_sort(arr)
print(f"Número de inversões: {inversions}")

# Saída: Número de inversões: 6
```

### Referências

- **Erickson, "Algorithms"**: Capítulo 1, Exercício 13
- **GeeksforGeeks**: [Python Program for Count Inversions](https://www.geeksforgeeks.org/python/python-program-for-count-inversions-in-an-array-set-1-using-merge-sort/)
- **TheAlgorithms**: [Inversions Implementation](https://github.com/TheAlgorithms/Python/blob/master/divide_and_conquer/inversions.py)

### Testes

Execute os testes com:
```bash
pytest algorithms/recursive_algorithms/test_count_inversions.py
```

Os testes cobrem:
- Casos básicos (arrays vazios, um elemento, dois elementos)
- Casos complexos (arrays ordenados, reversos, com duplicatas)
- Consistência entre diferentes algoritmos
- Performance com arrays grandes
- Validação de resultados

## Merge Sort

### Visão Geral

Mergesort é o exemplo por excelência de um algoritmo de divisão e conquista. Sua complexidade de tempo garantida de O(n log n) o torna superior ao Quicksort no pior caso, embora sua necessidade de espaço auxiliar O(n) possa ser uma limitação em ambientes com memória restrita.

### Estratégia do Algoritmo

1. **Dividir**: Dividir o array em duas metades aproximadamente iguais
2. **Conquistar**: Ordenar recursivamente as duas metades
3. **Combinar**: Mesclar as duas metades ordenadas em um único array ordenado

### Complexidade

- **Tempo**: O(n log n) - garantido para todos os casos
- **Espaço**: O(n) - array auxiliar para mesclagem
- **Estável**: Sim - mantém a ordem relativa de elementos iguais

### Funções Implementadas

#### `merge_sort(arr)`
Implementa o algoritmo Mergesort clássico.

#### `merge_sort_inplace(arr)`
Versão que modifica a lista original in-place.

#### `merge_sort_iterative(arr)`
Versão iterativa usando abordagem bottom-up.

#### `merge_sort_optimized(arr)`
Versão otimizada com melhorias de performance:
- Usar insertion sort para sub-listas pequenas
- Verificar se as sub-listas já estão ordenadas
- Usar array auxiliar reutilizável

#### `natural_merge_sort(arr)`
Natural Mergesort que aproveita sequências já ordenadas.

#### `merge_sort_parallel(arr, num_threads)`
Versão paralela usando múltiplas threads.

#### `merge_sort_with_comparison_count(arr)`
Retorna também o número de comparações realizadas.

#### `count_inversions_merge_sort(arr)`
Conta inversões usando modificação do Mergesort.

### Exemplo de Uso

```python
from algorithms.recursive_algorithms.merge_sort import merge_sort

# Ordenar array
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print(sorted_arr)

# Saída: [11, 12, 22, 25, 34, 64, 90]

# Versão in-place
merge_sort_inplace(arr)
print(arr)

# Saída: [11, 12, 22, 25, 34, 64, 90]
```

### Referências

- **Erickson, "Algorithms"**: Capítulo 1, Seção 1.4, "Mergesort"
- **TheAlgorithms**: [Merge Sort Implementation](https://github.com/TheAlgorithms/Python/blob/master/sorts/merge_sort.py)
- **HackerEarth**: [Merge Sort Visualization](https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/visualize/)
- **GeeksforGeeks**: [Merge Sort Tutorial](https://www.geeksforgeeks.org/dsa/merge-sort/)

### Variações Implementadas

1. **Versão Recursiva Clássica**: Demonstra o paradigma de divisão e conquista
2. **Versão In-place**: Modifica a lista original sem criar cópias
3. **Versão Iterativa**: Usa abordagem bottom-up para evitar recursão
4. **Versão Otimizada**: Inclui várias otimizações de performance
5. **Natural Merge Sort**: Aproveita sequências já ordenadas
6. **Versão Paralela**: Utiliza múltiplas threads para melhor performance
7. **Contagem de Comparações**: Útil para análise de complexidade
8. **Contagem de Inversões**: Demonstra adaptabilidade do algoritmo

### Testes

Execute os testes com:
```bash
pytest algorithms/recursive_algorithms/test_merge_sort.py
```

Os testes cobrem:
- Casos básicos (arrays vazios, um elemento, múltiplos elementos)
- Casos complexos (arrays ordenados, reversos, com duplicatas)
- Todas as variações implementadas
- Consistência entre diferentes implementações
- Performance com arrays grandes
- Validação de resultados ordenados

## Quickselect

### Visão Geral

O Quickselect é uma aplicação brilhante da ideia de particionamento do Quicksort. Em vez de recursão em ambos os lados do pivô, ele descarta um lado e continua a busca apenas na partição que deve conter o k-ésimo elemento. Isso reduz a complexidade média de O(n log n) para O(n), tornando-o um dos algoritmos de seleção mais eficientes na prática.

### Estratégia Recursiva

1. **Particionar** o array usando um pivô
2. **Comparar** a posição do pivô com k
3. **Recursão** apenas no lado que contém o k-ésimo elemento
4. **Base case**: quando o pivô está na posição k

### Complexidade

- **Tempo Médio**: O(n) - linear devido à redução do problema
- **Tempo Pior Caso**: O(n²) - quando o pivô é sempre o menor/maior
- **Espaço**: O(log n) - altura da pilha de recursão

### Funções Implementadas

#### `quickselect(arr, k)`
Encontra o k-ésimo menor elemento em tempo médio linear.

**Parâmetros:**
- `arr`: Lista de números inteiros
- `k`: Índice do elemento desejado (1-indexed)

**Retorna:** O k-ésimo menor elemento

#### `partition(arr, left, right)`
Particiona o array usando o último elemento como pivô.

#### `quickselect_median_of_three(arr, k)`
Usa a mediana de três como estratégia de pivô para melhor performance.

#### `find_kth_largest(arr, k)`
Encontra o k-ésimo maior elemento usando Quickselect.

#### `find_median(arr)`
Encontra a mediana de um array usando Quickselect.

### Exemplo de Uso

```python
from algorithms.recursive_algorithms.quickselect import quickselect

# Encontrar o 3º menor elemento
arr = [3, 2, 1, 5, 6, 4]
result = quickselect(arr, 3)
print(result)  # Saída: 3

# Encontrar a mediana
from algorithms.recursive_algorithms.quickselect import find_median
median = find_median([1, 3, 2, 5, 4])
print(median)  # Saída: 3.0
```

### Referências

- **Erickson, "Algorithms"**: Capítulo 1, Seção 1.8, "Linear-Time Selection"
- **GitHub**: [QuickSelect Implementation](https://github.com/alnakschbandi/QuickSelect)
- **Reddit**: [Quickselect complexity analysis](https://www.reddit.com/r/leetcode/comments/1hpbsx8/how_is_quickselect_on_when_quicksort_is_0nlogn/)

### Análise da Complexidade

A relação de recorrência é:
```
T(n) = T(n/2) + O(n)
```

A solução é:
```
T(n) = O(n)
```

### Variações Implementadas

1. **Versão Recursiva Clássica**: Demonstra a estratégia fundamental
2. **Pivô Aleatório**: Garante complexidade linear esperada
3. **Mediana de Três**: Melhora a escolha do pivô
4. **Versão Iterativa**: Evita overhead de recursão
5. **Tratamento de Duplicatas**: Lida com elementos repetidos
6. **Versão Paralela**: Aproveita múltiplas threads

### Testes

Execute os testes com:
```bash
pytest algorithms/recursive_algorithms/test_quickselect.py
```

Os testes cobrem:
- Casos básicos (arrays pequenos, diferentes valores de k)
- Casos com duplicatas e elementos repetidos
- Validação de resultados e consistência entre implementações
- Performance e análise de complexidade
- Casos extremos (arrays grandes, valores extremos)

## Mediana das Medianas (BFPRT)

### Visão Geral

O algoritmo Mediana das Medianas (Blum-Floyd-Pratt-Rivest-Tarjan) é um marco teórico que garante tempo linear no pior caso para o problema de seleção. Na prática, a constante oculta na notação O(n) é alta, tornando o Quickselect com pivô aleatório mais rápido para a maioria das entradas, mas a compreensão deste algoritmo é crucial para um domínio completo da análise de algoritmos de divisão e conquista.

### Estratégia do Algoritmo

1. **Dividir** o array em grupos de 5 elementos
2. **Encontrar** a mediana de cada grupo (usando ordenação)
3. **Recursão** para encontrar a mediana das medianas
4. **Particionar** o array ao redor da mediana das medianas
5. **Recursão** apenas no lado relevante

### Complexidade

- **Tempo**: O(n) - garantido no pior caso
- **Espaço**: O(n) - devido à recursão
- **Constante**: Alta (aproximadamente 3-4 vezes maior que Quickselect)

### Funções Implementadas

#### `median_of_medians_select(arr, k)`
Encontra o k-ésimo menor elemento usando o algoritmo BFPRT.

**Parâmetros:**
- `arr`: Lista de números inteiros
- `k`: Índice do elemento desejado (1-indexed)

**Retorna:** O k-ésimo menor elemento

#### `find_median_of_medians(arr, left, right)`
Encontra a mediana das medianas usando o algoritmo BFPRT.

#### `median_of_five(arr, left, right)`
Encontra a mediana de cinco elementos usando ordenação.

#### `partition_around_pivot(arr, left, right, pivot_index)`
Particiona o array ao redor do pivô especificado.

#### `find_median_using_mom(arr)`
Encontra a mediana usando o algoritmo Mediana das Medianas.

### Exemplo de Uso

```python
from algorithms.recursive_algorithms.median_of_medians import median_of_medians_select

# Encontrar o 3º menor elemento
arr = [3, 2, 1, 5, 6, 4]
result = median_of_medians_select(arr, 3)
print(result)  # Saída: 3

# Encontrar a mediana
from algorithms.recursive_algorithms.median_of_medians import find_median_using_mom
median = find_median_using_mom([1, 3, 2, 5, 4])
print(median)  # Saída: 3.0
```

### Referências

- **Erickson, "Algorithms"**: Capítulo 1, Seção 1.8, "MOMSELECT"
- **TheAlgorithms**: [Median of Medians Implementation](https://github.com/TheAlgorithms/Python/blob/master/searches/median_of_medians.py)
- **Wikipedia**: [Median of medians](https://en.wikipedia.org/wiki/Median_of_medians)

### Análise da Complexidade

A relação de recorrência é:
```
T(n) ≤ T(n/5) + T(7n/10) + O(n)
```

A solução é:
```
T(n) = O(n)
```

### Variações Implementadas

1. **Versão Recursiva Clássica**: Demonstra a estratégia fundamental
2. **Mediana de Cinco**: Encontra mediana de grupos de 5 elementos
3. **Partição ao Redor do Pivô**: Particiona o array adequadamente
4. **Versão Otimizada**: Inclui otimizações de performance
5. **Versão Paralela**: Aproveita múltiplas threads
6. **Tratamento de Duplicatas**: Lida com elementos repetidos

### Testes

Execute os testes com:
```bash
pytest algorithms/recursive_algorithms/test_median_of_medians.py
```

Os testes cobrem:
- Casos básicos (arrays pequenos, diferentes valores de k)
- Qualidade do pivô escolhido (deve estar entre 30º e 70º percentil)
- Validação de resultados e consistência entre implementações
- Análise de complexidade e limites teóricos
- Comparação com Quickselect
- Casos extremos (arrays grandes, valores extremos)

## Min-Max Finder

### Visão Geral

O problema de encontrar o elemento mínimo e máximo em um array é um exemplo clássico de como a reestruturação inteligente pode reduzir o número de operações fundamentais. A abordagem ingênua requer 2n-2 comparações, mas usando estratégias de divisão e conquista ou processamento em pares, podemos reduzir para aproximadamente 3n/2 comparações, uma melhoria de 25%.

### Estratégias Implementadas

1. **Abordagem Ingênua**: 2n-2 comparações - compara cada elemento com min e max
2. **Abordagem de Pares**: 3n/2 comparações - processa elementos em pares
3. **Divisão e Conquista**: 3n/2 comparações - método do torneio
4. **Método do Torneio**: Simula um torneio de eliminação

### Complexidade

- **Abordagem Ingênua**: O(n) com 2n-2 comparações
- **Abordagem de Pares**: O(n) com 3n/2 comparações
- **Divisão e Conquista**: O(n) com 3n/2 comparações
- **Método do Torneio**: O(n) com estrutura de torneio

### Funções Implementadas

#### `find_min_max_naive(arr)`
Implementa a abordagem ingênua para encontrar mínimo e máximo.

#### `find_min_max_pairs(arr)`
Implementa a abordagem de pares otimizada.

#### `find_min_max_divide_conquer(arr)`
Implementa a abordagem de divisão e conquista.

#### `find_min_max_tournament(arr)`
Implementa o método do torneio.

#### `find_min_max_with_comparison_count(arr)`
Retorna também o número de comparações realizadas.

#### `validate_min_max_result(arr, result)`
Valida se o resultado está correto.

### Exemplo de Uso

```python
from algorithms.recursive_algorithms.min_max_finder import find_min_max_pairs

# Encontrar mínimo e máximo
arr = [3, 2, 1, 5, 6, 4]
min_val, max_val = find_min_max_pairs(arr)
print(f"Mínimo: {min_val}, Máximo: {max_val}")

# Saída: Mínimo: 1, Máximo: 6
```

### Referências

- **Stack Overflow**: [How to find max and min using minimum comparisons](https://stackoverflow.com/questions/13544476/how-to-find-max-and-min-in-array-using-minimum-comparisons)
- **dyclassroom**: [Tournament Method](https://dyclassroom.com/programming/find-the-minimum-and-maximum-number-in-an-array-using-tournament-method)
- **AfterAcademy**: [Find minimum and maximum value](https://afteracademy.com/blog/find-the-minimum-and-maximum-value/)

### Análise da Complexidade

A abordagem de pares funciona assim:
1. **Comparar elementos em pares**: n/2 comparações
2. **Comparar menores com min global**: n/2 comparações  
3. **Comparar maiores com max global**: n/2 comparações
4. **Total**: 3n/2 comparações

### Variações Implementadas

1. **Abordagem Ingênua**: Demonstra a solução direta
2. **Abordagem de Pares**: Processamento inteligente em pares
3. **Divisão e Conquista**: Método recursivo elegante
4. **Método do Torneio**: Simulação de torneio de eliminação
5. **Versão Otimizada**: Escolhe a melhor estratégia
6. **Versão Paralela**: Aproveita múltiplas threads
7. **Contagem de Comparações**: Análise de eficiência
8. **Validação de Resultados**: Verificação de correção

### Testes

Execute os testes com:
```bash
pytest algorithms/recursive_algorithms/test_min_max_finder.py
```

Os testes cobrem:
- Casos básicos (arrays vazios, um elemento, múltiplos elementos)
- Casos complexos (arrays ordenados, reversos, com duplicatas)
- Todas as variações implementadas
- Consistência entre diferentes implementações
- Performance e análise de complexidade
- Casos extremos (arrays grandes, valores extremos)
- Validação de resultados e limites teóricos 