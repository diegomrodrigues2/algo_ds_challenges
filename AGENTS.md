## 🎯 Objetivo

Este repositório visa auxiliar no estudo aprofundado de **ciência da computação** em Python, especialmente para preparação de entrevistas técnicas e desenvolvimento de carreira. Utilizando um agente Codex, serão geradas tarefas práticas que incluem:

- **Casos de teste automatizados** com `pytest`.
- **Implementações parciais** com trechos a serem completados pelo usuário.
- **Execução local** com dependências mínimas (Python padrão + NumPy para ML).
- **Cobertura de múltiplas áreas**: Algoritmos, Machine Learning e Sistemas Distribuídos.

Cada tarefa é **autocontida** e independente, permitindo estudo paralelo e progressivo.

## 🧠 Funcionamento do Agente

### 1. Entrada

O agente pode receber:

- Um **conceito específico**, como `"Árvores Binárias"`, `"Regressão Linear"` ou `"Consensus Algorithms"`.
- Um **texto descritivo** contendo múltiplos conceitos e ideias.
- Uma **área de conhecimento** específica para explorar.

### 2. Processamento

Para cada entrada, o agente deve:

- **Identificar a área de conhecimento** (algorithms, machine_learning, distributed_systems).
- **Identificar tópicos** relevantes dentro da área.
- **Gerar múltiplas tarefas** práticas relacionadas.
- **Criar arquivos** para cada tarefa, incluindo:
  - Um arquivo de implementação com partes faltantes.
  - Um arquivo de testes automatizados com `pytest`.

### 3. Saída

A estrutura de saída para cada tarefa deve ser:

```
<area>/
└── <conceito>/
    ├── __init__.py
    ├── <nome_da_tarefa>.py
    └── test_<nome_da_tarefa>.py
```

Exemplos:

```
algorithms/
└── binary_trees/
    ├── __init__.py
    ├── balance_bst.py
    └── test_balance_bst.py

machine_learning/
└── supervised_learning/
    ├── __init__.py
    ├── gradient_descent.py
    └── test_gradient_descent.py

distributed_systems/
└── consensus/
    ├── __init__.py
    ├── paxos_algorithm.py
    └── test_paxos_algorithm.py
```

## 🧩 Detalhes da Tarefa

### Arquivo de Implementação (`<nome_da_tarefa>.py`)

- Contém a assinatura da função ou classe a ser implementada.
- Inclui estruturas auxiliares necessárias.
- Partes a serem implementadas devem estar marcadas com:

  ```python
  raise NotImplementedError("Implementar esta função")
  ```

### Arquivo de Testes (`test_<nome_da_tarefa>.py`)

- Utiliza o framework `pytest`.
- Inclui múltiplos testes com `assert` para validar a solução.
- Cobre casos típicos e extremos (*edge cases*).
- Importa o código a ser testado de forma relativa:

  ```python
  from .<nome_da_tarefa> import <função_ou_classe>
  ```

## 🧪 Execução dos Testes

Para rodar todos os testes:

```bash
pytest
```

Para rodar testes de uma área específica:

```bash
pytest algorithms/
pytest machine_learning/
pytest distributed_systems/
```

Para rodar testes de uma tarefa específica:

```bash
pytest <area>/<conceito>/test_<nome_da_tarefa>.py
```

## 📝 Convenções

- **Nomenclatura**:
  - Pastas e arquivos: `snake_case` em letras minúsculas.
  - Funções e variáveis: `snake_case`.
  - Classes: `CamelCase`.
- **Estilo de Código**:
  - Seguir as diretrizes do [PEP 8](https://peps.python.org/pep-0008/).
  - Incluir docstrings nas funções e classes.
- **Independência**:
  - Cada tarefa deve ser autocontida.
  - Para ML: usar apenas NumPy além do Python padrão.
  - Para sistemas distribuídos: usar apenas threading/multiprocessing/sockets.

## 📚 Exemplos de Uso por Área

### Algoritmos e Estruturas de Dados

**Entrada do agente**: `"Árvores Binárias"`

**Tarefas geradas**:

1. **Balanceamento de BST**:
   - `balance_bst.py`: Implementar função `balance_bst(root)`.
   - `test_balance_bst.py`: Testes para verificar o balanceamento correto.

### Machine Learning

**Entrada do agente**: `"Regressão Linear"`

**Tarefas geradas**:

1. **Gradiente Descendente**:
   - `gradient_descent.py`: Implementar função `gradient_descent(X, y, learning_rate, iterations)`.
   - `test_gradient_descent.py`: Testes para verificar convergência e precisão.

2. **Métricas de Avaliação**:
   - `metrics.py`: Implementar funções `mse()`, `mae()`, `r2_score()`.
   - `test_metrics.py`: Testes para validar cálculos de métricas.

### Sistemas Distribuídos

**Entrada do agente**: `"Consensus Algorithms"`

**Tarefas geradas**:

1. **Algoritmo de Paxos**:
   - `paxos_algorithm.py`: Implementar classe `PaxosNode` com métodos `propose()` e `accept()`.
   - `test_paxos_algorithm.py`: Testes para verificar consenso em cenários diversos.

## 🔧 Considerações Específicas por Área

### Machine Learning

- **Dependências**: Usar apenas NumPy para operações matemáticas
- **Dados**: Incluir geradores de dados sintéticos nos testes
- **Métricas**: Implementar métricas de avaliação comuns (MSE, MAE, R², accuracy, precision, recall)
- **Validação**: Cross-validation, train/test split
- **Otimização**: Gradiente descendente, SGD, Adam

### Sistemas Distribuídos

- **Simulação**: Usar threading/multiprocessing para simular nós distribuídos
- **Comunicação**: Implementar comunicação via sockets ou queues
- **Fault Tolerance**: Simular falhas de nós e rede
- **Consistência**: Implementar diferentes níveis de consistência
- **Métricas**: Latência, throughput, disponibilidade

## 🚀 Evolução do Repositório

- Novas tarefas podem ser adicionadas incrementando o repositório.
- Todas as tarefas devem manter os testes passando.
- O agente pode atualizar um `README.md` com a lista de tarefas disponíveis.
- Manter documentação atualizada com todas as áreas cobertas.

## 📖 Estrutura de Notas

O agente também pode gerar notas teóricas organizadas em:

```
notes/
├── algorithms/
│   ├── data_structures/
│   ├── sorting_algorithms/
│   └── graph_algorithms/
├── machine_learning/
│   ├── supervised_learning/
│   ├── unsupervised_learning/
│   └── optimization/
└── distributed_systems/
    ├── consensus/
    ├── consistency/
    └── fault_tolerance/
```

Cada área terá sua própria estrutura de notas teóricas complementando os desafios práticos.

## 🧠 Implementações Específicas - Programação Dinâmica

### Soma de Subconjuntos com Memoização

#### 🎯 Visão Geral
Implementação do problema da Soma de Subconjuntos usando memoização, demonstrando a transição fundamental de backtracking exponencial para programação dinâmica eficiente.

#### 🔗 Vínculos Conceituais
- **Erickson, "Algorithms"**: Capítulo 3, Seção 3.1, "Memo(r)ization"
- **Teoria**: [Erickson sobre Programação Dinâmica](https://jeffe.cs.illinois.edu/teaching/algorithms/book/03-dynprog.pdf)
- **Implementação**: [GeeksforGeeks - Subset Sum DP](https://www.geeksforgeeks.org/dsa/subset-sum-problem-dp-25/)
- **Comparação**: [Memoização vs Tabulação](https://www.geeksforgeeks.org/dsa/tabulation-vs-memoization/)

#### 🧠 Análise de Especialista
A transição do backtracking O(2^n) para programação dinâmica O(n·T) é a quintessência da PD:
- **Estado (i, t)**: "Existe subconjunto de X[i..n] que soma t?"
- **Memoização**: Cache para evitar recálculos exponenciais
- **Recursão Inteligente**: PD como otimização de algoritmos recursivos

#### ⚙️ Estrutura da Implementação
```python
def subset_sum_memoization(nums: List[int], target: int) -> bool:
    """
    Resolve Soma de Subconjuntos usando memoização.
    
    Args:
        nums: Lista de números inteiros
        target: Valor alvo a ser alcançado
        
    Returns:
        True se existe subconjunto que soma target, False caso contrário
    """
    # Cache para memoização
    memo = {}
    
    def dp(i: int, t: int) -> bool:
        # Verifica se resultado já está no cache
        if (i, t) in memo:
            return memo[(i, t)]
        
        # Casos base
        if t == 0:
            return True
        if i >= len(nums) or t < 0:
            return False
        
        # Recursão com memoização
        result = dp(i + 1, t - nums[i]) or dp(i + 1, t)
        memo[(i, t)] = result
        return result
    
    return dp(0, target)
```

#### 🚀 Funcionalidades Principais
1. **Memoização Top-Down**: Cache para evitar recálculos
2. **Transição de Backtracking**: Otimização de solução recursiva
3. **Complexidade Pseudo-Polinomial**: O(n·T) onde T é o valor alvo
4. **Identificação de Estado**: Par (i, t) representa subproblema único

#### 📊 Complexidade e Limitações
- **Tempo**: O(n·T) pseudo-polinomial
- **Espaço**: O(n·T) para cache de memoização
- **Vantagem**: Reduz complexidade exponencial para pseudo-polinomial
- **Limitação**: Ainda pode ser lento para valores de target muito grandes

#### 🎯 Aplicações Práticas
- **Problemas de Otimização**: Alocação de recursos, balanceamento de carga
- **Teoria da Computação**: Exemplo clássico de NP-completeness
- **Educação em PD**: Demonstra transição de força bruta para eficiência
- **Base para Outros Problemas**: Knapsack, Partition, Coin Change

#### ⚡ Otimizações Implementadas
1. **Cache de Memoização**: Evita recálculos de subproblemas
2. **Identificação de Estado**: Par (i, t) como chave única
3. **Pruning Inteligente**: Para quando t < 0 ou t == 0
4. **Transição Suave**: Mantém estrutura recursiva original

#### 🧪 Testes e Validação
- **Testes Unitários**: Casos básicos, casos extremos, casos de borda
- **Testes de Performance**: Comparação com backtracking puro
- **Análise de Complexidade**: Validação da redução de complexidade
- **Casos de Stress**: Testes com valores grandes de target
