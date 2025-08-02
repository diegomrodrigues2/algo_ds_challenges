# 🔄 Backtracking

## 🎯 Visão Geral

Backtracking é uma estratégia para encontrar soluções para problemas computacionais, especialmente problemas de restrição, que constrói incrementalmente candidatos a soluções e abandona um candidato ("backtracks") assim que determina que ele não pode ser completado para uma solução válida.

## 📚 Conteúdo

### 01. [N-Rainhas](./01.%20N-Rainhas.md)
- **Problema Prototípico**: Exemplo clássico de backtracking
- **Exploração Sistemática**: Árvore de decisão completa
- **Otimizações**: Arrays auxiliares, quebra de simetria
- **Aplicações**: Puzzles, scheduling, circuit design

## 🎯 Conceitos-Chave

### 🔄 Estratégia de Backtracking
- **Exploração Sistemática**: Visita todos os candidatos a solução
- **Poda Inteligente**: Abandona ramos inviáveis cedo
- **Recursão**: Estrutura natural para backtracking
- **Estado**: Mantém estado parcial durante exploração

### ⚡ Otimizações Fundamentais
- **Verificação Eficiente**: O(1) para verificar viabilidade
- **Quebra de Simetria**: Reduz espaço de busca
- **Heurísticas**: Escolha inteligente de candidatos
- **Memoização**: Evita recálculos desnecessários

### 📊 Análise de Complexidade
- **Espaço de Busca**: Exponencial no pior caso
- **Poda Efetiva**: Reduz drasticamente o tempo
- **Fatores de Ramificação**: Determina performance prática
- **Limites Teóricos**: NP-completeness para muitos problemas

## 🚀 Aplicações Práticas
- **Puzzle Games**: Sudoku, Kakuro, Crossword
- **Scheduling**: Alocação de recursos sem conflitos
- **Circuit Design**: Layout de circuitos integrados
- **AI Planning**: Planejamento de ações em IA
- **Constraint Satisfaction**: Problemas de satisfação de restrições
- **Combinatorial Optimization**: Problemas de otimização combinatória

## 💡 Insights Teóricos
- **Exploração Sistemática**: Garante encontrar todas as soluções
- **Poda Inteligente**: Chave para performance prática
- **Simetrias**: Quebra de simetria reduz espaço de busca
- **Heurísticas**: Escolha de candidatos afeta performance
- **NP-Completeness**: Muitos problemas de backtracking são NP-completos
- **Estado Parcial**: Manutenção eficiente do estado é crucial
- **Recursão vs Iteração**: Trade-offs entre clareza e performance
- **Memoização**: Técnica para evitar recálculos

## 🔗 Referências

- **Erickson, "Algorithms"**: Capítulo 2, "Backtracking"
- **Jeff Erickson**: [Backtracking Chapter](https://jeffe.cs.illinois.edu/teaching/algorithms/book/02-backtracking.pdf)
- **Research Papers**: Análise de complexidade e otimizações
- **Implementações**: Código de referência e exemplos práticos 