# Algoritmos de Grafos

Este módulo contém implementações de algoritmos fundamentais para grafos, incluindo estruturas de dados, algoritmos de busca e algoritmos avançados.

## Estruturas de Dados

### Grafo (Lista de Adjacência)
- **Arquivo**: `grafo_adj_list.py`
- **Classe**: `Grafo`
- **Descrição**: Implementação de grafo não direcionado usando lista de adjacência
- **Métodos**:
  - `adiciona_aresta(u, v)`: Adiciona aresta entre vértices u e v
  - `vizinhos(u)`: Retorna lista de vértices adjacentes a u

## Algoritmos de Busca

### Busca em Largura (BFS)
- **Arquivo**: `busca_largura.py`
- **Função**: `busca_largura(adj, inicio)`
- **Descrição**: Implementação de BFS usando dicionário de adjacência
- **Complexidade**: O(V + E)

### Busca em Profundidade (DFS)
- **Arquivo**: `busca_profundidade.py`
- **Função**: `busca_profundidade(adj, inicio)`
- **Descrição**: Implementação de DFS usando dicionário de adjacência
- **Complexidade**: O(V + E)

### BFS Genérico
- **Arquivo**: `bfs_graph.py`
- **Função**: `bfs_graph(graph, start)`
- **Descrição**: Versão genérica de BFS para grafos representados como dicionário
- **Complexidade**: O(V + E)

## Algoritmos Avançados

### Caminho Mais Curto (BFS)
- **Arquivo**: `bfs_shortest_path.py`
- **Função**: `bfs_shortest_path(graph, start, goal)`
- **Descrição**: Encontra o caminho mais curto entre dois vértices em grafo não ponderado
- **Complexidade**: O(V + E)

### Ordenação Topológica (DFS)
- **Arquivo**: `topological_sort_dfs.py`
- **Função**: `topological_sort(graph)`
- **Descrição**: Realiza ordenação topológica em grafo acíclico direcionado
- **Complexidade**: O(V + E)

## Como Executar os Testes

Para executar todos os testes do módulo:
```bash
pytest algorithms/graphs/
```

Para executar testes específicos:
```bash
pytest algorithms/graphs/test_grafo_adj_list.py
pytest algorithms/graphs/test_busca_largura.py
pytest algorithms/graphs/test_busca_profundidade.py
pytest algorithms/graphs/test_bfs_graph.py
pytest algorithms/graphs/test_bfs_shortest_path.py
pytest algorithms/graphs/test_topological_sort_dfs.py
```

## Estrutura de Arquivos

```
graphs/
├── __init__.py
├── README.md
├── grafo_adj_list.py
├── busca_largura.py
├── busca_profundidade.py
├── bfs_graph.py
├── bfs_shortest_path.py
├── topological_sort_dfs.py
├── test_grafo_adj_list.py
├── test_busca_largura.py
├── test_busca_profundidade.py
├── test_bfs_graph.py
├── test_bfs_shortest_path.py
└── test_topological_sort_dfs.py
``` 