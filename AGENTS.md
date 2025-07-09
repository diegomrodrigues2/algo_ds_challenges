## 🎯 Objetivo

Este repositório visa auxiliar no estudo aprofundado de **estruturas de dados e algoritmos** em Python, especialmente para preparação de entrevistas técnicas. Utilizando um agente Codex, serão geradas tarefas práticas que incluem:

- **Casos de teste automatizados** com `pytest`.
- **Implementações parciais** com trechos a serem completados pelo usuário.
- **Execução local** sem dependências externas, utilizando apenas o Python padrão.

Cada tarefa é **autocontida** e independente, permitindo estudo paralelo e progressivo.

## 🧠 Funcionamento do Agente

### 1. Entrada

O agente pode receber:

- Um **conceito específico**, como `"Árvores Binárias"`.
- Um **texto descritivo** contendo múltiplos conceitos e ideias.

### 2. Processamento

Para cada entrada, o agente deve:

- **Identificar tópicos** relevantes.
- **Gerar múltiplas tarefas** práticas relacionadas.
- **Criar arquivos** para cada tarefa, incluindo:
  - Um arquivo de implementação com partes faltantes.
  - Um arquivo de testes automatizados com `pytest`.

### 3. Saída

A estrutura de saída para cada tarefa deve ser:

```
algorithms/
└── <conceito>/
    ├── __init__.py
    ├── <nome_da_tarefa>.py
    └── test_<nome_da_tarefa>.py
```

Exemplo:

```
algorithms/
└── arvores_binarias/
    ├── __init__.py
    ├── balance_bst.py
    └── test_balance_bst.py
```

## 🧩 Detalhes da Tarefa

### Arquivo de Implementação (`<nome_da_tarefa>.py`)

- Contém a assinatura da função ou classe a ser implementada.

- Inclui estruturas auxiliares necessárias (ex: definição de `TreeNode`).

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

Para rodar testes de uma tarefa específica:

```bash
pytest algorithms/<conceito>/test_<nome_da_tarefa>.py
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
  - Cada tarefa deve ser autocontida, sem dependências externas.
  - Utilizar apenas bibliotecas padrão do Python.

## 📚 Exemplo de Uso

**Entrada do agente**: `"Árvores Binárias"`

**Tarefas geradas**:

1. **Balanceamento de BST**:
   - `balance_bst.py`: Implementar função `balance_bst(root)`.
   - `test_balance_bst.py`: Testes para verificar o balanceamento correto.
2. **Percurso em Largura (BFS)**:
   - `percurso_bfs.py`: Implementar função `percurso_bfs(root)`.
   - `test_percurso_bfs.py`: Testes para validar o percurso em largura.
3. **Verificação de BST Válida**:
   - `is_valid_bst.py`: Implementar função `is_valid_bst(root)`.
   - `test_is_valid_bst.py`: Testes para verificar se a árvore é uma BST válida.

Cada tarefa inclui:

- Estrutura auxiliar `TreeNode` definida no arquivo de implementação.
- Testes abrangentes cobrindo diferentes cenários.

## 🚀 Evolução do Repositório

- Novas tarefas podem ser adicionadas incrementando o repositório.
- Todas as tarefas devem manter os testes passando.
- O agente pode atualizar um `README.md` com a lista de tarefas disponíveis.
