# 🚀 Multiplicação Rápida de Inteiros Grandes

## 📋 Visão Geral

Este módulo implementa o **algoritmo de Karatsuba** para multiplicação rápida de números inteiros grandes representados como strings. O algoritmo é um exemplo clássico de **divisão e conquista** que reduz a complexidade de $O(n^2)$ para $O(n^{1.585})$.

## 🎯 Conceito Central

### Identidade Algébrica de Karatsuba

Para multiplicar dois números $x$ e $y$ de $n$ dígitos cada:

1. **Dividir**: $x = 10^m \cdot a + b$ e $y = 10^m \cdot c + d$
2. **Multiplicar**: $z_0 = b \cdot d$, $z_2 = a \cdot c$
3. **Otimizar**: $z_1 = (a + b) \cdot (c + d) - z_0 - z_2$
4. **Combinar**: $x \cdot y = 10^{2m} \cdot z_2 + 10^m \cdot z_1 + z_0$

### 🎨 Otimização Chave

A **otimização de Karatsuba** está na redução de **4 multiplicações** para **3 multiplicações**:

- ❌ **Tradicional**: $ac$, $ad$, $bc$, $bd$ (4 multiplicações)
- ✅ **Karatsuba**: $ac$, $bd$, $(a+b)(c+d)$ (3 multiplicações)

## 📁 Estrutura dos Arquivos

```
fast_multiplication/
├── __init__.py
├── karatsuba.py          # Implementação principal
├── test_karatsuba.py     # Testes abrangentes
└── README.md            # Esta documentação
```

## 🔧 Funções Principais

### `multiply_large_numbers(a: str, b: str) -> str`
Interface principal para multiplicação de números grandes.

**Parâmetros:**
- `a`: Primeiro número como string
- `b`: Segundo número como string

**Retorna:**
- Produto como string

**Exemplo:**
```python
result = multiply_large_numbers("123456789", "987654321")
# Resultado: "121932631112635269"
```

### `karatsuba_multiply(a: str, b: str) -> str`
Implementação do algoritmo de Karatsuba.

### `add_strings(str1: str, str2: str) -> str`
Adiciona dois números representados como strings.

### `subtract_strings(str1: str, str2: str) -> str`
Subtrai dois números representados como strings.

### `remove_leading_zeros(s: str) -> str`
Remove zeros à esquerda de uma string numérica.

## 🧪 Execução dos Testes

```bash
# Executar todos os testes do módulo
pytest algorithms/fast_multiplication/

# Executar testes específicos
pytest algorithms/fast_multiplication/test_karatsuba.py

# Executar com detalhes
pytest algorithms/fast_multiplication/test_karatsuba.py -v
```

## 📊 Casos de Teste

### ✅ Casos Básicos
- Multiplicação de dígitos únicos
- Números pequenos (2-4 dígitos)
- Números médios (5-10 dígitos)

### 🔥 Casos Extremos
- Números muito grandes (30+ dígitos)
- Multiplicação por zero
- Strings vazias
- Números palíndromos
- Potências de 10

### 🎯 Casos de Validação
- Consistência com multiplicação tradicional
- Validação de entrada inválida
- Performance comparison

## 🚀 Complexidade

| Operação | Complexidade | Descrição |
|----------|--------------|-----------|
| **Tempo** | $O(n^{1.585})$ | Melhor que $O(n^2)$ tradicional |
| **Espaço** | $O(n)$ | Recursão + strings temporárias |
| **Recorrência** | $T(n) = 3T(n/2) + O(n)$ | Master theorem aplicável |

## 📚 Referências

- **Erickson, "Algorithms"**: Capítulo 1, Seção 1.9, "Fast Multiplication"
- **GeeksforGeeks**: [Karatsuba Algorithm](https://www.geeksforgeeks.org/karatsuba-algorithm-for-fast-multiplication-of-large-decimal-numbers-represented-as-strings/)
- **Brilliant.org**: [Karatsuba Algorithm Explanation](https://brilliant.org/wiki/karatsuba-algorithm/)

## 🎯 Desafios de Implementação

### 🔧 Funções a Implementar

1. **`remove_leading_zeros(s: str) -> str`**
   - Remove zeros à esquerda mantendo pelo menos um zero
   - Exemplo: `"00123"` → `"123"`, `"000"` → `"0"`

2. **`karatsuba_multiply(a: str, b: str) -> str`**
   - Implementar a divisão dos números ao meio
   - Implementar as três multiplicações recursivas
   - Implementar a combinação dos resultados

### 💡 Dicas de Implementação

1. **Divisão dos Números:**
   ```python
   mid = len(a) // 2
   a_left = a[:mid]
   a_right = a[mid:]
   ```

2. **Multiplicações Recursivas:**
   ```python
   z0 = karatsuba_multiply(a_right, b_right)
   z2 = karatsuba_multiply(a_left, b_left)
   z1 = karatsuba_multiply(add_strings(a_left, a_right), 
                           add_strings(b_left, b_right))
   z1 = subtract_strings(subtract_strings(z1, z0), z2)
   ```

3. **Combinação dos Resultados:**
   ```python
   result = add_strings(
       add_strings(
           z2 + "0" * (2 * mid),  # 10^(2*mid) * z2
           z1 + "0" * mid          # 10^mid * z1
       ),
       z0                          # z0
   )
   ```

## 🏆 Objetivos de Aprendizado

- ✅ Compreender **divisão e conquista** em algoritmos
- ✅ Aplicar **otimizações algébricas** para melhorar complexidade
- ✅ Manipular **números grandes** representados como strings
- ✅ Implementar **operações aritméticas** básicas com strings
- ✅ Entender a **análise de recorrência** e Master Theorem
- ✅ Comparar **trade-offs** entre diferentes abordagens

## 🔍 Extensões Possíveis

- **Toom-Cook Algorithm**: Generalização do Karatsuba
- **FFT-based Multiplication**: Para números muito grandes
- **Binary Karatsuba**: Operação em base 2
- **Parallel Karatsuba**: Implementação paralela 