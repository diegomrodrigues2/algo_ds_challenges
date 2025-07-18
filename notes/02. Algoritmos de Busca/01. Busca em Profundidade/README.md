# 🔍 Busca em Profundidade (DFS) - Índice

## 📚 Visão Geral

Esta pasta contém **resumos didáticos** sobre Depth-First Search (DFS), organizados por tópicos específicos.


## 📖 Estrutura dos Resumos

### 🎯 [01. Depth-First Search.md](./01.%20Depth-First%20Search.md)
**Conceitos Fundamentais**
- O que é DFS
- Estratégia de exploração
- Complexidade e propriedades
- Vantagens e desvantagens
- Aplicações práticas

### 🔄 [02. Implementações.md](./02.%20Implementações.md)
**Recursiva e Iterativa**
- DFS recursivo (backtracking natural)
- DFS iterativo com pilha
- Comparação de abordagens
- Casos de uso específicos

### 🔍 [03. Detecção de Ciclos.md](./03.%20Detecção%20de%20Ciclos.md)
**Análise de Grafos**
- Detecção de ciclos em grafos direcionados
- Estados dos vértices (branco, cinza, preto)
- Aplicações em ordenação topológica
- Grafos acíclicos direcionados (DAGs)

### 🎨 [04. Aplicações Avançadas.md](./04.%20Aplicações%20Avançadas.md)
**Casos de Uso Específicos**
- Ordenação topológica
- Componentes fortemente conectados
- Pontes e pontos de articulação
- Coloração de grafos


## 🎯 Problemas Relacionados

Baseado na análise dos arquivos em `algorithms/busca_em_profundidade/`:

### 🔄 **Implementações Básicas**
- `dfs_recursivo.py` → [02. Implementações](./02.%20Implementações.md)
- `dfs_iterativo.py` → [02. Implementações](./02.%20Implementações.md)

### 🔍 **Análise de Grafos**
- `detect_cycle_dfs.py` → [03. Detecção de Ciclos](./03.%20Detecção%20de%20Ciclos.md)


## 🎯 Conceitos-Chave

### 🌟 **Estratégia Fundamental**
```
DFS: "Vá o mais fundo possível antes de voltar"
- Explora um caminho até o final
- Backtrack quando não há mais opções
- Usa pilha (recursão ou explícita)
```

### ⚡ **Complexidade**
| Aspecto | Complexidade | Observação |
|---------|--------------|------------|
| Tempo | O(V + E) | Visita cada vértice e aresta uma vez |
| Espaço | O(V) | Altura da pilha de recursão |
| Memória | O(V) | Para grafo completo pode ser O(V²) |

### 🔄 **Estados dos Vértices**
- **🟢 Branco**: Não visitado
- **🟡 Cinza**: Em processamento (na pilha)
- **⚫ Preto**: Processado completamente

### 🎯 **Aplicações Principais**
- **🔍 Exploração**: Labirintos, jogos
- **📊 Topologia**: Ordenação de dependências
- **🔗 Conectividade**: Componentes conectados
- **🎨 Coloração**: Grafos bipartidos


## 💡 Dicas de Estudo

### 🎓 **Ordem Recomendada**
1. **Conceitos básicos** → [01. Depth-First Search](./01.%20Depth-First%20Search.md)
2. **Como implementar** → [02. Implementações](./02.%20Implementações.md)
3. **Detecção de ciclos** → [03. Detecção de Ciclos](./03.%20Detecção%20de%20Ciclos.md)
4. **Aplicações práticas** → [04. Aplicações Avançadas](./04.%20Aplicações%20Avançadas.md)

### 🔍 **Para Prática**
1. **Desenhe o grafo** e trace a execução
2. **Compare com BFS** - quando usar cada um
3. **Implemente ambas** versões (recursiva e iterativa)
4. **Teste com grafos** cíclicos e acíclicos


## 🎯 Próximos Passos

### 📚 **Tópicos Relacionados**
- **Breadth-First Search**: Exploração em largura
- **Backtracking**: DFS com restrições
- **Ordenação Topológica**: Dependências em DAGs
- **Componentes Fortemente Conectados**: Algoritmo de Tarjan

### 🔧 **Implementações Práticas**
- **Sistemas de build**: Ordenação de dependências
- **Jogos**: IA para exploração de estados
- **Compiladores**: Análise de dependências
- **Redes sociais**: Análise de conectividade


*💡 **Dica**: DFS é fundamental para algoritmos de grafos. Sua simplicidade conceitual esconde um poder enorme para resolver problemas complexos de conectividade e dependência!* 