"""
K-Nearest Neighbors (k-NN) para Regressão

Este módulo implementa o algoritmo k-NN para problemas de regressão.
O método k-NN é um algoritmo não paramétrico que prediz valores
baseado na média dos k vizinhos mais próximos.

Referência: The Elements of Statistical Learning, Seção 2.3.2
"""

import numpy as np
from typing import Union, Tuple


def euclidean_distance(x1: np.ndarray, x2: np.ndarray) -> float:
    """
    Calcula a distância euclidiana entre dois pontos.
    
    Args:
        x1: Primeiro ponto (array 1D)
        x2: Segundo ponto (array 1D)
        
    Returns:
        Distância euclidiana entre os pontos
    """
    # TODO: Implementar cálculo da distância euclidiana
    # Dica: Use np.sqrt() e np.sum()
    raise NotImplementedError("Implementar cálculo da distância euclidiana")


def find_k_nearest_neighbors(X_train: np.ndarray, x_query: np.ndarray, k: int) -> np.ndarray:
    """
    Encontra os k vizinhos mais próximos de x_query em X_train.
    
    Args:
        X_train: Matriz de características de treinamento (n_samples, n_features)
        x_query: Ponto de consulta (array 1D)
        k: Número de vizinhos a encontrar
        
    Returns:
        Índices dos k vizinhos mais próximos
    """
    # TODO: Implementar busca pelos k vizinhos mais próximos
    # 1. Calcular distâncias entre x_query e todos os pontos em X_train
    # 2. Encontrar os k índices com menores distâncias
    # Dica: Use np.argsort() para obter os índices ordenados
    raise NotImplementedError("Implementar busca pelos k vizinhos mais próximos")


def knn_regress(X_train: np.ndarray, y_train: np.ndarray, x_query: np.ndarray, k: int) -> float:
    """
    Prediz o valor para x_query usando k-NN para regressão.
    
    Para um ponto de consulta, identifica os k pontos mais próximos no conjunto
    de treinamento e prediz a média de suas respostas.
    
    Args:
        X_train: Matriz de características de treinamento (n_samples, n_features)
        y_train: Vetor de respostas de treinamento (n_samples,)
        x_query: Ponto de consulta (array 1D)
        k: Número de vizinhos a considerar
        
    Returns:
        Valor predito (média dos k vizinhos mais próximos)
        
    Raises:
        ValueError: Se k > n_samples ou k <= 0
        ValueError: Se dimensões de X_train e y_train não são compatíveis
    """
    # Validações
    if k <= 0:
        raise ValueError("k deve ser positivo")
    
    if k > len(X_train):
        raise ValueError("k não pode ser maior que o número de amostras de treinamento")
    
    if len(X_train) != len(y_train):
        raise ValueError("X_train e y_train devem ter o mesmo número de amostras")
    
    # TODO: Implementar algoritmo k-NN para regressão
    # 1. Encontrar os k vizinhos mais próximos
    # 2. Calcular a média dos valores y correspondentes
    # Dica: Use a função find_k_nearest_neighbors() que você implementou
    raise NotImplementedError("Implementar algoritmo k-NN para regressão")


def knn_regress_batch(X_train: np.ndarray, y_train: np.ndarray, X_query: np.ndarray, k: int) -> np.ndarray:
    """
    Prediz valores para múltiplos pontos de consulta usando k-NN para regressão.
    
    Args:
        X_train: Matriz de características de treinamento (n_samples, n_features)
        y_train: Vetor de respostas de treinamento (n_samples,)
        X_query: Matriz de pontos de consulta (n_queries, n_features)
        k: Número de vizinhos a considerar
        
    Returns:
        Array de valores preditos (n_queries,)
    """
    # TODO: Implementar predição em lote
    # Aplicar knn_regress() para cada ponto em X_query
    raise NotImplementedError("Implementar predição em lote")


class KNNRegressor:
    """
    Classe para k-Nearest Neighbors Regressor.
    
    Implementa o algoritmo k-NN para regressão seguindo a interface
    similar ao scikit-learn.
    """
    
    def __init__(self, k: int = 5):
        """
        Inicializa o regressor k-NN.
        
        Args:
            k: Número de vizinhos a considerar
        """
        self.k = k
        self.X_train = None
        self.y_train = None
        
    def fit(self, X: np.ndarray, y: np.ndarray) -> 'KNNRegressor':
        """
        Armazena os dados de treinamento (k-NN é um algoritmo lazy).
        
        Args:
            X: Matriz de características (n_samples, n_features)
            y: Vetor de respostas (n_samples,)
            
        Returns:
            self
        """
        # TODO: Implementar método fit
        # Apenas armazene X e y (k-NN não treina um modelo)
        raise NotImplementedError("Implementar método fit")
        
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Prediz valores para os pontos em X.
        
        Args:
            X: Matriz de pontos de consulta (n_queries, n_features)
            
        Returns:
            Array de valores preditos (n_queries,)
        """
        # TODO: Implementar método predict
        # Use knn_regress_batch() para predições em lote
        raise NotImplementedError("Implementar método predict") 