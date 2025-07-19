# 📐 Notação Padrão

## 🔢 Complexidade de Tempo
- **O(1)**: Constante
- **O(log n)**: Logarítmico
- **O(n)**: Linear
- **O(n log n)**: Log-linear
- **O(n²)**: Quadrático
- **O(2ⁿ)**: Exponencial

## 📊 Estruturas de Dados
- **n**: Número de elementos na estrutura
- **size**: Tamanho do array alocado
- **length**: Número de elementos atualmente armazenados
- **i**: Índice de acesso (0 ≤ i < n)

## 🔗 Ponteiros e Referências
- **head**: Ponteiro para primeiro elemento
- **tail**: Ponteiro para último elemento
- **next**: Ponteiro para próximo nó
- **prev**: Ponteiro para nó anterior

## 🏗️ Modelo de Computação
- **w**: Tamanho da palavra da máquina (bits)
- **Word RAM**: Modelo de memória com acesso aleatório
- **θ(n)**: Ordem exata (tanto O(n) quanto Ω(n))

## ⚡ Análise Amortizada
- **Amortizado**: Média sobre sequência de operações
- **Pior caso**: Garantia absoluta para qualquer operação
- **Caso médio**: Esperança sobre distribuição de entrada

## 📋 Operações de Sequência
- **get_at(i)**: Acesso ao elemento na posição i
- **set_at(i, x)**: Modificação do elemento na posição i
- **insert_at(i, x)**: Inserção na posição i
- **delete_at(i)**: Remoção da posição i
- **insert_first(x)**: Inserção no início
- **insert_last(x)**: Inserção no final

## 🗂️ Operações de Set
- **build(A)**: Cria set a partir de iterável A
- **find(k)**: Busca objeto com chave k
- **insert(x)**: Adiciona objeto x ao set
- **delete(k)**: Remove objeto com chave k
- **find_min()**: Menor chave no set
- **find_max()**: Maior chave no set

## 📊 Algoritmos de Ordenação
- **T(n)**: Função de tempo para entrada de tamanho n
- **aT(n/b)**: Recorrência divide-and-conquer
- **f(n)**: Custo de combinação
- **Master Theorem**: Solução para recorrências padrão
- **Ω(n log n)**: Limite inferior para ordenação por comparação
- **u**: Tamanho do universo de chaves (0 ≤ key < u)
- **log_n(u)**: Número de dígitos em base n para representar u
- **n!**: Número de permutações possíveis (fatorial)
