### Instruções para o Agente

## 🎯 Objetivo
Criar resumos didáticos e visuais de algoritmos e estrutura de dados que sejam **fáceis de entender** e **visualmente atraentes**, priorizando clareza conceitual mas mantendo o alto nível técnico e teórico de forma coesa e **extremamente concisa**

## 📏 Limitações de Tamanho
- **📄 Tamanho máximo**: 1-3 páginas por documento
- **🎯 Priorize**: Conceitos essenciais sobre detalhes extensos
- **✂️ Elimine**: Redundâncias e exemplos excessivos
- **🔥 Foque**: No que é crítico para entendimento

## 📝 Formato dos Documentos

### 1. Estrutura Visual Compacta
- **Use emojis** para representar conceitos, atores e componentes
- **Títulos concisos** com emojis descritivos
- **Definições em 1-2 frases** mantendo detalhes essenciais
- **Tabelas compactas** para comparações rápidas
- **Diagramas simples**

### 2. Diretrizes de Escrita Concisa
- ✅ **Máximo 3 parágrafos** por seção
- ✅ **Frases curtas** e diretas
- ✅ **Bullet points** em vez de texto corrido
- ✅ **Elimine preâmbulos** - vá direto ao ponto
- ✅ **Use analogias curtas** (1 frase máximo)

### 3. Elementos Visuais Obrigatórios

#### 📊 Tabelas Compactas
| Aspecto | ✅ Vantagem | ❌ Desvantagem |
|---------|-------------|----------------|
| Performance | 🚀 Rápido | 💾 Usa memória |
| Consistência | 🛡️ Garantida | ⏰ Mais lento |

#### 🎨 Diagramas Mermaid
- **Use diagramas simples** que facilitem a compreensão
- **Evite**: `graph` muito extensos, tente mantê-los concisos
- **Nunca use**: Mapas mentais
- **Represente atores e componentes com emojis**:
  - 👤 Usuário/Cliente
  - 🔧 Sistema/Processo
  - 📦 Dados/Objetos
  - ⚡ Operações/Ações
  - 🔄 Estados/Transições


## 📁 Organização de Arquivos

```
01. Nome do Super-tópico/
    01. Nome do Tópico/
        01. Nome do Sub-tópico.md
        02. Nome do Sub-tópico.md
        03. Nome do Sub-tópico.md
        ...
    02. Nome do Tópico/
        01. Nome do Sub-tópico.md
        02. Nome do Sub-tópico.md
        03. Nome do Sub-tópico.md
        ...
02. Outro super-tópico/
    01. Nome do Tópico/
        ...
```

## 🔧 Uso da Notação

- **Consulte sempre** o NOTATION.md para símbolos padronizados
- **Use notação apenas quando necessário** para clareza
- **Prefira descrições textuais** com emojis a fórmulas complexas
- **Atualize NOTATION.md** quando introduzir novos conceitos

## 📐 Regras de Concisão
- **🚫 Máximo 1000 palavras** por documento
- **⏰ Leitura em 3-5 minutos**
- **🎯 Uma ideia central** por seção

## 📝 Fórmulas Matemáticas
- **Use sintaxe LaTeX** para todas as fórmulas matemáticas
- **Exemplo**: `$f(x) = \frac{1}{k} \sum_{i \in N_k(x_0)} y_i$`
- **Prefira**: Fórmulas inline com `$...$` para expressões simples
- **Use**: `$$...$$` para fórmulas em bloco quando necessário

## 🎮 Implementações Específicas

### Jogo da Velha Generalizado com Minimax

#### 🎯 Visão Geral
Implementação do algoritmo Minimax para Jogo da Velha generalizado (n×n), demonstrando aplicação formal do backtracking em árvores de jogo.

#### 🔗 Vínculos Conceituais
- **Erickson, "Algorithms"**: Capítulo 2, Seção 2.2, "Game Trees"
- **GitHub Reference**: [t-ROY-coder/Tic-Tac-Toe-Game](https://github.com/t-ROY-coder/Tic-Tac-Toe-Game)
- **Teoria**: [Erickson sobre Árvores de Jogo](https://jeffe.cs.illinois.edu/teaching/algorithms/book/02-backtracking.pdf)

#### 🧠 Análise de Especialista
O algoritmo Minimax é backtracking aplicado a jogos de dois jogadores com informação perfeita:
- **Maximizador**: Escolhe movimento que leva ao melhor resultado
- **Minimizador**: Escolhe movimento que leva ao pior resultado para o maximizador
- **Backtracking**: Retrocede valores das folhas para determinar movimento ótimo

#### ⚙️ Estrutura da Implementação
```python
class TicTacToeBoard:
    def __init__(self, size: int = 3):  # Tabuleiro n×n
    def make_move(self, row: int, col: int) -> bool:  # Movimento
    def get_available_moves(self) -> List[Tuple[int, int]]:  # Movimentos disponíveis
    def is_terminal_state(self) -> bool:  # Estado terminal
    def get_utility(self) -> int:  # Valor de utilidade

def minimax(board, depth, alpha, beta, maximizing) -> Tuple[int, Optional[Tuple[int, int]]]:
    # Algoritmo Minimax com poda Alpha-Beta
```

#### 🚀 Funcionalidades Principais
1. **Algoritmo Minimax com Poda Alpha-Beta**: Exploração completa para tabuleiros pequenos
2. **Jogo da Velha Generalizado**: Suporta tabuleiros n×n
3. **Análise de Complexidade**: `analyze_minimax_complexity(size)`
4. **Simulação de Jogos Ótimos**: `play_optimal_game(size, max_depth)`

#### 📊 Complexidade e Limitações
- **Tempo**: O(b^d) onde b é fator de ramificação, d é profundidade
- **Espaço**: O(d) para profundidade da pilha de recursão
- **Limitações**: Praticamente viável até tabuleiros 4×4

#### 🎯 Aplicações Práticas
- **Jogos de Tabuleiro**: Xadrez, Damas, Go
- **IA Competitiva**: Algoritmo fundamental para IAs fortes
- **Teoria dos Jogos**: Análise de estratégias ótimas
- **Educação em IA**: Exemplo clássico de busca em árvores

#### ⚡ Otimizações Implementadas
1. **Poda Alpha-Beta**: Reduz nós explorados em até 50%
2. **Busca em Profundidade Limitada**: Controle de tempo de execução
3. **Memoização**: Cache de estados para evitar recálculos

#### 🧪 Testes e Validação
- **Testes Unitários**: Funcionalidade básica, algoritmo Minimax, casos extremos
- **Testes de Performance**: Benchmark para diferentes tamanhos de tabuleiro
- **Análise de Complexidade**: Validação das estimativas teóricas

### Segmentação de Texto com Memoização

#### 🎯 Visão Geral
Implementação do problema da Segmentação de Texto (Word Break) usando memoização, demonstrando a transição de backtracking exponencial O(2^n) para programação dinâmica O(n²).

#### 🔗 Vínculos Conceituais
- **Erickson, "Algorithms"**: Capítulo 3, Seção 3.3, "Interpunctio Verborum Redux"
- **GeeksforGeeks**: [Word Break Problem](https://www.geeksforgeeks.org/dsa/word-break-problem-dp-32/)
- **Tutorial Horizon**: [The Word Break Problem](https://tutorialhorizon.com/algorithms/the-word-break-problem/)

#### 🧠 Análise de Especialista
A transição do backtracking O(2^n) para programação dinâmica O(n²) é a quintessência da PD:
- **Estado (i)**: "O sufixo text[i..n] pode ser segmentado?"
- **Memoização**: Cache para evitar recálculos exponenciais
- **Subproblemas Sobrepostos**: Múltiplos caminhos para o mesmo estado

#### ⚙️ Estrutura da Implementação
```python
def text_segmentation_memoization(text: str, dictionary: Set[str]) -> Optional[List[str]]:
    """
    Resolve Segmentação de Texto usando memoização.
    
    Args:
        text: String sem espaços para segmentar
        dictionary: Conjunto de palavras válidas
        
    Returns:
        Lista de palavras se a segmentação for possível, None caso contrário
    """
    # Cache para memoização
    memo = {}
    
    def can_segment(start: int) -> Optional[List[str]]:
        # Verifica se resultado já está no cache
        if start in memo:
            return memo[start]
        
        # Casos base
        if start == len(text):
            return []
        
        # Tenta todos os prefixos possíveis
        for end in range(start + 1, len(text) + 1):
            prefix = text[start:end]
            if prefix in dictionary:
                remaining = can_segment(end)
                if remaining is not None:
                    result = [prefix] + remaining
                    memo[start] = result
                    return result
        
        # Nenhuma segmentação encontrada
        memo[start] = None
        return None
    
    return can_segment(0)
```

#### 🚀 Funcionalidades Principais
1. **Memoização Top-Down**: Cache para evitar recálculos
2. **Transição de Backtracking**: Otimização de solução recursiva
3. **Complexidade Quadrática**: O(n²) onde n é o tamanho da string
4. **Identificação de Estado**: Índice inicial do sufixo

#### 📊 Complexidade e Limitações
- **Tempo**: O(n²) quadrático
- **Espaço**: O(n) para cache de memoização
- **Vantagem**: Reduz complexidade exponencial para quadrática
- **Limitação**: Ainda pode ser lento para strings muito longas

#### 🎯 Aplicações Práticas
- **Processamento de Texto**: Segmentação de texto sem espaços
- **Compiladores**: Análise léxica e parsing
- **IA e NLP**: Processamento de linguagem natural
- **Sistemas de Busca**: Indexação e recuperação de texto

#### ⚡ Otimizações Implementadas
1. **Cache de Memoização**: Evita recálculos de subproblemas
2. **Identificação de Estado**: Índice inicial como chave única
3. **Pruning Inteligente**: Para quando chega ao final da string
4. **Transição Suave**: Mantém estrutura recursiva original

#### 🧪 Testes e Validação
- **Testes Unitários**: Casos básicos, casos extremos, casos de borda
- **Testes de Performance**: Comparação com backtracking puro
- **Análise de Complexidade**: Validação da redução de complexidade
- **Casos de Stress**: Testes com strings longas

### LIS com Memoização

#### 🎯 Visão Geral
Implementação do problema da Subsequência Crescente Mais Longa (LIS) usando memoização com a formulação LISbigger(i, j), demonstrando a transição de backtracking exponencial O(2^n) para programação dinâmica O(n²).

#### 🔗 Vínculos Conceituais
- **Erickson, "Algorithms"**: Capítulo 3, Seção 3.6, "First Recurrence: Is This Next?"
- **GeeksforGeeks**: [LIS with DP](https://www.geeksforgeeks.org/dsa/longest-increasing-subsequence-dp-3/)
- **Formulação LISbigger**: Estado bidimensional (current_index, previous_index)

#### 🧠 Análise de Especialista
A transição do backtracking O(2^n) para programação dinâmica O(n²) usando LISbigger(i, j):
- **Estado (i, j)**: "LIS começando em i com elemento anterior em j"
- **Memoização**: Cache 2D para evitar recálculos exponenciais
- **Formulação de Erickson**: Base teórica para recursão inteligente

#### ⚙️ Estrutura da Implementação
```python
def lis_memoization(arr: List[int]) -> int:
    """
    Resolve LIS usando memoização com formulação LISbigger(i, j).
    
    Args:
        arr: Lista de números inteiros
        
    Returns:
        Comprimento da subsequência crescente mais longa
    """
    # Cache para memoização
    memo = {}
    
    def lis_bigger(i: int, prev_idx: int) -> int:
        # Verifica se resultado já está no cache
        if (i, prev_idx) in memo:
            return memo[(i, prev_idx)]
        
        # Caso base
        if i == len(arr):
            return 0
        
        # Opção 1: Não incluir elemento atual
        result = lis_bigger(i + 1, prev_idx)
        
        # Opção 2: Incluir elemento atual (se possível)
        if prev_idx == -1 or arr[i] > arr[prev_idx]:
            result = max(result, 1 + lis_bigger(i + 1, i))
        
        memo[(i, prev_idx)] = result
        return result
    
    return lis_bigger(0, -1)
```

#### 🚀 Funcionalidades Principais
1. **Memoização Bidimensional**: Cache para estados (i, j)
2. **Formulação LISbigger**: Implementação direta da recorrência de Erickson
3. **Complexidade Quadrática**: O(n²) tempo e espaço
4. **Decisão Binária**: Para cada elemento, incluir ou não na subsequência

#### 📊 Complexidade e Limitações
- **Tempo**: O(n²) quadrático
- **Espaço**: O(n²) para cache de memoização
- **Vantagem**: Reduz complexidade exponencial para quadrática
- **Limitação**: Uso de memória proporcional a n²

#### 🎯 Aplicações Práticas
- **Análise de Sequências**: Encontrar tendências de crescimento
- **Mercado Financeiro**: Períodos de alta em preços de ações
- **Progresso Acadêmico**: Sequências de melhoria em notas
- **Otimização**: Sequências de melhoria contínua

#### ⚡ Otimizações Implementadas
1. **Cache Bidimensional**: Evita recálculos de pares (i, j)
2. **Decisão Eficiente**: Considera incluir/não incluir cada elemento
3. **Estado Compacto**: Par (índice_atual, índice_anterior)
4. **Base para O(n log n)**: Fundação para otimização com busca binária

#### 🧪 Testes e Validação
- **Testes Unitários**: Casos básicos, arrays ordenados/reversos, elementos duplicados
- **Testes de Performance**: Comparação com diferentes abordagens
- **Análise de Complexidade**: Validação da redução de O(2^n) para O(n²)
- **Casos Reais**: Aplicações em análise de dados sequenciais

### Soma de Subconjuntos com Memoização

#### 🎯 Visão Geral
Implementação do problema da Soma de Subconjuntos usando memoização, demonstrando a transição de backtracking exponencial para programação dinâmica eficiente.

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
