# 🔄 Algoritmos Paralelos

Este diretório contém implementações de algoritmos paralelos usando o modelo **fork-join**, seguindo os princípios de **work/span analysis** para análise de performance.

## 📚 Conteúdo

### 🔢 Fibonacci Paralelo (`fibonacci_parallel.py`)
- **P-FIB**: Cálculo recursivo de números de Fibonacci usando spawn/sync
- **Análise**: Work = Θ(φⁿ), Span = Θ(n), Parallelism = Θ(φⁿ/n)
- **Característica**: Demonstra paralelismo exponencial

### 🔢 Multiplicação Matriz-Vetor (`matrix_vector_multiply.py`)
- **P-MAT-VEC**: Multiplicação paralela de matriz n×n por vetor n
- **Análise**: Work = Θ(n²), Span = Θ(n), Parallelism = Θ(n)
- **Característica**: Paraleliza apenas o loop externo para evitar races

## 🎯 Modelo Fork-Join

### 📤 Palavras-Chave
- **spawn**: Executa subrotina em paralelo
- **sync**: Sincroniza threads spawnadas
- **parallel for**: Loop com iterações paralelas

### 📊 Métricas de Performance
- **Work (T₁)**: Tempo total em 1 processador
- **Span (T₁)**: Tempo com ∞ processadores (caminho crítico)
- **Parallelism**: T₁/T₁ (razão work/span)

## 🧪 Execução dos Testes

```bash
# Executar todos os testes
pytest algorithms/parallel_algorithms/

# Teste específico
pytest algorithms/parallel_algorithms/test_fibonacci_parallel.py
pytest algorithms/parallel_algorithms/test_matrix_vector_multiply.py
```

## 📖 Documentação Teórica

### 📚 Notas de Estudo
- `notes/04. Algoritmos Paralelos/01. Fundamentos/01. Modelo Fork-Join.md`
- `notes/04. Algoritmos Paralelos/02. Multiplicação de Matrizes/01. Multiplicação Matriz-Vetor.md`
- `notes/04. Algoritmos Paralelos/02. Multiplicação de Matrizes/02. Multiplicação Recursiva.md`
- `notes/04. Algoritmos Paralelos/03. Merge Sort Paralelo/01. Algoritmo P-MERGE.md`
- `notes/04. Algoritmos Paralelos/04. Race Conditions/01. Determinacy Races.md`
- `notes/04. Algoritmos Paralelos/05. Estudo de Caso/01. Lição do Xadrez.md`

## ⚠️ Race Conditions

### 🏁 Exemplos de Races
```python
# ❌ INCORRETO - Race condition
parallel for i = 1 to n:
    parallel for j = 1 to n:
        y[i] = y[i] + A[i][j] * x[j]  # Múltiplas threads escrevem em y[i]
```

### ✅ Código Determinístico
```python
# ✅ CORRETO - Sem races
parallel for i = 1 to n:
    for j = 1 to n:
        y[i] = y[i] + A[i][j] * x[j]  # Cada thread tem seu próprio i
```

## 🎮 Implementação Prática

### 🔧 Limitações Atuais
- **Implementação Serial**: Por enquanto, as funções usam implementação serial
- **TODO**: Implementar spawn/sync reais usando threading ou multiprocessing
- **Foco**: Análise teórica e estrutura dos algoritmos

### 🚀 Próximos Passos
1. Implementar spawn/sync usando `concurrent.futures`
2. Adicionar merge sort paralelo (P-MERGE)
3. Implementar multiplicação recursiva de matrizes
4. Adicionar algoritmos de redução e scan

## 📈 Análise de Performance

### 🔍 Lei do Work e Span
```
Tₚ ≥ max(T₁/P, T₁)
```

### 🎯 Speedup Máximo
- **Linear Speedup**: T₁/Tₚ = P (speedup perfeito)
- **Limite**: T₁/Tₚ ≤ T₁/T₁ (parallelism)

### 📊 Slackness
- **Slackness > 1**: Boa escalabilidade
- **Slackness < 1**: Span domina, speedup limitado

## 🎯 Lições Aprendidas

### ✅ Boas Práticas
- **Identificar independência**: Paralelizar apenas operações independentes
- **Evitar races**: Cada saída modificada por uma thread
- **Análise work/span**: Sempre analisar antes de implementar

### ❌ Armadilhas
- **Paralelizar loops aninhados**: Pode criar races inesperadas
- **Ignorar span**: Focar apenas em reduzir work
- **Over-parallelization**: Overhead pode dominar benefício 