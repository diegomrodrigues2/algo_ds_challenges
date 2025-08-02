# 🚀 Exponenciação Rápida (Binary Exponentiation)

## 📋 Visão Geral

Este módulo implementa o **algoritmo de exponenciação rápida**, também conhecido como "exponentiation by squaring" ou "binary exponentiation", que calcula $x^n \bmod m$ em tempo $O(\log n)$ em vez de $O(n)$.

O algoritmo é fundamental para **criptografia** (RSA, Diffie-Hellman) e **computação científica**, permitindo calcular potências muito grandes de forma eficiente.

## 🎯 Conceito Central

### Representação Binária do Expoente

O algoritmo baseia-se na observação de que qualquer expoente $n$ pode ser expresso como uma soma de potências de 2:

$n = b_k \cdot 2^k + b_{k-1} \cdot 2^{k-1} + \ldots + b_0 \cdot 2^0$

Portanto: $x^n = x^{b_k \cdot 2^k} \cdot x^{b_{k-1} \cdot 2^{k-1}} \cdot \ldots \cdot x^{b_0 \cdot 2^0}$

### 🎨 Otimização Chave

Em vez de calcular $x^n$ com $n-1$ multiplicações, calculamos apenas $O(\log n)$ quadrados:

- **Tradicional**: $x \cdot x \cdot x \cdot \ldots \cdot x$ ($n-1$ multiplicações)
- **Binário**: $x^1, x^2, x^4, x^8, \ldots$ ($\log n$ quadrados)

## 📁 Estrutura dos Arquivos

```
fast_exponentiation/
├── __init__.py
├── binary_exponentiation.py    # Implementação principal
├── test_binary_exponentiation.py  # Testes abrangentes
└── README.md                  # Esta documentação
```

## 🔧 Funções Principais

### `power_mod(base: int, exponent: int, modulus: int) -> int`
Interface principal para exponenciação modular.

**Parâmetros:**
- `base`: Número base
- `exponent`: Expoente não-negativo
- `modulus`: Módulo (deve ser positivo)

**Retorna:**
- $(base^{exponent}) \bmod modulus$

**Exemplo:**
```python
result = power_mod(2, 100, 1000000007)
# Resultado: 976371285
```

### `binary_exponentiation(base: int, exponent: int) -> int`
Calcula $base^{exponent}$ usando exponenciação binária.

### `modular_exponentiation(base: int, exponent: int, modulus: int) -> int`
Calcula $(base^{exponent}) \bmod modulus$ de forma eficiente.

### `recursive_exponentiation(base: int, exponent: int) -> int`
Implementação recursiva que demonstra a recorrência:
- $x^n = (x^{n/2})^2$ se $n$ é par
- $x^n = x \cdot (x^{(n-1)/2})^2$ se $n$ é ímpar

### `matrix_exponentiation(matrix: list, exponent: int, modulus: int = None) -> list`
Calcula $matrix^{exponent}$ para matrizes 2×2.

### `fibonacci_fast(n: int, modulus: int = None) -> int`
Calcula o n-ésimo número de Fibonacci usando exponenciação de matriz.

## 🧪 Execução dos Testes

```bash
# Executar todos os testes do módulo
pytest algorithms/fast_exponentiation/

# Executar testes específicos
pytest algorithms/fast_exponentiation/test_binary_exponentiation.py

# Executar com detalhes
pytest algorithms/fast_exponentiation/test_binary_exponentiation.py -v
```

## 📊 Casos de Teste

### ✅ Casos Básicos
- Expoentes pequenos (0-10)
- Bases comuns (2, 3, 5, 10)
- Módulos pequenos (5, 7, 10, 13)

### 🔥 Casos Extremos
- Expoentes muito grandes (1000+)
- Módulos grandes (1000000007)
- Bases zero e um
- Expoentes zero

### 🎯 Casos de Validação
- Consistência com exponenciação tradicional
- Validação de entrada inválida
- Performance comparison
- Fibonacci com módulo

## 🚀 Complexidade

| Operação | Complexidade | Descrição |
|----------|--------------|-----------|
| **Tempo** | $O(\log n)$ | Melhor que $O(n)$ tradicional |
| **Espaço** | $O(1)$ | Apenas variáveis temporárias |
| **Multiplicações** | $O(\log n)$ | Uma por bit do expoente |

## 📚 Referências

- **Erickson, "Algorithms"**: Capítulo 1, Seção 1.10, "Exponentiation"
- **FreeCodeCamp**: [Binary Exponentiation Algorithm](https://www.freecodecamp.org/news/binary-exponentiation-algorithm-explained-with-examples/)
- **Attila Olah**: [Python Modular Exponentiation](https://attilaolah.eu/2011/05/22/python-modular-exponentiation-by-squaring/)
- **Khan Academy**: [Fast Modular Exponentiation](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/fast-modular-exponentiation)

## 🎯 Desafios de Implementação

### 🔧 Funções a Implementar

1. **`binary_exponentiation(base: int, exponent: int) -> int`**
   - Implementar exponenciação binária iterativa
   - Usar operações bitwise para verificar bits
   - Quadrar a base a cada iteração

2. **`modular_exponentiation(base: int, exponent: int, modulus: int) -> int`**
   - Implementar exponenciação modular
   - Aplicar módulo a cada multiplicação
   - Evitar overflow em cálculos grandes

3. **`recursive_exponentiation(base: int, exponent: int) -> int`**
   - Implementar versão recursiva
   - Usar divisão inteira e verificar paridade

4. **`matrix_exponentiation(matrix: list, exponent: int, modulus: int = None) -> list`**
   - Implementar exponenciação de matriz
   - Usar multiplicação de matrizes

5. **`fibonacci_fast(n: int, modulus: int = None) -> int`**
   - Implementar Fibonacci usando exponenciação de matriz
   - Usar a matriz [[1, 1], [1, 0]]

### 💡 Dicas de Implementação

1. **Exponenciação Binária Iterativa:**
   ```python
   result = 1
   while exponent > 0:
       if exponent & 1:  # Bit atual é 1
           result *= base
       base *= base      # Quadrar a base
       exponent >>= 1    # Mover para próximo bit
   ```

2. **Exponenciação Modular:**
   ```python
   result = 1
   base %= modulus
   while exponent > 0:
       if exponent & 1:
           result = (result * base) % modulus
       base = (base * base) % modulus
       exponent >>= 1
   ```

3. **Versão Recursiva:**
   ```python
   if exponent == 0:
       return 1
   if exponent % 2 == 0:
       half = recursive_exponentiation(base, exponent // 2)
       return half * half
   else:
       half = recursive_exponentiation(base, (exponent - 1) // 2)
       return base * half * half
   ```

4. **Multiplicação de Matrizes:**
   ```python
   def matrix_multiply(A, B, modulus=None):
       result = [[0, 0], [0, 0]]
       for i in range(2):
           for j in range(2):
               for k in range(2):
                   result[i][j] += A[i][k] * B[k][j]
               if modulus:
                   result[i][j] %= modulus
       return result
   ```

## 🏆 Objetivos de Aprendizado

- ✅ Compreender **exponenciação binária** e sua eficiência
- ✅ Aplicar **aritmética modular** em criptografia
- ✅ Implementar **exponenciação de matriz** para recorrências
- ✅ Entender **representação binária** de expoentes
- ✅ Comparar **versões iterativa e recursiva**
- ✅ Aplicar em **problemas práticos** (Fibonacci, RSA)

## 🔍 Aplicações Práticas

### 🔐 Criptografia
- **RSA**: $c = m^e \bmod n$
- **Diffie-Hellman**: $K = g^{ab} \bmod p$
- **ElGamal**: $c_1 = g^k \bmod p$

### 🧮 Computação Científica
- **Fibonacci rápido**: $F(n)$ em $O(\log n)$
- **Sequências lineares**: $a_n = c_1 a_{n-1} + c_2 a_{n-2}$
- **Cálculos de precisão**: Evitar overflow

### 🎯 Competições de Programação
- **Problemas de módulo**: Calcular $(a^b) \bmod m$
- **Sequências grandes**: Fibonacci, Lucas, etc.
- **Otimização**: Reduzir complexidade de $O(n)$ para $O(\log n)$

## 🔍 Extensões Possíveis

- **Exponenciação de Matrizes N×N**: Para recorrências de ordem superior
- **Exponenciação com Expoente Negativo**: Usando inversos modulares
- **Exponenciação com Expoente Racional**: Usando raízes
- **Exponenciação Paralela**: Para cálculos distribuídos 