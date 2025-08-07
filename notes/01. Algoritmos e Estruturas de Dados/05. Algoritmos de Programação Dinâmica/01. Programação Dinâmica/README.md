# 🧠 Programação Dinâmica

## 🎯 Visão Geral

Programação Dinâmica (PD) é uma técnica de otimização que resolve problemas complexos quebrando-os em subproblemas menores e armazenando as soluções desses subproblemas para evitar recálculos. A filosofia central é que **"PD é recursão inteligente"**.

## 📚 Conteúdo

### 01. [Conceitos Fundamentais](./01.%20Conceitos%20Fundamentais.md)
- **Filosofia Central**: PD como otimização de algoritmos recursivos
- **Memoização vs Tabulação**: Abordagens top-down e bottom-up
- **Identificação de Subproblemas**: Como quebrar problemas complexos
- **Aplicações**: Transição de força bruta para eficiência

### 02. [Problema do Corte de Barras](./02.%20Problema%20do%20Corte%20de%20Barras.md)
- **Problema Clássico**: Maximizar lucro cortando barras de diferentes tamanhos
- **Subestrutura Ótima**: Propriedade fundamental da PD
- **Memoização**: Cache para evitar recálculos
- **Aplicações**: Indústria de corte de materiais

### 03. [Elementos Fundamentais](./03.%20Elementos%20Fundamentais.md)
- **Subestrutura Ótima**: Propriedade que permite decomposição
- **Sobreposição de Subproblemas**: Justificativa para cache
- **Memoização**: Armazenamento de resultados intermediários
- **Tabelação**: Construção iterativa da tabela de soluções

### 04. [Árvores Binárias de Busca Ótimas](./04.%20Árvores%20Binárias%20de%20Busca%20Ótimas.md)
- **Problema de Otimização**: Construir BST com custo mínimo de busca
- **Frequências de Acesso**: Consideração de probabilidades
- **Algoritmo de Knuth**: Otimização da construção da tabela
- **Aplicações**: Compiladores, sistemas de arquivos

### 05. [Soma de Subconjuntos com Memoização](./05.%20Soma%20de%20Subconjuntos%20com%20Memoização.md)
- **Transição Fundamental**: De O(2^n) para O(n·T) pseudo-polinomial
- **Estado (i, t)**: "Existe subconjunto de X[i..n] que soma t?"
- **Cache Inteligente**: Memoização para evitar recálculos exponenciais
- **Recursão Inteligente**: PD como otimização de backtracking

### 06. [Segmentação de Texto com Memoização](./06.%20Segmentação%20de%20Texto%20com%20Memoização.md) ⭐ NOVO
- **Transição Fundamental**: De O(2^n) para O(n²) quadrático
- **Estado (i)**: "O sufixo text[i..n] pode ser segmentado?"
- **Subproblemas Sobrepostos**: Múltiplos caminhos para o mesmo estado
- **Aplicações**: Processamento de texto, compiladores, NLP

### 07. [LIS com Memoização](./07.%20LIS%20com%20Memoização.md) ⭐ NOVO
- **Transição Fundamental**: De O(2^n) para O(n²) quadrático
- **Estado (i, j)**: "LIS começando em i com anterior em j" (LISbigger)
- **Formulação de Erickson**: "First Recurrence: Is This Next?"
- **Aplicações**: Análise de sequências, otimização, crescimento

## 🎯 Conceitos-Chave

### 🔄 Filosofia da PD
- **"PD é Recursão Inteligente"**: Não é técnica nova, mas otimização
- **Transição Suave**: Mantém estrutura lógica da recursão original
- **Cache Inteligente**: Adiciona cache para evitar recálculos
- **Identificação de Estado**: Representação única de subproblemas

### ⚡ Abordagens Fundamentais
- **Memoização (Top-Down)**: Cache de resultados durante recursão
- **Tabelação (Bottom-Up)**: Construção iterativa da tabela de soluções
- **Subestrutura Ótima**: Propriedade que permite decomposição
- **Sobreposição de Subproblemas**: Justificativa para cache

### 📊 Análise de Complexidade
- **Pseudo-Polinomial**: O(n·T) onde T é valor alvo
- **Melhoria Exponencial**: Reduz O(2^n) para O(n·T)
- **Trade-off Memória-Tempo**: Cache vs recálculos
- **Identificação de Estado**: Chave para eficiência

## 🚀 Aplicações Práticas
- **Problemas de Otimização**: Knapsack, corte de barras, BST ótimas
- **Problemas de Sequência**: LCS, LIS, edit distance
- **Problemas de Caminho**: Shortest path, longest path
- **Problemas de Partição**: Subset sum, partition, coin change
- **Problemas de Scheduling**: Job scheduling, resource allocation

## 💡 Insights Teóricos
- **Transição Fundamental**: De força bruta para eficiência
- **Identificação de Estado**: Chave para decomposição correta
- **Memoização vs Tabulação**: Trade-offs entre abordagens
- **Subestrutura Ótima**: Propriedade fundamental para PD
- **Sobreposição de Subproblemas**: Justificativa para cache
- **Complexidade Pseudo-Polinomial**: Limitação e vantagem
- **Recursão Inteligente**: PD como otimização de algoritmos recursivos
- **Cache Eficiente**: Armazenamento de resultados intermediários

## 🔗 Referências

- **Erickson, "Algorithms"**: Capítulo 3, "Dynamic Programming"
- **Jeff Erickson**: [Dynamic Programming Chapter](https://jeffe.cs.illinois.edu/teaching/algorithms/book/03-dynprog.pdf)
- **Research Papers**: Análise de complexidade e otimizações
- **Implementações**: Código de referência e exemplos práticos 