# 🔄 Algoritmos Recursivos

## 🎯 Visão Geral
Fundamentos de algoritmos recursivos: desde multiplicação rápida até ordenação, com foco em **divide-and-conquer** e análise de recorrências.

## 📚 Conteúdo

### 01. [Merge Sort](./01.%20Merge%20Sort.md)
- **Divide-and-Conquer**: Estratégia fundamental de divisão
- **Two-Finger Merge**: Algoritmo eficiente de combinação
- **Análise**: O(n log n) com recorrência T(n) = 2T(n/2) + O(n)
- **Variações**: In-place, natural, iterativo

### 02. [Fast Multiplication](./02.%20Fast%20Multiplication.md)
- **Karatsuba Algorithm**: Multiplicação O(n^1.585) vs O(n²)
- **Binary Exponentiation**: Potenciação O(log n) vs O(n)
- **Divide-and-Conquer**: Quebrando problemas grandes em menores
- **Aplicações**: Criptografia, computação científica

### 03. [Tower of Hanoi](./03.%20Tower%20Hanoi.md)
- **Problema Clássico**: Mover discos entre torres
- **Solução Recursiva**: Estratégia de 3 passos
- **Análise**: 2^n - 1 movimentos mínimos
- **Insights**: Padrão fundamental de recursão

### 04. [Count Inversions](./04.%20Count%20Inversions.md)
- **Problema**: Contar pares (i,j) onde i < j e A[i] > A[j]
- **Solução**: Adaptação do Merge Sort
- **Aplicações**: Análise de similaridade, ordenação
- **Complexidade**: O(n log n) tempo e espaço

### 05. [Quickselect](./05.%20Quickselect.md)
- **Seleção Linear**: Encontrar k-ésimo elemento em tempo médio O(n)
- **Particionamento**: Adaptação inteligente do Quicksort
- **Redução**: Recursão apenas no lado relevante
- **Aplicações**: Mediana, percentis, estatísticas

### 06. [Median of Medians](./06.%20Median%20of%20Medians.md)
- **BFPRT Algorithm**: Seleção determinística em tempo linear
- **Pivô Garantido**: Entre 30º e 70º percentil
- **Complexidade**: O(n) no pior caso garantido
- **Marco Teórico**: Limite fundamental para algoritmos de seleção

### 07. [Min-Max Finder](./07.%20Min-Max%20Finder.md)
- **Otimização de Algoritmos**: Redução de 25% nas comparações
- **Abordagem de Pares**: Processamento inteligente em pares
- **Método do Torneio**: Simulação de torneio de eliminação
- **Análise Comparativa**: Trade-offs entre diferentes estratégias

## 🎯 Conceitos-Chave

### 🔄 Recursão vs Iteração
- **Recursão**: Solução natural para problemas dividíveis
- **Base Case**: Condição de parada essencial
- **Stack Space**: Custo da pilha de recursão
- **Tail Recursion**: Otimização para evitar stack overflow

### ⚡ Divide-and-Conquer
- **Divide**: Quebrar problema em subproblemas menores
- **Conquer**: Resolver subproblemas recursivamente
- **Combine**: Juntar soluções dos subproblemas
- **Recorrência**: T(n) = aT(n/b) + f(n)

### 📊 Análise de Recorrências
- **Substituição**: Método direto de prova
- **Master Theorem**: Solução automática para casos padrão
- **Recursion Tree**: Visualização do processo
- **Indução**: Prova de correção matemática

## 🚀 Aplicações Práticas
- **Ordenação**: Merge Sort em linguagens de programação
- **Criptografia**: Multiplicação rápida em RSA
- **Computação Científica**: Potenciação em simulações
- **Análise de Dados**: Contagem de inversões para similaridade
- **Estatística**: Quickselect para medianas e percentis
- **Sistemas de Tempo Real**: BFPRT para seleção determinística

## 💡 Insights Teóricos
- **Recursão**: Estrutura natural para problemas dividíveis
- **Master Theorem**: Ferramenta poderosa para análise
- **Logaritmo**: Resultado natural de divisão binária
- **Exponencial**: Crescimento típico de problemas recursivos
- **Memoização**: Técnica para evitar recálculos
- **Backtracking**: Exploração sistemática de possibilidades
- **Fé Recursiva**: Acreditar que subproblemas "simplesmente funcionam"
- **Redução de Problemas**: Transformar problemas complexos em menores
- **Limites Teóricos**: BFPRT como marco fundamental da seleção 