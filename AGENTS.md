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
