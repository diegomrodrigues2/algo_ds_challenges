# 🎯 Paralelismo de Tarefas

## 📋 Visão Geral

O paralelismo de tarefas é um paradigma fundamental que permite executar múltiplas operações computacionais de forma simultânea, focando na **identificação e execução de tarefas independentes** que podem rodar em paralelo.

## 🎯 Objetivos de Aprendizado

- **Distinguir** concorrência de paralelismo
- **Identificar** tarefas paralelizáveis em problemas
- **Implementar** soluções usando diferentes mecanismos
- **Reconhecer** e **mitigar** problemas de sincronização
- **Analisar** performance de algoritmos paralelos

## 📚 Conteúdo

### 01. Conceitos Fundamentais
- Concorrência vs Paralelismo
- Modelo de execução baseado em DAG
- Tipos de paralelismo (tarefas vs dados)
- Métricas de performance (Trabalho, Span, Paralelismo)

### 02. Desafios e Problemas
- Custos de comunicação e coordenação
- Condições de corrida e determinacy races
- Deadlocks e problemas de vivacidade
- Falso compartilhamento e contenda de cache
- Gerenciamento de tarefas dependentes

### 03. Mecanismos de Implementação
- **Python asyncio**: Coroutines, Tasks, Futures
- **C++**: Futures, passagem de mensagens
- **Java**: Executor Framework, técnicas avançadas
- Primitivas de sincronização

## 🔗 Relacionamentos

- **Fundamentos**: Baseia-se no modelo Fork-Join
- **Race Conditions**: Problemas específicos de sincronização
- **Multiplicação de Matrizes**: Exemplo prático de paralelismo de dados
- **Merge Sort Paralelo**: Exemplo de divisão de tarefas

## 💡 Aplicações Práticas

- **Web Scraping**: Múltiplas requisições simultâneas
- **Processamento de Imagens**: Pipeline de filtros
- **Simulações**: Múltiplas execuções independentes
- **Sistemas Distribuídos**: Coordenação de serviços 