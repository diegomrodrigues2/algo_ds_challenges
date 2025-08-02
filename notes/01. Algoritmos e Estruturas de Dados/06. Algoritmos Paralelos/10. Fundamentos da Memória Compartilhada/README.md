# 🔗 Fundamentos da Memória Compartilhada

## 📋 Visão Geral

Esta seção explora os fundamentos teóricos e práticos da computação concorrente com memória compartilhada, desde registradores básicos até construções complexas de snapshots atômicos.

## 🎯 Objetivos

- **Compreender** o modelo de computação concorrente com memória compartilhada
- **Analisar** diferentes tipos de registradores e suas propriedades
- **Implementar** construções de registradores mais fortes a partir de mais fracos
- **Entender** snapshots atômicos e suas aplicações

## 📚 Conteúdo

### 01. Modelo de Computação Concorrente
- **Fundamentos teóricos** da computação sequencial vs concorrente
- **Modelo de threads assíncronas** e comunicação via objetos compartilhados
- **Propriedades de segurança e vivacidade**

### 02. Espaço de Registradores
- **Tipos de registradores**: Safe, Regular, Atomic
- **Classificações**: SRSW, MRSW, MRMW
- **Condições de consistência** e suas implicações

### 03. Construções de Registradores
- **Hierarquia de construções** de registradores fracos para fortes
- **Algoritmos de implementação** com timestamps
- **Provas de correção** para cada construção

### 04. Snapshots Atômicos
- **Problema do snapshot** e suas aplicações
- **Implementações obstruction-free** e wait-free
- **Algoritmos de ajuda mútua** entre threads

## 🔧 Conceitos-Chave

- **Wait-free**: Cada método termina em número finito de passos
- **Linearizabilidade**: Comportamento equivalente a execução sequencial
- **Timestamps**: Mecanismo para ordenação de operações
- **Double collect**: Técnica para detectar estabilidade do estado

## 📖 Referências

- Herlihy & Shavit: "The Art of Multiprocessor Programming"
- Lynch: "Distributed Algorithms"
- Attiya & Welch: "Distributed Computing: Fundamentals, Simulations, and Advanced Topics" 