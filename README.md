# Repositório de Estudos em Ciência da Computação

## Visão Geral do Projeto

Este repositório tem como objetivo auxiliar nos estudos aprofundados de **ciência da computação** em Python, especialmente visando entrevistas técnicas para **Software Engineering** e desenvolvimento de carreira. A ideia é criar um ambiente semelhante a plataformas de desafios (como HackerRank ou LeetCode), porém totalmente local e personalizado, cobrindo múltiplas áreas da computação.

Um **agente (IA)** irá gerar automaticamente desafios de programação a partir de conceitos dados, incluindo casos de teste automatizados e esboços de soluções (com partes faltando para o praticante implementar). Dessa forma, será possível praticar diferentes tópicos, entender *trade-offs* e aprimorar a implementação em Python com foco em desempenho e boas práticas.

## Áreas de Estudo

### 🧮 Algoritmos e Estruturas de Dados
- **Estruturas de dados fundamentais**: Arrays, listas ligadas, pilhas, filas, árvores, grafos
- **Algoritmos de ordenação e busca**: Quicksort, mergesort, busca binária, etc.
- **Algoritmos de grafos**: BFS, DFS, Dijkstra, algoritmos de caminho mínimo
- **Programação dinâmica**: Problemas clássicos como mochila, corte de barras, LCS
- **Estruturas avançadas**: Árvores AVL, Red-Black, heaps, tries

### 🤖 Machine Learning
- **Algoritmos fundamentais**: Regressão linear, classificação, clustering
- **Otimização**: Gradiente descendente, algoritmos de otimização
- **Validação**: Cross-validation, métricas de avaliação
- **Feature engineering**: Seleção de features, normalização, encoding
- **Modelos supervisionados**: KNN, SVM, Random Forest, Neural Networks básicos
- **Modelos não supervisionados**: K-means, DBSCAN, PCA

### 🌐 Sistemas Distribuídos
- **Comunicação entre processos**: Sockets, RPC, message queues
- **Consistência de dados**: CAP theorem, consistência eventual, strong consistency
- **Algoritmos distribuídos**: Consensus (Paxos, Raft), leader election
- **Sincronização**: Locks distribuídos, timestamps, vector clocks
- **Fault tolerance**: Replicação, failover, circuit breakers
- **Load balancing**: Algoritmos de distribuição de carga
- **Microservices**: Service discovery, API gateways, circuit breakers

## Objetivos e Funcionalidades Desejadas

- **Cobertura Abrangente de Conceitos:** Dado um **conceito** de qualquer área (ex: *árvores binárias*, *regressão linear*, *consensus algorithms*), o agente deve propor **várias tarefas** práticas relacionadas.
- **Aprendizado Orientado a Testes:** Cada tarefa incluirá um conjunto de **testes automatizados** que validam a solução, incentivando TDD.
- **Soluções Parciais para Implementação:** O agente fornecerá um *esqueleto* de solução com `raise NotImplementedError()` para partes a serem implementadas.
- **Independência e Paralelismo:** As tarefas geradas devem ser **autocontidas**, permitindo estudo paralelo.
- **Execução Rápida de Testes:** Comando único `pytest` para executar todos os testes.
- **Evolução Contínua com Qualidade:** Manter todos os testes passando conforme o repositório cresce.

## Estrutura do Repositório

```
├── algorithms/           # Algoritmos e estruturas de dados
│   ├── linked_lists/
│   ├── binary_trees/
│   ├── graphs/
│   ├── sorting/
│   ├── dynamic_programming/
│   └── parallel_algorithms/
├── machine_learning/     # Machine Learning
│   ├── supervised_learning/
│   ├── unsupervised_learning/
│   ├── optimization/
│   ├── feature_engineering/
│   └── evaluation/
├── distributed_systems/  # Sistemas Distribuídos
│   ├── consensus/
│   ├── communication/
│   ├── consistency/
│   ├── fault_tolerance/
│   └── load_balancing/
├── notes/               # Notas teóricas organizadas por área
│   ├── algorithms/
│   ├── machine_learning/
│   └── distributed_systems/
└── tools/               # Ferramentas auxiliares
    ├── data_generators/
    ├── visualization/
    └── benchmarking/
```

## Papel e Funcionamento do Agente

O **Agente Codex** será responsável por automatizar a geração dos desafios conforme as diretrizes acima. Ele será orientado por um arquivo de instruções (`AGENTS.md`) que descreve passo a passo o que deve ser feito quando um novo conceito ou tema é fornecido.

### Comportamento Esperado do Agente:

1. **Analisar o Conceito de Entrada:** A entrada pode ser um conceito específico ou texto descritivo contendo múltiplos conceitos.
2. **Proposição de Múltiplas Tarefas:** Para cada conceito, gerar múltiplas tarefas práticas relacionadas.
3. **Geração da Solução Interna e Casos de Teste:** Criar testes robustos usando PyTest.
4. **Criação de Arquivos de Código:** Para cada desafio, criar arquivo de implementação (stub) e arquivo de testes.
5. **Estrutura de Diretórios:** Organizar arquivos logicamente por área de conhecimento.
6. **Revisão e Ajustes:** Verificar consistência, ausência de dependências externas, legibilidade e isolamento.
7. **Registro das Tarefas:** Atualizar índices com desafios disponíveis.

## Convenções de Nomeação e Estilo

- **Nomes de Pastas (Áreas):** Usar nomes descritivos em inglês: `algorithms`, `machine_learning`, `distributed_systems`
- **Nomes de Arquivos de Código:** Seguir snake_case e indicar a funcionalidade principal
- **Nomes de Arquivos de Teste:** Sempre começar com `test_`
- **Nomes de Funções e Classes:** `snake_case` para funções, `CamelCase` para classes
- **Documentação:** Incluir docstrings e comentários explicativos
- **Formatação:** Seguir PEP 8
- **Codificação:** UTF-8

## Execução dos Testes Automatizados

- **Comando Único:** `pytest` na raiz do projeto executa todos os testes
- **Testes Isolados:** `pytest <area>/<conceito>/test_<nome>.py`
- **Feedback Rápido:** Testes eficientes para execução rápida
- **Manter Todos os Testes Verdes:** Executar antes de commits

## Exemplo de Uso do Agente

**Entrada do agente:** `"Regressão Linear"`

**Saída esperada:**

1. **Identificação de desafios:**
   - *Desafio 1:* **Implementação do Gradiente Descendente** – Implementar função `gradient_descent(X, y, learning_rate, iterations)`
   - *Desafio 2:* **Cálculo de Métricas** – Implementar `calculate_metrics(y_true, y_pred)` para MSE, MAE, R²
   - *Desafio 3:* **Validação Cruzada** – Implementar `cross_validation(X, y, k_folds)`

2. **Geração dos arquivos:**
   ```
   machine_learning/
   └── supervised_learning/
       ├── __init__.py
       ├── gradient_descent.py
       ├── test_gradient_descent.py
       ├── metrics.py
       ├── test_metrics.py
       ├── cross_validation.py
       └── test_cross_validation.py
   ```

## Considerações Específicas por Área

### Machine Learning
- **Dependências:** Usar apenas NumPy para operações matemáticas básicas
- **Dados:** Incluir geradores de dados sintéticos para testes
- **Métricas:** Implementar métricas de avaliação comuns
- **Visualização:** Opcional, usando matplotlib para plots

### Sistemas Distribuídos
- **Simulação:** Usar threading/multiprocessing para simular distribuição
- **Networking:** Implementar comunicação via sockets básicos
- **Fault Injection:** Simular falhas para testar resiliência
- **Métricas:** Latência, throughput, disponibilidade

## Evolução do Repositório

- **Cobertura de Performance:** Testes que insinuam questões de performance
- **Modularidade:** Novos conceitos podem ser adicionados incrementalmente
- **Extensibilidade:** Estrutura pode inspirar práticas similares em outras linguagens
- **Documentação:** Manter README atualizado com todas as áreas e desafios

## Tarefas Disponíveis

### Algoritmos e Estruturas de Dados

#### Linked Lists
- `reverse_linked_list.py` - reverter uma lista ligada simples.
- `detect_cycle.py` - verificar presença de ciclos em uma lista ligada.
- `merge_sorted_lists.py` - mesclar duas listas ligadas ordenadas.

#### Árvores Binárias
- `balance_bst.py` - balancear uma BST desbalanceada.
- `nivel_ordem.py` - percorrer a árvore em ordem de nível.
- `is_valid_bst.py` - verificar se uma árvore é uma BST válida.
- `delete_bst_node.py` - remover um nó de uma BST.
- `tree_min_max.py` - obter o menor e o maior valor de uma árvore.
- `tree_height.py` - calcular a altura de uma árvore binária.
- `count_nodes.py` - contar a quantidade de nós da árvore.
- `search_bst.py` - buscar um valor em uma BST.
- `lowest_common_ancestor.py` - encontrar o menor ancestral comum de dois nós.
- `in_ordem.py` - percorrer a árvore em ordem.
- `pre_ordem.py` - percorrer a árvore em pré-ordem.
- `pos_ordem.py` - percorrer a árvore em pós-ordem.

#### Tree Rotations
- `rotate_left.py` - realizar rotação à esquerda de um nó.
- `rotate_right.py` - realizar rotação à direita de um nó.

#### Árvores Rubro-Negras
- `insert_red_black.py` - inserir valor mantendo as propriedades Rubro-Negras.
- `is_valid_red_black.py` - validar se a árvore segue as regras Rubro-Negras.

#### AVL Trees
- `insert_avl.py` - inserir valores mantendo o balanceamento AVL.
- `is_avl_tree.py` - verificar se uma árvore atende às propriedades AVL.

#### Queues
- `simple_queue.py` - fila básica com operações de enfileirar e desenfileirar.
- `queue_two_stacks.py` - fila implementada com duas pilhas.
- `circular_queue.py` - fila circular de tamanho fixo.

#### Graphs
- `bfs_shortest_path.py` - encontrar o caminho mais curto em um grafo nao ponderado usando BFS.
- `topological_sort_dfs.py` - ordenação topológica usando busca em profundidade.
- `bfs_graph.py` - busca em largura a partir de um vértice inicial.
- `grafo_adj_list.py` - grafo usando lista de adjacência.
- `busca_largura.py` - percurso em largura (BFS) em grafos.
- `busca_profundidade.py` - percurso em profundidade (DFS) em grafos.

#### Stacks
- `validate_parentheses.py` - verificar se uma sequência de parênteses está balanceada.
- `min_stack.py` - pilha que retorna o valor mínimo em O(1).
- `min_max_stack.py` - pilha que retorna os valores mínimo e máximo em O(1).
- `evaluate_postfix.py` - avaliar expressões em notação pós-fixa.
- `equal_stacks.py` - equalizar três pilhas removendo do topo.
- `pair_stack.py` - pilha que armazena pares de inteiros.

#### Huffman
- `huffman_decoding.py` - decodificar mensagem a partir de códigos de Huffman.

#### Busca em Profundidade
- `dfs_recursivo.py` - busca em profundidade implementada de forma recursiva.
- `dfs_iterativo.py` - busca em profundidade utilizando pilha.
- `detect_cycle_dfs.py` - detecção de ciclos em grafo usando DFS.

#### Radix Trees
- `radix_insert.py` - inserir palavra em uma Radix Tree.
- `radix_search.py` - buscar palavra em uma Radix Tree.
- `radix_delete.py` - remover palavra de uma Radix Tree.

#### General Tree Conversion
- `convert_to_binary.py` - converter uma árvore geral para binária.
- `binary_to_general.py` - converter uma árvore binária na representação filho à esquerda/irmão à direita para uma árvore geral.

#### Prefix Sums
- `cumulative_sum.py` - gerar lista de somas acumuladas.
- `range_sum_query.py` - calcular somas de intervalos usando prefix sums.
- `prefix_set_intersection.py` - calcular intersecção de conjuntos prefixados.

#### Priority Queues
- `min_priority_queue.py` - fila de prioridade mínima usando heap.
- `merge_k_sorted_lists.py` - mesclar múltiplas listas ordenadas.
- `kth_smallest.py` - encontrar o k-ésimo menor elemento.

#### Heaps
- `binary_heap.py` - implementa uma min-heap simples.
- `heap_sort.py` - ordena uma lista usando heap sort.
- `k_largest_elements.py` - retorna os k maiores elementos de uma lista.

#### Sorting Algorithms
- `merge_sort.py` - ordenar uma lista usando merge sort.
- `selection_sort.py` - ordenar uma lista usando selection sort.
- `set_operations.py` - operações de conjunto (união, interseção, diferença).
- `direct_access_array_sort.py` - ordenação usando array de acesso direto O(n + u).
- `counting_sort.py` - ordenação por contagem estável O(n + u).
- `radix_sort.py` - ordenação por dígitos O(n × d) com counting sort auxiliar.
- `tuple_sort.py` - ordenação por múltiplas chaves com priorização O(k × (n + u)).

#### Dynamic Programming
- `rod_cutting.py` - problema do corte de barras para maximizar lucro.
- `knapsack.py` - problema da mochila (0/1, fracionária e com itens).
- `longest_common_subsequence.py` - subsequência comum mais longa entre strings.
- `optimal_binary_search_tree.py` - árvore binária de busca ótima.

#### Parallel Algorithms
- `fibonacci_parallel.py` - cálculo de Fibonacci usando modelo fork-join.
- `matrix_vector_multiply.py` - multiplicação matriz-vetor paralela.
- `task_parallelism.py` - padrões de paralelismo de tarefas (pipeline, produtor-consumidor, map-reduce).
- `async_synchronization.py` - primitivas de sincronização assíncrona (contador, pool, barreira, lock r/w).

#### Concurrent Objects
- `quiescent_counter.py` - contador quiescentemente consistente.
- `sequential_register.py` - register sequencialmente consistente.
- `linearizable_queue.py` - fila linearizável FIFO.
- `wait_free_counter.py` - contador wait-free.
- `lock_free_stack.py` - pilha lock-free LIFO.

### Machine Learning

#### Supervised Learning
- `knn_regression.py` - implementação do algoritmo k-Nearest Neighbors para regressão.

### Sistemas Distribuídos
[será preenchido conforme desafios forem criados]
