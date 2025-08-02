# 📊 Algoritmos de Ordenação

## 🎯 Visão Geral
Fundamentos de algoritmos de ordenação: desde algoritmos simples até implementações eficientes, com foco em análise de complexidade e aplicações práticas.

## 📚 Conteúdo

### 01. [Set Interface](./01.%20Set%20Interface.md)
- **Interface vs Implementação**: Separação conceitual
- **Operações de Set**: Build, find, insert, delete
- **Conceito de Chave**: Separação entre objeto e chave de busca

### 02. [Problema de Ordenação](./02.%20Problema%20de%20Ordenação.md)
- **Definição**: Input, output e tipos de algoritmos
- **Motivação**: Por que ordenar para implementar sets eficientes
- **Trade-offs**: Arrays ordenados vs não ordenados

### 03. [Selection Sort](./03.%20Selection%20Sort.md)
- **Estratégia**: Seleciona maior elemento e coloca no final
- **Implementação Recursiva**: Prefix max e selection sort
- **Análise**: O(n²) com prova por substituição

### 04. [Merge Sort](../04.%20Algoritmos%20Recursivos/01.%20Merge%20Sort.md)
- **Divide-and-Conquer**: Estratégia fundamental
- **Two-Finger Merge**: Algoritmo eficiente de combinação
- **Análise**: O(n log n) com recorrência

### 05. [Comparação de Algoritmos](./05.%20Comparação%20de%20Algoritmos.md)
- **Tabela Completa**: Complexidade de todos algoritmos
- **Trade-offs**: Velocidade, espaço, estabilidade
- **Aplicações Práticas**: Implementações em linguagens

### 06. [Ordenação Linear](./06.%20Ordenação%20Linear.md)
- **Quebrando Limites**: Algoritmos O(n) usando acesso aleatório
- **Direct Access Array**: Ordenação por indexação direta
- **Counting Sort**: Extensão para chaves duplicadas
- **Radix Sort**: Ordenação por dígitos para números grandes

### 07. [Radix Sort](./07.%20Radix%20Sort.md)
- **Implementação Detalhada**: Pseudocódigo e código Python
- **Análise Completa**: Complexidade tempo/espaço
- **Exemplo Passo a Passo**: Demonstração visual do algoritmo
- **Variações**: MSD, base mista, ordenação de strings
- **Aplicações Práticas**: Casos de uso reais

### 08. [Tuple Sort](./08.%20Tuple%20Sort.md)
- **Ordenação por Múltiplas Chaves**: Estratégia de priorização
- **Implementação Completa**: Pseudocódigo e código Python
- **Relação com Radix Sort**: Conceito unificado
- **Aplicações Práticas**: Planilhas, bancos de dados
- **Análise de Complexidade**: O(k × (n + u))

### 09. [Counting Sort](./09.%20Counting%20Sort.md)
- **Algoritmo Estável**: Ordenação por contagem
- **Implementação Detalhada**: Versões simples e avançadas
- **Variações**: Objetos, strings, faixas específicas
- **Análise Completa**: O(n + u) tempo e espaço
- **Aplicações**: Algoritmo auxiliar para outros sorts

### 10. [Quicksort](./10.%20Quicksort.md)
- **Divide-and-Conquer**: Estratégia fundamental de ordenação
- **Partição de Lomuto**: Escolhe último elemento como pivô
- **Análise Probabilística**: O(n log n) no caso médio
- **Otimizações**: Mediana de 3, three-way partition
- **Aplicações**: Ordenação geral, sistemas em tempo real

## 🎯 Conceitos-Chave

### 🔧 Interface vs Estrutura
- **Set Interface**: Especificação das operações desejadas
- **Implementações**: Diferentes estruturas para mesma interface
- **Trade-offs**: Escolha baseada no padrão de uso

### ⚡ Complexidade de Algoritmos
- **Selection Sort**: O(n²) - simples mas lento
- **Merge Sort**: O(n log n) - eficiente e estável
- **Limite Teórico**: Ω(n log n) para comparação
- **Ordenação Linear**: O(n) - quebrando limites com restrições

### 📊 Análise de Recorrências
- **Substituição**: Método para resolver recorrências
- **Master Theorem**: Solução automática para casos padrão
- **Indução**: Prova de correção de algoritmos recursivos

## 🚀 Aplicações Práticas
- **Implementações de Linguagens**: Python, Java, C++
- **Bancos de Dados**: Índices ordenados
- **Sistemas de Arquivos**: Organização de dados
- **Análise de Dados**: Estatísticas ordenadas

## 💡 Insights Teóricos
- **Divide-and-Conquer**: Padrão fundamental em algoritmos
- **Recursão**: Estrutura natural para análise
- **Estabilidade**: Importância em aplicações práticas
- **Híbridos**: Combinação de algoritmos para otimização
- **Modelos de Computação**: Comparação vs acesso aleatório
- **Decomposição**: Quebrar problemas grandes em menores 