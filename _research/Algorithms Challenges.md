# Roteiro de Implementação Avançada: 100 Desafios de Algoritmos e Estruturas de Dados Baseados em "Algorithms" de Jeff Erickson





## Introdução





### Propósito e Filosofia



Este documento serve como um companheiro prático e focado em implementação para o livro-texto "Algorithms" de Jeff Erickson.1 O objetivo é fornecer um roteiro estruturado para dominar os conceitos apresentados no livro, não através da leitura passiva, mas por meio da implementação rigorosa e da experimentação. A filosofia de Erickson, que enfatiza a construção da intuição a partir de formulações recursivas antes de buscar a otimização, é o princípio orientador desta coleção de 100 desafios. Os problemas são projetados para serem resolvidos de forma incremental, espelhando a progressão do livro, desde os fundamentos da recursão e do backtracking até as complexidades da programação dinâmica, algoritmos de grafos, fluxos de rede e a teoria da NP-dificuldade.

O público-alvo deste roteiro é o estudante avançado de ciência da computação ou o engenheiro de software que busca aprofundar seu domínio algorítmico. Os desafios partem de um ponto avançado, assumindo familiaridade com estruturas de dados fundamentais e técnicas de prova, conforme delineado no prefácio do livro.1



### Estrutura dos Desafios



Cada um dos 100 desafios foi projetado para ser uma tarefa de programação autocontida, exigindo uma solução implementada "do zero" (from scratch) em Python. A estrutura de apresentação de cada desafio é inspirada em repositórios de codificação competitiva, garantindo clareza e facilitando testes sistemáticos. Cada desafio é apresentado com os seguintes componentes:

1. **ID e Título:** Um identificador único (1-100) e um nome descritivo para o problema.
2. **Enunciado do Problema:** Uma especificação precisa e formal do problema, incluindo os formatos de entrada e saída esperados.
3. **Vínculo Conceitual:** Uma referência explícita ao capítulo e à seção correspondentes no texto de Erickson 1, conectando a implementação prática à sua base teórica.
4. **Estrutura da Solução:** Um esqueleto de código Python sugerido, indicando a função principal a ser implementada.
5. **Estrutura de Testes:** Um exemplo de suíte de testes, no estilo do framework `pytest`, com casos de teste que cobrem casos base, casos gerais e cenários de borda críticos.



### Pré-requisitos



Este roteiro adota os mesmos pré-requisitos do livro de Erickson. Presume-se que o leitor tenha familiaridade com os seguintes tópicos 1:

- **Matemática Discreta:** Álgebra, teoria dos conjuntos, lógica de predicados, aritmética modular e definições recursivas.
- **Técnicas de Prova:** Indução, contradição e análise de casos.
- **Conceitos de Programação:** Variáveis, laços, recursão e ponteiros/referências.
- **Estruturas de Dados Fundamentais:** Arrays, listas ligadas, árvores de busca binária (incluindo uma forma balanceada como AVL ou Red-Black), tabelas hash e heaps binários.
- **Algoritmos Fundamentais:** Busca sequencial e binária, algoritmos de ordenação (Mergesort, Quicksort, etc.), e travessias em árvores (pré-ordem, em-ordem, pós-ordem).
- **Análise de Algoritmos:** Notação assintótica (O,Ω,Θ), tradução de laços em somatórios e de chamadas recursivas em recorrências.



## Mapeamento de Desafios para Conceitos



A tabela a seguir fornece um mapa de alto nível, conectando cada desafio aos principais conceitos e capítulos do livro de Jeff Erickson. Ela serve como um guia para navegar pela progressão dos tópicos, desde a recursão fundamental até as reduções de NP-dificuldade.

| ID do Desafio | Nome do Desafio                                    | Capítulo(s) Erickson | Conceitos Principais                                     |
| ------------- | -------------------------------------------------- | -------------------- | -------------------------------------------------------- |
| **Parte I**   | **Recursão, Backtracking e Divisão e Conquista**   | **1, 2**             |                                                          |
| 1-5           | Multiplicação Rápida e Exponenciação               | 1                    | Divisão e Conquista, Recorrências                        |
| 6-10          | Ordenação e Seleção Recursiva                      | 1                    | Quicksort, Mergesort, Quickselect                        |
| 11-15         | Backtracking Clássico                              | 2                    | N-Rainhas, Soma de Subconjuntos                          |
| 16-20         | Backtracking em Sequências                         | 2                    | Segmentação de Texto, LIS, OBST                          |
| **Parte II**  | **Programação Dinâmica**                           | **3**                |                                                          |
| 21-25         | Otimizando Backtracking com Memoização             | 3                    | Memoização, Recorrências                                 |
| 26-30         | DP Tabular (Bottom-Up)                             | 3                    | Ordem de Avaliação, Distância de Edição                  |
| 31-35         | Variações de Problemas de Subsequência             | 3                    | LCS, SCS, Subsequência Bitônica                          |
| 36-40         | Programação Dinâmica em Árvores                    | 3                    | Conjunto Independente Máximo em Árvore                   |
| **Parte III** | **Algoritmos Gulosos e Árvores Geradoras Mínimas** | **4, 7**             |                                                          |
| 41-45         | Problemas Gulosos Clássicos                        | 4                    | Escalonamento de Atividades, Códigos de Huffman          |
| 46-50         | Algoritmos de Árvore Geradora Mínima (MST)         | 7                    | Jarník (Prim), Kruskal, Borůvka                          |
| 51-55         | Estruturas de Dados para Algoritmos Gulosos        | 7                    | Fila de Prioridade, Union-Find                           |
| **Parte IV**  | **Algoritmos Fundamentais de Grafos**              | **5, 6, 8, 9**       |                                                          |
| 56-60         | Travessia em Grafos (BFS e DFS)                    | 5, 6                 | BFS, DFS, Componentes Conexos                            |
| 61-65         | Aplicações de Travessia                            | 6                    | Ordenação Topológica, Detecção de Ciclos, SCCs           |
| 66-70         | Caminhos Mínimos de Fonte Única (SSSP)             | 8                    | Dijkstra, Bellman-Ford, SSSP em DAGs                     |
| 71-75         | Caminhos Mínimos Todos-para-Todos (APSP)           | 9                    | Floyd-Warshall, Johnson                                  |
| **Parte V**   | **Fluxo Máximo e Corte Mínimo**                    | **10, 11**           |                                                          |
| 76-80         | Algoritmos de Fluxo Máximo                         | 10                   | Ford-Fulkerson, Edmonds-Karp                             |
| 81-85         | Modelagem com Fluxo: Emparelhamento e Cobertura    | 11                   | Emparelhamento Bipartido, Cobertura de Caminhos          |
| 86-90         | Modelagem com Fluxo: Problemas de Seleção          | 11                   | Seleção de Projetos, Eliminação no Beisebol              |
| **Parte VI**  | **NP-Dificuldade e Tópicos Avançados**             | **12**               |                                                          |
| 91-93         | Verificadores Polinomiais                          | 12                   | Definição de NP, Verificador para Ciclo Hamiltoniano     |
| 94-96         | Solucionadores de Tempo Exponencial                | 12                   | Solucionador Brute-Force para 3-SAT, TSP                 |
| 97-100        | Implementando Reduções Polinomiais                 | 12                   | 3-SAT para Independent Set, Vertex Cover para Subset Sum |

------



## Parte I: Recursão, Backtracking e Divisão e Conquista



Esta seção inicial foca nos Capítulos 1 e 2 de Erickson 1, que estabelecem a recursão como a ferramenta fundamental para o design de algoritmos. Os desafios aqui são projetados para solidificar a habilidade de "pensar recursivamente". A ênfase está na formulação correta da relação de recorrência e na implementação direta dessa lógica, mesmo que resulte em complexidade de tempo exponencial. Esta base é crucial, pois as otimizações nas seções subsequentes, como a programação dinâmica, dependem fundamentalmente de uma formulação recursiva correta.



### Divisão e Conquista (Capítulo 1)



Os algoritmos de divisão e conquista particionam o problema em subproblemas menores e independentes, resolvem-nos recursivamente e, em seguida, combinam suas soluções.

**Desafio 1: Multiplicação Rápida de Inteiros (Karatsuba)**

- **Enunciado do Problema:** Implemente o algoritmo de Karatsuba para multiplicar dois inteiros grandes. A entrada consistirá em dois números não negativos representados como strings, e a saída deve ser uma string representando seu produto. É proibido o uso de bibliotecas de inteiros de precisão arbitrária.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 1, Seção 1.9, "Fast Multiplication" (1, p. 40). O desafio testa a compreensão da identidade recursiva $ (10^m a + b)(10^m c + d) = 10^{2m}ac + 10^m(ad+bc) + bd $ e a otimização de Karatsuba que reduz quatro multiplicações de subproblemas para três.

**Desafio 2: Exponenciação Rápida (Elevação ao Quadrado Repetida)**

- **Enunciado do Problema:** Implemente um algoritmo de exponenciação rápida para calcular xnmodm em tempo logarítmico. A entrada são três inteiros: a base `x`, o expoente `n` (n≥0), e o módulo `m`.

- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 1, Seção 1.10, "Exponentiation" (1, p. 42). Este desafio se baseia na recorrência: 

  xn=(xn/2)2 se n for par, e xn=x⋅(x(n−1)/2)2 se n for ímpar.

**Desafio 3: Multiplicação de Inteiros Egípcia (Duplicação e Mediação)**

- **Enunciado do Problema:** Implemente o algoritmo de multiplicação "camponesa russa", que reduz a multiplicação a operações de adição, duplicação e divisão por dois. A entrada são dois inteiros positivos `x` e `y`.

- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 0, Seção 0.2, "Duplation and Mediation" (1, p. 5). Este é um exercício fundamental para entender a recursão através de uma identidade simples: 

  x⋅y=(⌊x/2⌋⋅2y) se x for par, e x⋅y=(⌊x/2⌋⋅2y)+y se x for ímpar.

**Desafio 4: Torre de Hanói**

- **Enunciado do Problema:** Implemente uma função que resolve o quebra-cabeça da Torre de Hanói. A função deve receber o número de discos `n` e os identificadores dos pinos de origem, destino e auxiliar. A saída deve ser a sequência de movimentos ("Mover disco 1 do pino A para o pino C").

- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 1, Seção 1.3, "Tower of Hanoi" (1, p. 24). Este é o exemplo canônico da "fé recursiva": resolver o problema para 

  n−1 discos e usar essa solução para mover o disco n.

**Desafio 5: Contagem de Inversões**

- **Enunciado do Problema:** Dado um array de números, conte o número de inversões, que são pares de índices (i,j) tais que i<j e A[i]>A[j]. O algoritmo deve ter complexidade O(nlogn).
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 1, Exercício 13 (1, p. 51). Este problema é uma variação clássica do Mergesort, onde a contagem de inversões ocorre durante a etapa de mesclagem.

**Desafio 6: Mergesort**

- **Enunciado do Problema:** Implemente o algoritmo Mergesort para ordenar um array de números.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 1, Seção 1.4, "Mergesort" (1, p. 26).

**Desafio 7: Quicksort (com Partição de Lomuto)**

- **Enunciado do Problema:** Implemente o algoritmo Quicksort usando a estratégia de partição de Lomuto, onde o pivô é tipicamente o último elemento.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 1, Seção 1.5, "Quicksort" (1, p. 29).

**Desafio 8: Quickselect**

- **Enunciado do Problema:** Implemente o algoritmo Quickselect para encontrar o k-ésimo menor elemento em um array não ordenado em tempo médio linear.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 1, Seção 1.8, "Linear-Time Selection" (1, p. 35).

**Desafio 9: Seleção em Tempo Linear no Pior Caso (Mediana das Medianas)**

- **Enunciado do Problema:** Implemente o algoritmo de seleção de Blum-Floyd-Pratt-Rivest-Tarjan (Mediana das Medianas) para encontrar o k-ésimo menor elemento em tempo linear no pior caso.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 1, Seção 1.8, "MOMSELECT" (1, p. 36). Este é um desafio avançado que requer uma implementação cuidadosa da escolha do pivô.

**Desafio 10: Encontrar o Elemento Mínimo e Máximo**

- **Enunciado do Problema:** Projete um algoritmo de divisão e conquista que encontre o elemento mínimo e máximo em um array de n números usando no máximo 3n/2 comparações.
- **Vínculo Conceitual:** Um problema clássico de divisão e conquista que ilustra como a combinação de resultados de subproblemas pode ser mais eficiente do que abordagens ingênuas.



### Backtracking (Capítulo 2)



Backtracking é uma estratégia para encontrar soluções para problemas computacionais, especialmente problemas de restrição, que constrói incrementalmente candidatos a soluções e abandona um candidato ("backtracks") assim que determina que ele não pode ser completado para uma solução válida.

**Desafio 11: N-Rainhas**

- **Enunciado do Problema:** Implemente um algoritmo de backtracking para encontrar todas as soluções para o problema das N-Rainhas, que consiste em posicionar N rainhas de xadrez em um tabuleiro N×N de forma que nenhuma rainha ameace outra.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 2, Seção 2.1, "N Queens" (1, p. 71). A implementação deve explorar recursivamente as possíveis posições para as rainhas, uma linha de cada vez.

**Desafio 12: Soma de Subconjuntos (Subset Sum)**

- **Enunciado do Problema:** Dado um conjunto de inteiros positivos `X` e um inteiro alvo `T`, implemente uma função de backtracking que determine se existe um subconjunto de `X` cujos elementos somam `T`.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 2, Seção 2.3, "Subset Sum" (1, p. 76). Para cada elemento, a recursão decide se o inclui ou não no subconjunto.

**Desafio 13: Segmentação de Texto**

- **Enunciado do Problema:** Dada uma string sem espaços e uma função `is_word(substring)` que retorna `True` se a substring for uma palavra válida, implemente um algoritmo de backtracking para determinar se a string pode ser segmentada em uma sequência de palavras válidas.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 2, Seção 2.5, "Text Segmentation" (1, p. 80).

**Desafio 14: Subsequência Crescente Mais Longa (LIS) - Versão Backtracking**

- **Enunciado do Problema:** Implemente um algoritmo de backtracking para encontrar o comprimento da subsequência crescente mais longa (LIS) de um dado array de números.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 2, Seção 2.6, "Longest Increasing Subsequence" (1, p. 86). Este desafio implementa a primeira formulação recursiva, que tem complexidade exponencial, preparando o terreno para a otimização com programação dinâmica.

**Desafio 15: Árvores de Busca Binária Ótimas (OBST) - Versão Backtracking**

- **Enunciado do Problema:** Dado um conjunto ordenado de chaves e suas frequências de busca, implemente um algoritmo de backtracking para encontrar o custo de uma árvore de busca binária ótima. O custo é a soma das profundidades de cada chave multiplicada por sua frequência.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 2, Seção 2.8, "Optimal Binary Search Trees" (1, p. 91).

**Desafio 16: Geração de Subconjuntos**

- **Enunciado do Problema:** Dado um conjunto de elementos distintos, implemente um algoritmo de backtracking para gerar todos os subconjuntos possíveis (o conjunto das partes).
- **Vínculo Conceitual:** Relacionado à estrutura de decisão do problema Subset Sum, mas com o objetivo de enumerar todas as possibilidades.

**Desafio 17: Geração de Permutações**

- **Enunciado do Problema:** Dado um conjunto de elementos distintos, implemente um algoritmo de backtracking para gerar todas as permutações possíveis.
- **Vínculo Conceitual:** Um problema clássico de backtracking onde a cada passo recursivo, um elemento ainda não utilizado é escolhido.

**Desafio 18: Coloração de Grafos**

- **Enunciado do Problema:** Dado um grafo não direcionado e um inteiro `k`, implemente um algoritmo de backtracking para determinar se o grafo pode ser colorido com `k` cores, de modo que vértices adjacentes não tenham a mesma cor.
- **Vínculo Conceitual:** Uma aplicação direta do backtracking para resolver um problema de satisfação de restrições em grafos.

**Desafio 19: Caminho Hamiltoniano**

- **Enunciado do Problema:** Dado um grafo, implemente um algoritmo de backtracking para encontrar um caminho Hamiltoniano, que é um caminho que visita cada vértice exatamente uma vez.
- **Vínculo Conceitual:** Um problema de busca em grafos que explora caminhos, fazendo backtracking quando um caminho não pode ser estendido para visitar todos os vértices restantes.

**Desafio 20: Jogo da Velha Generalizado**

- **Enunciado do Problema:** Implemente um solucionador de backtracking para um jogo da velha em um tabuleiro N×N, onde o objetivo é conseguir K peças em linha. A função deve determinar, a partir de um estado de jogo, se o jogador atual pode forçar uma vitória.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 2, Seção 2.2, "Game Trees" (1, p. 74). Este desafio envolve a exploração de uma árvore de jogo para encontrar uma estratégia vencedora.



## Parte II: Programação Dinâmica



Esta seção, baseada no Capítulo 3 de Erickson 1, aborda a programação dinâmica como "recursão inteligente". Os desafios são estruturados para ilustrar a transição de soluções de backtracking ineficientes para algoritmos eficientes através da memoização (top-down) e da tabulação (bottom-up). A chave é identificar os subproblemas sobrepostos e armazenar seus resultados.



### Otimização de Backtracking



**Desafio 21: Soma de Subconjuntos com Memoização**

- **Enunciado do Problema:** Modifique sua solução de backtracking para o problema da Soma de Subconjuntos (Desafio 12) para usar memoização. A função deve armazenar os resultados dos subproblemas `(i, t)` para evitar recálculos.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 3, Seção 3.1, "Memo(r)ization" (1, p. 99).

**Desafio 22: Segmentação de Texto com Memoização**

- **Enunciado do Problema:** Otimize sua solução de backtracking para a Segmentação de Texto (Desafio 13) usando memoização. O estado de um subproblema é definido pelo índice inicial do sufixo da string.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 3, Seção 3.3, "Interpunctio Verborum Redux" (1, p. 105).

**Desafio 23: LIS com Memoização**

- **Enunciado do Problema:** Otimize sua solução de backtracking para a Subsequência Crescente Mais Longa (Desafio 14) usando memoização. Use a formulação `LISbigger(i, j)`.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 3, Seção 3.6, "First Recurrence: Is This Next?" (1, p. 109).

**Desafio 24: Distância de Edição (Levenshtein) com Memoização**

- **Enunciado do Problema:** Implemente um algoritmo recursivo com memoização para calcular a distância de edição entre duas strings. A distância de edição é o número mínimo de inserções, exclusões ou substituições de um único caractere para transformar uma string na outra.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 3, Seção 3.7, "Edit Distance" (1, p. 111).

**Desafio 25: Fibonacci com Memoização**

- **Enunciado do Problema:** Implemente a função de Fibonacci usando recursão com memoização para alcançar complexidade de tempo linear.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 3, Seção 3.1, "Backtracking Can Be Slow" (1, p. 98). Este é o exemplo introdutório clássico para a programação dinâmica.



### Programação Dinâmica Tabular (Bottom-Up)



**Desafio 26: Fibonacci com Tabulação**

- **Enunciado do Problema:** Implemente a função de Fibonacci de forma iterativa (bottom-up), preenchendo uma tabela de valores.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 3, Seção 3.1, "Dynamic Programming: Fill Deliberately" (1, p. 101).

**Desafio 27: Soma de Subconjuntos com Tabulação**

- **Enunciado do Problema:** Resolva o problema da Soma de Subconjuntos usando um algoritmo de programação dinâmica tabular. Crie uma tabela 2D `S[i, t]` que armazena se um subconjunto de `X[i..n]` pode somar `t`.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 3, Seção 3.8, "Subset Sum" (1, p. 116).

**Desafio 28: Distância de Edição com Tabulação**

- **Enunciado do Problema:** Implemente o algoritmo de distância de edição de forma iterativa, preenchendo uma tabela 2D `Edit[i, j]`.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 3, Seção 3.7, "Dynamic Programming" (1, p. 113).

**Desafio 29: LIS com Tabulação (O(n²))**

- **Enunciado do Problema:** Implemente um algoritmo de programação dinâmica com complexidade O(n2) para o problema da Subsequência Crescente Mais Longa. Use um array `LIS[i]` para armazenar o comprimento da LIS que termina no índice `i`.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 3, Seção 3.6, "Second Recurrence: What's Next?" (1, p. 110).

**Desafio 30: Árvores de Busca Binária Ótimas com Tabulação**

- **Enunciado do Problema:** Implemente a solução de programação dinâmica com complexidade O(n3) para o problema da Árvore de Busca Binária Ótima.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 3, Seção 3.9, "Optimal Binary Search Trees" (1, p. 117).



### Variações de Problemas de Subsequência



**Desafio 31: Subsequência Comum Mais Longa (LCS)**

- **Enunciado do Problema:** Dadas duas strings, encontre o comprimento da subsequência comum mais longa (LCS).
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 3, Exercício 5(a) (1, p. 125). Um problema clássico de DP 2D.

**Desafio 32: Supersequência Comum Mais Curta (SCS)**

- **Enunciado do Problema:** Dadas duas strings, encontre o comprimento da supersequência comum mais curta.

- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 3, Exercício 5(b) (1, p. 125). Relacionado ao LCS pela identidade 

  ∣SCS(A,B)∣=∣A∣+∣B∣−∣LCS(A,B)∣.

**Desafio 33: Problema da Mochila 0/1 (0/1 Knapsack)**

- **Enunciado do Problema:** Dados os pesos e valores de `n` itens e a capacidade `W` de uma mochila, determine o valor máximo total de itens que podem ser colocados na mochila sem exceder a capacidade. Cada item pode ser escolhido ou não (0/1).
- **Vínculo Conceitual:** Um problema canônico de DP, não abordado diretamente nos capítulos principais de Erickson, mas fundamental no campo. A recorrência envolve decidir para cada item se ele é incluído ou não.

**Desafio 34: Problema de Troco de Moedas (Coin Change)**

- **Enunciado do Problema:** Dado um conjunto de denominações de moedas e um valor total, encontre o número mínimo de moedas necessárias para formar esse valor.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 3, Exercício 1 (1, p. 123).

**Desafio 35: Partição de Palíndromos**

- **Enunciado do Problema:** Dada uma string, encontre o número mínimo de cortes necessários para que cada substring resultante seja um palíndromo.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 3, Exercício 9(c) (1, p. 128).



### Programação Dinâmica em Árvores



**Desafio 36: Conjunto Independente Máximo em uma Árvore**

- **Enunciado do Problema:** Dado uma árvore (não necessariamente binária), encontre o tamanho do maior conjunto independente, que é um subconjunto de vértices em que não há dois vértices adjacentes.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 3, Seção 3.10, "Dynamic Programming on Trees" (1, p. 120).

**Desafio 37: Cobertura de Vértices Mínima em uma Árvore**

- **Enunciado do Problema:** Dada uma árvore, encontre o tamanho da menor cobertura de vértices, que é um subconjunto de vértices tal que toda aresta tem pelo menos um de seus extremos no subconjunto.
- **Vínculo Conceitual:** Relacionado ao conjunto independente máximo pelo Teorema de Kőnig para grafos bipartidos (e, portanto, para árvores): ∣MIS∣+∣MVC∣=∣V∣.

**Desafio 38: Diâmetro de uma Árvore**

- **Enunciado do Problema:** Dada uma árvore com pesos nas arestas, encontre o diâmetro, que é o caminho mais longo entre quaisquer dois nós na árvore.
- **Vínculo Conceitual:** Pode ser resolvido com duas buscas em largura/profundidade, mas também tem uma formulação de DP em árvores, calculando para cada nó a maior e a segunda maior profundidade em suas subárvores.

**Desafio 39: Coloração de Árvore com Custo Mínimo**

- **Enunciado do Problema:** Dada uma árvore enraizada e um conjunto de cores, onde cada nó `v` tem um custo `custo(v, c)` para ser colorido com a cor `c`, encontre uma coloração válida (nós adjacentes têm cores diferentes) com custo total mínimo.
- **Vínculo Conceitual:** Um problema de DP em árvores onde o estado para um nó `v` é `dp[v][c]`, o custo mínimo para colorir a subárvore de `v` com a cor `c`.

**Desafio 40: Maior Subárvore de Busca Binária em uma Árvore Binária**

- **Enunciado do Problema:** Dada uma árvore binária, encontre a maior subárvore que também é uma árvore de busca binária (BST). "Maior" refere-se ao número de nós.
- **Vínculo Conceitual:** Um problema de DP em árvores que requer uma travessia pós-ordem. Para cada nó, a função recursiva retorna informações sobre sua subárvore (se é uma BST, seu tamanho, o valor mínimo e o máximo).



## Parte III: Algoritmos Gulosos e Árvores Geradoras Mínimas



Esta seção, cobrindo os Capítulos 4 e 7 1, foca em algoritmos que fazem escolhas localmente ótimas na esperança de encontrar uma solução globalmente ótima. Erickson adverte que algoritmos gulosos "quase nunca funcionam", tornando a prova de correção um componente essencial. Os desafios aqui incluem problemas clássicos onde a abordagem gulosa é correta, com uma ênfase especial nos algoritmos de Árvore Geradora Mínima (MST).



### Problemas Gulosos Clássicos (Capítulo 4)



**Desafio 41: Escalonamento de Atividades (Scheduling)**

- **Enunciado do Problema:** Dado um conjunto de atividades, cada uma com um tempo de início e fim, selecione o subconjunto máximo de atividades não conflitantes.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 4, Seção 4.2, "Scheduling Classes" (1, p. 161). A estratégia gulosa correta é escolher a atividade que termina primeiro.

**Desafio 42: Códigos de Huffman**

- **Enunciado do Problema:** Dado um conjunto de caracteres e suas frequências, construa um código de prefixo ótimo (um Código de Huffman) para compressão de dados. Implemente a construção da árvore e a geração dos códigos.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 4, Seção 4.4, "Huffman Codes" (1, p. 165). Requer o uso de uma fila de prioridade.

**Desafio 43: Emparelhamento Estável (Gale-Shapley)**

- **Enunciado do Problema:** Implemente o algoritmo de Gale-Shapley para encontrar um emparelhamento estável entre dois conjuntos de elementos (por exemplo, médicos e hospitais), dadas as listas de preferências de cada elemento.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 4, Seção 4.5, "Stable Matching" (1, p. 170).

**Desafio 44: Problema da Mochila Fracionária**

- **Enunciado do Problema:** Resolva o problema da mochila fracionária, onde você pode pegar frações de itens. A estratégia gulosa é pegar os itens na ordem decrescente de sua razão valor/peso.
- **Vínculo Conceitual:** Um exemplo clássico onde uma abordagem gulosa funciona, em contraste com a versão 0/1 que requer DP.

**Desafio 45: Falha da Estratégia Gulosa**

- **Enunciado do Problema:** Para o problema da Mochila 0/1 (Desafio 33) e o problema de Troco de Moedas (Desafio 34), forneça um exemplo de entrada (itens/moedas e capacidades/valores) onde a estratégia gulosa mais óbvia (maior valor/peso primeiro; maior moeda primeiro) falha em produzir a solução ótima.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 3, Seção 3.5, "Warning: Greed is Stupid" (1, p. 107). Este desafio reforça a necessidade de cautela com algoritmos gulosos.



### Árvores Geradoras Mínimas (MST) (Capítulo 7)



**Desafio 46: Algoritmo de Jarník (Prim)**

- **Enunciado do Problema:** Implemente o algoritmo de Jarník (comumente conhecido como algoritmo de Prim) para encontrar uma Árvore Geradora Mínima (MST) de um grafo ponderado não direcionado. Use uma fila de prioridade para eficiência.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 7, Seção 7.4, "Jarník's ('Prim's') Algorithm" (1, p. 263).

**Desafio 47: Algoritmo de Kruskal**

- **Enunciado do Problema:** Implemente o algoritmo de Kruskal para encontrar uma MST. Este desafio requer a implementação de uma estrutura de dados Union-Find (Conjuntos Disjuntos) com compressão de caminho e união por ranking/tamanho.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 7, Seção 7.5, "Kruskal's Algorithm" (1, p. 265).

**Desafio 48: Algoritmo de Borůvka**

- **Enunciado do Problema:** Implemente o algoritmo de Borůvka para encontrar uma MST. Este algoritmo é notável por sua adequação a implementações paralelas.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 7, Seção 7.3, "Borůvka's Algorithm" (1, p. 261).

**Desafio 49: Estrutura de Dados Union-Find**

- **Enunciado do Problema:** Implemente a estrutura de dados Union-Find (Conjuntos Disjuntos) com as otimizações de compressão de caminho e união por ranking ou tamanho.
- **Vínculo Conceitual:** Essencial para a implementação eficiente do algoritmo de Kruskal.

**Desafio 50: Segunda Melhor MST**

- **Enunciado do Problema:** Dado um grafo, encontre a segunda melhor árvore geradora mínima, ou seja, a MST com o segundo menor peso total.
- **Vínculo Conceitual:** Um problema avançado que pode ser resolvido analisando as arestas não presentes na MST e os ciclos que elas formam.



### Outros Problemas Gulosos



**Desafio 51: Cobertura de Conjuntos em uma Linha**

- **Enunciado do Problema:** Dado um conjunto de intervalos na linha real, encontre o menor subconjunto de intervalos cuja união cobre a mesma região que a união de todos os intervalos originais.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 4, Exercício 3 (1, p. 178).

**Desafio 52: Menor Conjunto de Pontos para "Furar" Intervalos**

- **Enunciado do Problema:** Dado um conjunto de intervalos, encontre o menor conjunto de pontos tal que cada intervalo contenha pelo menos um ponto.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 4, Exercício 4 (1, p. 178).

**Desafio 53: Coloração de Grafos de Intervalo**

- **Enunciado do Problema:** Dado um conjunto de intervalos, encontre o número mínimo de cores necessárias para colorir cada intervalo de forma que intervalos sobrepostos tenham cores diferentes.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 4, Exercício 5 (1, p. 178).

**Desafio 54: Atribuição de Esquis a Esquiadores**

- **Enunciado do Problema:** Dados `n` esquiadores com alturas `P[1..n]` e `n` esquis com alturas `S[1..n]`, atribua um esqui a cada esquiador para minimizar a diferença média de altura.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 4, Exercício 17 (1, p. 181).

**Desafio 55: Menor Número de Paradas para Reabastecimento**

- **Enunciado do Problema:** Você está dirigindo um carro que pode viajar `L` milhas com um tanque cheio. Dada uma rota com postos de gasolina, encontre o número mínimo de paradas para reabastecer para chegar ao destino.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 4, Exercício 20(a) (1, p. 183).



## Parte IV: Algoritmos Fundamentais de Grafos



Esta seção, a mais extensa, cobre os Capítulos 5, 6, 8 e 9 de Erickson.1 Ela aborda os pilares da teoria dos grafos algorítmica: travessia, conectividade e problemas de caminho mínimo. Os desafios são projetados para construir uma base sólida, começando com implementações de BFS e DFS e progredindo para algoritmos de caminho mínimo mais complexos, destacando suas diferenças, casos de uso e a estrutura unificadora da "relaxação de arestas".



### Travessia em Grafos (Capítulos 5 e 6)



**Desafio 56: Implementação de Grafo (Lista e Matriz de Adjacência)**

- **Enunciado do Problema:** Crie uma classe `Graph` em Python que possa representar grafos direcionados e não direcionados. A classe deve suportar internamente tanto a representação por lista de adjacência quanto por matriz de adjacência e fornecer métodos para adicionar vértices, adicionar arestas e obter vizinhos.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 5, Seção 5.4, "Data Structures" (1, p. 195).

**Desafio 57: Busca em Largura (BFS)**

- **Enunciado do Problema:** Implemente a Busca em Largura (BFS) a partir de um vértice de origem em um grafo. A função deve retornar as distâncias (em número de arestas) da origem para todos os vértices alcançáveis.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 5, Seção 5.6, "Queue: Breadth-First" (1, p. 202).

**Desafio 58: Busca em Profundidade (DFS) - Recursiva e Iterativa**

- **Enunciado do Problema:** Implemente a Busca em Profundidade (DFS) de duas maneiras: uma versão recursiva e uma versão iterativa usando uma pilha explícita.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 5, Seção 5.6, "Stack: Depth-First" (1, p. 201).

**Desafio 59: Componentes Conexos (Grafos Não Direcionados)**

- **Enunciado do Problema:** Dado um grafo não direcionado, use BFS ou DFS para encontrar e rotular seus componentes conexos.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 5, Seção 5.6, "Disconnected Graphs" (1, p. 203).

**Desafio 60: Detecção de Ciclos em Grafos Direcionados e Não Direcionados**

- **Enunciado do Problema:** Implemente um algoritmo baseado em DFS para detectar se um grafo (direcionado ou não direcionado) contém um ciclo. Para grafos direcionados, use a coloração dos vértices (branco, cinza, preto).
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 6, Seção 6.2, "Detecting Cycles" (1, p. 231).

**Desafio 61: Ordenação Topológica**

- **Enunciado do Problema:** Implemente um algoritmo para encontrar uma ordenação topológica de um grafo acíclico direcionado (DAG).
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 6, Seção 6.3, "Topological Sort" (1, p. 232).

**Desafio 62: Componentes Fortemente Conexos (Kosaraju-Sharir)**

- **Enunciado do Problema:** Implemente o algoritmo de Kosaraju-Sharir para encontrar os componentes fortemente conexos (SCCs) de um grafo direcionado.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 6, Seção 6.6, "Kosaraju and Sharir's Algorithm" (1, p. 238).

**Desafio 63: Componentes Fortemente Conexos (Tarjan)**

- **Enunciado do Problema:** Implemente o algoritmo de Tarjan para encontrar os SCCs de um grafo direcionado. Este algoritmo realiza apenas uma passagem de DFS.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 6, Seção 6.6, "Tarjan's Algorithm" (1, p. 242).

**Desafio 64: Pontos de Articulação**

- **Enunciado do Problema:** Dado um grafo não direcionado, encontre todos os seus pontos de articulação (ou vértices de corte), que são vértices cuja remoção aumenta o número de componentes conexos.
- **Vínculo Conceitual:** Uma aplicação clássica da DFS que usa os tempos de descoberta e os valores "low-link".

**Desafio 65: Pontes**

- **Enunciado do Problema:** Dado um grafo não direcionado, encontre todas as suas pontes, que são arestas cuja remoção aumenta o número de componentes conexos.
- **Vínculo Conceitual:** Similar aos pontos de articulação, também resolvido com uma única passagem de DFS.



### Caminhos Mínimos de Fonte Única (SSSP) (Capítulo 8)



**Desafio 66: Caminhos Mínimos em Grafos Não Ponderados (BFS)**

- **Enunciado do Problema:** Use sua implementação de BFS para encontrar os caminhos mínimos (em número de arestas) de um vértice de origem `s` para todos os outros vértices em um grafo não ponderado.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 8, Seção 8.4, "Unweighted Graphs: Breadth-First Search" (1, p. 278).

**Desafio 67: Caminhos Mínimos em DAGs**

- **Enunciado do Problema:** Implemente um algoritmo de tempo linear para encontrar os caminhos mínimos de uma fonte `s` em um grafo acíclico direcionado (DAG) com pesos de aresta possivelmente negativos.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 8, Seção 8.5, "Directed Acyclic Graphs: Depth-First Search" (1, p. 282).

**Desafio 68: Algoritmo de Dijkstra**

- **Enunciado do Problema:** Implemente o algoritmo de Dijkstra para encontrar os caminhos mínimos de uma fonte `s` em um grafo com pesos de aresta não negativos. Use uma fila de prioridade para eficiência.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 8, Seção 8.6, "Best-First: Dijkstra's Algorithm" (1, p. 284).

**Desafio 69: Algoritmo de Bellman-Ford**

- **Enunciado do Problema:** Implemente o algoritmo de Bellman-Ford para encontrar os caminhos mínimos de uma fonte `s` em um grafo que pode ter arestas com pesos negativos. Sua implementação deve detectar e relatar a presença de ciclos de peso negativo alcançáveis a partir de `s`.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 8, Seção 8.7, "Relax ALL the Edges: Bellman-Ford" (1, p. 289).

**Desafio 70: Detecção de Ciclo de Arbitragem**

- **Enunciado do Problema:** Dado um conjunto de taxas de câmbio entre moedas, modele o problema como um grafo e use uma variação do algoritmo de Bellman-Ford para detectar se existe uma oportunidade de arbitragem (um ciclo cujo produto das taxas é > 1, o que corresponde a um ciclo de peso negativo se os pesos forem logaritmos negativos das taxas).
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 9, Exercício 6 (1, p. 321).



### Caminhos Mínimos Todos-para-Todos (APSP) (Capítulo 9)



**Desafio 71: APSP com Múltiplas Execuções de SSSP**

- **Enunciado do Problema:** Implemente um algoritmo de caminhos mínimos todos-para-todos executando um algoritmo SSSP (Dijkstra ou Bellman-Ford, dependendo dos pesos das arestas) a partir de cada vértice do grafo.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 9, Seção 9.2, "Lots of Single Sources" (1, p. 310).

**Desafio 72: Algoritmo de Floyd-Warshall**

- **Enunciado do Problema:** Implemente o algoritmo de Floyd-Warshall para resolver o problema de caminhos mínimos todos-para-todos em O(V3).
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 9, Seção 9.8, "(Kleene-Roy-)Floyd-Warshall(-Ingerman)" (1, p. 318).

**Desafio 73: Algoritmo de Johnson**

- **Enunciado do Problema:** Implemente o algoritmo de Johnson para o problema de caminhos mínimos todos-para-todos, que é eficiente em grafos esparsos com pesos de aresta negativos. Requer a execução de Bellman-Ford uma vez, seguida por `V` execuções de Dijkstra.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 9, Seção 9.4, "Johnson's Algorithm" (1, p. 312).

**Desafio 74: Fecho Transitivo**

- **Enunciado do Problema:** Dado um grafo direcionado, calcule seu fecho transitivo. Isso pode ser feito usando o algoritmo de Floyd-Warshall em um grafo não ponderado ou através de multiplicação de matrizes booleanas.
- **Vínculo Conceitual:** Uma aplicação direta do conceito de alcançabilidade todos-para-todos.

**Desafio 75: Multiplicação de Matrizes Min-Plus**

- **Enunciado do Problema:** Implemente a multiplicação de matrizes "min-plus" (ou "distance product"). Mostre como o problema APSP pode ser resolvido com logV multiplicações min-plus.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 9, Seção 9.7, "Funny Matrix Multiplication" (1, p. 316).



## Parte V: Fluxo Máximo e Corte Mínimo



Esta seção, baseada nos Capítulos 10 e 11 1, explora um dos tópicos mais poderosos e versáteis da otimização combinatória. Os desafios começam com a implementação dos algoritmos fundamentais de fluxo e, em seguida, se concentram na habilidade crucial de modelar problemas aparentemente não relacionados como problemas de fluxo máximo ou corte mínimo.



### Algoritmos Fundamentais de Fluxo (Capítulo 10)



**Desafio 76: Algoritmo de Ford-Fulkerson (Genérico)**

- **Enunciado do Problema:** Implemente o método genérico de Ford-Fulkerson para encontrar o fluxo máximo em uma rede. A implementação deve construir e atualizar explicitamente o grafo residual e encontrar um caminho de aumento usando DFS ou BFS.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 10, Seção 10.4, "Ford and Fulkerson's augmenting-path algorithm" (1, p. 334).

**Desafio 77: Heurística de Edmonds-Karp (Caminho Mais Curto)**

- **Enunciado do Problema:** Especialize sua implementação de Ford-Fulkerson para usar a heurística de Edmonds-Karp, onde o caminho de aumento é sempre o caminho mais curto (em número de arestas) no grafo residual, encontrado via BFS.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 10, Seção 10.6, "Shortest Augmenting Paths" (1, p. 341).

**Desafio 78: Heurística de Edmonds-Karp (Caminho Mais "Gordo")**

- **Enunciado do Problema:** Especialize sua implementação de Ford-Fulkerson para usar a heurística do caminho mais "gordo" (fattest augmenting path), onde o caminho de aumento é aquele com a maior capacidade de gargalo.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 10, Seção 10.6, "Fattest Augmenting Paths" (1, p. 340).

**Desafio 79: Decomposição de Fluxo**

- **Enunciado do Problema:** Dado um fluxo `f` em uma rede, implemente um algoritmo para decompor `f` em uma soma de fluxos de caminho e de ciclo.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 10, Seção 10.5, "Combining and Decomposing Flows" (1, p. 336).

**Desafio 80: Encontrando um Corte Mínimo**

- **Enunciado do Problema:** Dado uma rede e um fluxo máximo, encontre um corte (s, t) mínimo correspondente. Isso pode ser feito encontrando todos os vértices alcançáveis a partir de `s` no grafo residual final.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 10, Seção 10.3, "The Maxflow-Mincut Theorem" (1, p. 331).



### Aplicações e Modelagem (Capítulo 11)



**Desafio 81: Emparelhamento Bipartido Máximo**

- **Enunciado do Problema:** Resolva o problema do emparelhamento bipartido máximo reduzindo-o a um problema de fluxo máximo. Crie uma função que receba um grafo bipartido e o converta em uma rede de fluxo apropriada.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 11, Seção 11.3, "Bipartite Matching" (1, p. 355).

**Desafio 82: Caminhos Vértice-Disjuntos**

- **Enunciado do Problema:** Dados um grafo direcionado e dois vértices `s` e `t`, encontre o número máximo de caminhos vértice-disjuntos de `s` a `t`. Modele este problema usando fluxo máximo com capacidades nos vértices.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 11, Seção 11.2, "Vertex Capacities and Vertex-Disjoint Paths" (1, p. 354).

**Desafio 83: Cobertura Mínima de Caminhos em um DAG**

- **Enunciado do Problema:** Dado um DAG, encontre o número mínimo de caminhos vértice-disjuntos necessários para cobrir todos os vértices. Reduza este problema a um emparelhamento bipartido máximo.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 11, Seção 11.5, "Disjoint-Path Covers" (1, p. 360).

**Desafio 84: Eliminação no Beisebol**

- **Enunciado do Problema:** Implemente um algoritmo para resolver o problema da eliminação no beisebol. Dada a classificação atual (vitórias, derrotas) e o cronograma de jogos restantes, determine se uma equipe específica está matematicamente eliminada da primeira posição.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 11, Seção 11.6, "Baseball Elimination" (1, p. 363).

**Desafio 85: Seleção de Projetos**

- **Enunciado do Problema:** Dado um conjunto de projetos com lucros (ou custos) associados e um conjunto de dependências (o projeto A deve ser feito para que o projeto B possa ser feito), encontre um subconjunto de projetos que maximize o lucro total. Modele como um problema de corte mínimo.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 11, Seção 11.7, "Project Selection" (1, p. 366).

**Desafio 86: Escalonamento de Exames**

- **Enunciado do Problema:** Resolva um problema de escalonamento de exames com restrições de salas, horários e fiscais, modelando-o como um problema de seleção de tuplas que pode ser resolvido com fluxo máximo.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 11, Seção 11.4, "Exam Scheduling" (1, p. 358).

**Desafio 87: Cobertura de Vértices em Grafos Bipartidos**

- **Enunciado do Problema:** Encontre a cobertura de vértices mínima em um grafo bipartido. Use o Teorema de Kőnig, que afirma que o tamanho do emparelhamento máximo é igual ao tamanho da cobertura de vértices mínima.
- **Vínculo Conceitual:** Uma aplicação direta do emparelhamento bipartido.

**Desafio 88: Circulação com Demandas**

- **Enunciado do Problema:** Dado um grafo com demandas em cada aresta (um fluxo mínimo necessário), determine se existe uma circulação viável (um fluxo com divergência zero em todos os vértices).
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 10, Exercício 12 (1, p. 347).

**Desafio 89: Atribuição de Tripulação de Voo**

- **Enunciado do Problema:** Dada uma lista de voos e uma lista de tripulações, com restrições sobre quais voos cada tripulação pode operar e regras sobre descanso, atribua tripulações aos voos para cobrir o máximo de voos possível. Modele como um problema de fluxo.
- **Vínculo Conceitual:** Uma variação do problema de emparelhamento/seleção de tuplas.

**Desafio 90: Arredondamento de Matrizes**

- **Enunciado do Problema:** Dada uma matriz de números reais, arredonde cada entrada para o inteiro acima ou abaixo, de modo que as somas das linhas e colunas permaneçam inalteradas. Modele como um problema de circulação.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 11, Exercício 16 (1, p. 374).



## Parte VI: NP-Dificuldade e Tópicos Avançados



Esta seção final, baseada no Capítulo 12 1, é de natureza mais teórica. Como não se espera que problemas NP-difíceis sejam resolvidos eficientemente, os desafios aqui são não convencionais. Em vez de buscar soluções rápidas, eles se concentram em implementar os próprios 

*conceitos* da teoria da complexidade, como verificadores, solucionadores de força bruta e, o mais importante, as reduções polinomiais que estão no cerne das provas de NP-dificuldade.

**Desafio 91: Verificador para o Problema do Caixeiro Viajante (TSP)**

- **Enunciado do Problema:** Escreva uma função que atue como um verificador para o problema do caixeiro viajante na sua versão de decisão. A função recebe um grafo ponderado, um "certificado" (uma sequência de vértices) e um limite de custo `k`. Ela deve retornar `True` se o certificado for um ciclo Hamiltoniano válido com custo total no máximo `k`, e `False` caso contrário. A função deve rodar em tempo polinomial.
- **Vínculo Conceitual:** Este desafio torna concreta a definição de NP: um problema está em NP se uma solução proposta pode ser verificada em tempo polinomial.

**Desafio 92: Verificador para 3-Coloração**

- **Enunciado do Problema:** Escreva um verificador polinomial para o problema de 3-Coloração. A função recebe um grafo e uma "coloração" (uma atribuição de cores de {0, 1, 2} para cada vértice) e retorna `True` se a coloração for válida.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 12, Seção 12.10, "Graph Coloring" (1, p. 395).

**Desafio 93: Verificador para Soma de Subconjuntos**

- **Enunciado do Problema:** Escreva um verificador polinomial para o problema da Soma de Subconjuntos. A função recebe o conjunto `X`, o alvo `T`, e um subconjunto candidato, e verifica se os elementos do subconjunto somam `T`.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 12, Seção 12.12, "Subset Sum" (1, p. 402).

**Desafio 94: Solucionador Exponencial para 3-SAT**

- **Enunciado do Problema:** Implemente um solucionador de força bruta para o 3-SAT. O algoritmo deve testar todas as 2n atribuições de verdade possíveis para as `n` variáveis e retornar `True` se encontrar uma que satisfaça a fórmula.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 12, Seção 12.6, "3SAT" (1, p. 388). Este exercício demonstra na prática a complexidade exponencial de problemas NP-difíceis.

**Desafio 95: Solucionador Exponencial para o Caixeiro Viajante**

- **Enunciado do Problema:** Implemente um solucionador de força bruta para o problema do caixeiro viajante. O algoritmo deve gerar todas as (n−1)! permutações de vértices, calcular o custo de cada ciclo Hamiltoniano e retornar o custo mínimo.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 12, Seção 12.11, "Hamiltonian Cycle" (1, p. 398).

**Desafio 96: Solucionador Exponencial para Cobertura de Vértices**

- **Enunciado do Problema:** Implemente um solucionador de força bruta para o problema da Cobertura de Vértices Mínima. O algoritmo deve testar todos os subconjuntos de vértices de tamanho 1, 2,..., |V| até encontrar o menor que seja uma cobertura de vértices.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 12, Seção 12.9, "Vertex Cover" (1, p. 394).

**Desafio 97: Implementando a Redução de 3-SAT para Conjunto Independente Máximo**

- **Enunciado do Problema:** Escreva uma função que receba uma fórmula 3-CNF e a transforme em um grafo `G` e um inteiro `k`, de acordo com a redução descrita por Erickson. A função deve retornar `G` e `k` tais que `G` tem um conjunto independente de tamanho `k` se e somente se a fórmula for satisfatível.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 12, Seção 12.7, "Maximum Independent Set (from 3SAT)" (1, p. 390). Este é um desafio de implementação de uma prova de NP-dificuldade.

**Desafio 98: Implementando a Redução de Cobertura de Vértices para Soma de Subconjuntos**

- **Enunciado do Problema:** Escreva uma função que receba um grafo `G` e um inteiro `k` e os transforme em um conjunto de inteiros `X` e um alvo `T`, de acordo com a redução de Cobertura de Vértices para Soma de Subconjuntos. A redução envolve a construção de números grandes em base 4.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 12, Seção 12.12, "Subset Sum (from Vertex Cover)" (1, p. 402).

**Desafio 99: Implementando a Redução de Conjunto Independente para Cobertura de Vértices**

- **Enunciado do Problema:** Escreva uma função que receba um grafo `G` e um inteiro `k` para uma instância do problema do Conjunto Independente Máximo e retorne um grafo `G'` e um inteiro `k'` para uma instância do problema da Cobertura de Vértices Mínima. A redução é trivial: G′=G e k′=∣V∣−k.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 12, Seção 12.9, "Clique and Vertex Cover" (1, p. 394).

**Desafio 100: Implementando a Redução de Ciclo Hamiltoniano para Caminho Hamiltoniano**

- **Enunciado do Problema:** Escreva uma função que transforme uma instância do problema do Ciclo Hamiltoniano em uma instância do problema do Caminho Hamiltoniano.
- **Vínculo Conceitual:** Erickson, "Algorithms", Capítulo 12, Exercício 10 (1, p. 418). Este desafio finaliza a jornada, solidificando a habilidade de manipular e conectar problemas complexos através de transformações algorítmicas.