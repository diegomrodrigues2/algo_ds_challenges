# 🤖 Machine Learning

Este diretório contém implementações de algoritmos de Machine Learning em Python, focando em implementações **from-scratch** para aprendizado e compreensão profunda dos conceitos.

## 📚 Estrutura

```
machine_learning/
├── supervised_learning/     # Aprendizado Supervisionado
│   ├── knn_regression.py   # K-Nearest Neighbors para Regressão
│   └── test_knn_regression.py
├── unsupervised_learning/   # Aprendizado Não Supervisionado
├── optimization/           # Algoritmos de Otimização
├── feature_engineering/    # Engenharia de Features
└── evaluation/            # Métricas de Avaliação
```

## 🎯 Desafios Disponíveis

### Supervised Learning

#### K-Nearest Neighbors (k-NN) para Regressão
- **Arquivo**: `supervised_learning/knn_regression.py`
- **Testes**: `supervised_learning/test_knn_regression.py`
- **Conceito**: Algoritmo não paramétrico que prediz valores baseado na média dos k vizinhos mais próximos
- **Funções a implementar**:
  - `euclidean_distance()`: Cálculo de distância euclidiana
  - `find_k_nearest_neighbors()`: Busca pelos k vizinhos mais próximos
  - `knn_regress()`: Predição principal para um ponto
  - `knn_regress_batch()`: Predição em lote para múltiplos pontos
  - `KNNRegressor`: Classe com interface similar ao scikit-learn

#### Características do Desafio:
- **Dependências**: Apenas NumPy
- **Complexidade**: O(n) para predição, O(1) para treinamento
- **Casos de teste**: Inclui dados sintéticos, validações de entrada, e testes de comportamento esperado
- **Referência**: The Elements of Statistical Learning, Seção 2.3.2

## 🧪 Execução dos Testes

```bash
# Executar todos os testes de Machine Learning
pytest machine_learning/

# Executar testes específicos do k-NN
pytest machine_learning/supervised_learning/test_knn_regression.py

# Executar com verbose
pytest machine_learning/ -v
```

## 📋 Próximos Desafios Planejados

### Supervised Learning
- **Regressão Linear**: Implementação do gradiente descendente
- **Logistic Regression**: Classificação binária
- **Decision Trees**: Árvores de decisão para classificação e regressão
- **Random Forest**: Ensemble de árvores de decisão
- **Support Vector Machines**: SVM para classificação e regressão

### Unsupervised Learning
- **K-Means Clustering**: Agrupamento baseado em centroides
- **DBSCAN**: Clustering baseado em densidade
- **Principal Component Analysis**: Redução de dimensionalidade

### Optimization
- **Gradient Descent**: Otimização de primeira ordem
- **Stochastic Gradient Descent**: Variante estocástica
- **Adam Optimizer**: Otimizador adaptativo

## 🎯 Objetivos de Aprendizado

1. **Compreensão Teórica**: Entender os fundamentos matemáticos de cada algoritmo
2. **Implementação Prática**: Desenvolver algoritmos from-scratch em Python
3. **Validação**: Criar testes robustos que validem a correção das implementações
4. **Otimização**: Considerar aspectos de performance e eficiência
5. **Comparação**: Entender trade-offs entre diferentes algoritmos

## 📚 Referências

- **The Elements of Statistical Learning**: Hastie, Tibshirani, Friedman
- **Pattern Recognition and Machine Learning**: Bishop
- **Machine Learning**: Mitchell
- **Scikit-learn Documentation**: Para comparação com implementações de produção

## 🔧 Convenções

- **Dependências**: Usar apenas NumPy além do Python padrão
- **Documentação**: Incluir docstrings explicativas
- **Testes**: Cobertura completa com casos típicos e edge cases
- **Performance**: Considerar complexidade temporal e espacial
- **Interface**: Seguir padrões similares ao scikit-learn quando apropriado 