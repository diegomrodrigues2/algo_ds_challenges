"""
Testes para K-Nearest Neighbors (k-NN) para Regressão

Este módulo contém testes automatizados para validar a implementação
do algoritmo k-NN para problemas de regressão.
"""

import pytest
import numpy as np
from .knn_regression import (
    euclidean_distance,
    find_k_nearest_neighbors,
    knn_regress,
    knn_regress_batch,
    KNNRegressor
)


class TestEuclideanDistance:
    """Testes para a função de cálculo de distância euclidiana."""
    
    def test_euclidean_distance_1d(self):
        """Testa distância euclidiana em 1D."""
        x1 = np.array([0])
        x2 = np.array([3])
        expected = 3.0
        result = euclidean_distance(x1, x2)
        assert np.isclose(result, expected)
    
    def test_euclidean_distance_2d(self):
        """Testa distância euclidiana em 2D."""
        x1 = np.array([0, 0])
        x2 = np.array([3, 4])
        expected = 5.0  # sqrt(3² + 4²) = 5
        result = euclidean_distance(x1, x2)
        assert np.isclose(result, expected)
    
    def test_euclidean_distance_same_point(self):
        """Testa distância entre pontos idênticos."""
        x1 = np.array([1, 2, 3])
        x2 = np.array([1, 2, 3])
        expected = 0.0
        result = euclidean_distance(x1, x2)
        assert np.isclose(result, expected)
    
    def test_euclidean_distance_negative_values(self):
        """Testa distância com valores negativos."""
        x1 = np.array([-1, -2])
        x2 = np.array([2, 3])
        expected = np.sqrt(3**2 + 5**2)  # sqrt(9 + 25) = sqrt(34)
        result = euclidean_distance(x1, x2)
        assert np.isclose(result, expected)


class TestFindKNearestNeighbors:
    """Testes para a função de busca por k vizinhos mais próximos."""
    
    def test_find_k_nearest_neighbors_simple(self):
        """Testa busca simples por k vizinhos."""
        X_train = np.array([[0, 0], [1, 0], [0, 1], [2, 2]])
        x_query = np.array([0, 0])
        k = 2
        
        result = find_k_nearest_neighbors(X_train, x_query, k)
        expected = np.array([0, 1])  # [0,0] e [1,0] são os mais próximos
        
        # Verifica se os índices estão corretos (ordem pode variar)
        assert len(result) == k
        assert set(result) == set(expected)
    
    def test_find_k_nearest_neighbors_all_points(self):
        """Testa busca quando k = número total de pontos."""
        X_train = np.array([[0, 0], [1, 1], [2, 2]])
        x_query = np.array([1, 1])
        k = 3
        
        result = find_k_nearest_neighbors(X_train, x_query, k)
        
        assert len(result) == k
        assert set(result) == {0, 1, 2}
    
    def test_find_k_nearest_neighbors_exact_match(self):
        """Testa quando o ponto de consulta é idêntico a um ponto de treino."""
        X_train = np.array([[0, 0], [1, 1], [2, 2]])
        x_query = np.array([1, 1])
        k = 1
        
        result = find_k_nearest_neighbors(X_train, x_query, k)
        
        assert len(result) == 1
        assert result[0] == 1  # O ponto [1,1] deve ser o mais próximo de si mesmo


class TestKNNRegress:
    """Testes para a função principal de regressão k-NN."""
    
    def test_knn_regress_simple_case(self):
        """Testa caso simples de regressão k-NN."""
        X_train = np.array([[0], [1], [2], [3]])
        y_train = np.array([0, 1, 4, 9])  # y = x²
        x_query = np.array([1.5])
        k = 2
        
        result = knn_regress(X_train, y_train, x_query, k)
        expected = 2.5  # Média de y[1] e y[2]: (1 + 4) / 2 = 2.5
        
        assert np.isclose(result, expected)
    
    def test_knn_regress_k_equals_one(self):
        """Testa k=1 (deve retornar o valor do vizinho mais próximo)."""
        X_train = np.array([[0], [1], [2]])
        y_train = np.array([0, 1, 4])
        x_query = np.array([1.1])
        k = 1
        
        result = knn_regress(X_train, y_train, x_query, k)
        expected = 1.0  # O vizinho mais próximo é [1] com y=1
        
        assert np.isclose(result, expected)
    
    def test_knn_regress_k_equals_all_points(self):
        """Testa quando k = número total de pontos de treino."""
        X_train = np.array([[0], [1], [2]])
        y_train = np.array([0, 1, 4])
        x_query = np.array([1.5])
        k = 3
        
        result = knn_regress(X_train, y_train, x_query, k)
        expected = 5/3  # Média de todos os valores: (0 + 1 + 4) / 3
        
        assert np.isclose(result, expected)
    
    def test_knn_regress_multidimensional(self):
        """Testa regressão k-NN com dados multidimensionais."""
        X_train = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
        y_train = np.array([0, 1, 1, 2])
        x_query = np.array([0.5, 0.5])
        k = 2
        
        result = knn_regress(X_train, y_train, x_query, k)
        # Os dois vizinhos mais próximos são [0,0] e [1,0] ou [0,1]
        # A média deve estar entre 0.5 e 1.5
        
        assert 0.5 <= result <= 1.5
    
    def test_knn_regress_invalid_k(self):
        """Testa validação de k inválido."""
        X_train = np.array([[0], [1]])
        y_train = np.array([0, 1])
        x_query = np.array([0.5])
        
        # k <= 0
        with pytest.raises(ValueError, match="k deve ser positivo"):
            knn_regress(X_train, y_train, x_query, k=0)
        
        with pytest.raises(ValueError, match="k deve ser positivo"):
            knn_regress(X_train, y_train, x_query, k=-1)
        
        # k > n_samples
        with pytest.raises(ValueError, match="k não pode ser maior"):
            knn_regress(X_train, y_train, x_query, k=3)
    
    def test_knn_regress_dimension_mismatch(self):
        """Testa validação de incompatibilidade de dimensões."""
        X_train = np.array([[0], [1]])
        y_train = np.array([0, 1, 2])  # Mais amostras que X_train
        
        with pytest.raises(ValueError, match="mesmo número de amostras"):
            knn_regress(X_train, y_train, np.array([0.5]), k=1)


class TestKNNRegressBatch:
    """Testes para predição em lote."""
    
    def test_knn_regress_batch_simple(self):
        """Testa predição em lote simples."""
        X_train = np.array([[0], [1], [2]])
        y_train = np.array([0, 1, 4])
        X_query = np.array([[0.5], [1.5]])
        k = 2
        
        result = knn_regress_batch(X_train, y_train, X_query, k)
        
        assert len(result) == 2
        assert result.shape == (2,)
        
        # Para x=0.5, vizinhos são [0] e [1], média = (0+1)/2 = 0.5
        # Para x=1.5, vizinhos são [1] e [2], média = (1+4)/2 = 2.5
        assert np.isclose(result[0], 0.5)
        assert np.isclose(result[1], 2.5)
    
    def test_knn_regress_batch_single_query(self):
        """Testa predição em lote com apenas um ponto de consulta."""
        X_train = np.array([[0], [1], [2]])
        y_train = np.array([0, 1, 4])
        X_query = np.array([[1.5]])
        k = 2
        
        result = knn_regress_batch(X_train, y_train, X_query, k)
        
        assert len(result) == 1
        assert np.isclose(result[0], 2.5)  # Média de y[1] e y[2]


class TestKNNRegressor:
    """Testes para a classe KNNRegressor."""
    
    def test_knn_regressor_initialization(self):
        """Testa inicialização da classe."""
        k = 3
        regressor = KNNRegressor(k=k)
        
        assert regressor.k == k
        assert regressor.X_train is None
        assert regressor.y_train is None
    
    def test_knn_regressor_fit(self):
        """Testa método fit."""
        regressor = KNNRegressor(k=2)
        X = np.array([[0], [1], [2]])
        y = np.array([0, 1, 4])
        
        result = regressor.fit(X, y)
        
        assert result is regressor  # Deve retornar self
        assert regressor.X_train is not None
        assert regressor.y_train is not None
        np.testing.assert_array_equal(regressor.X_train, X)
        np.testing.assert_array_equal(regressor.y_train, y)
    
    def test_knn_regressor_predict(self):
        """Testa método predict."""
        regressor = KNNRegressor(k=2)
        X_train = np.array([[0], [1], [2]])
        y_train = np.array([0, 1, 4])
        X_query = np.array([[0.5], [1.5]])
        
        regressor.fit(X_train, y_train)
        result = regressor.predict(X_query)
        
        assert len(result) == 2
        assert result.shape == (2,)
        assert np.isclose(result[0], 0.5)  # Média de y[0] e y[1]
        assert np.isclose(result[1], 2.5)  # Média de y[1] e y[2]
    
    def test_knn_regressor_predict_single_point(self):
        """Testa predição de um único ponto."""
        regressor = KNNRegressor(k=1)
        X_train = np.array([[0], [1], [2]])
        y_train = np.array([0, 1, 4])
        X_query = np.array([[1.1]])
        
        regressor.fit(X_train, y_train)
        result = regressor.predict(X_query)
        
        assert len(result) == 1
        assert np.isclose(result[0], 1.0)  # Vizinho mais próximo é [1]


class TestKNNRegressionWithSyntheticData:
    """Testes com dados sintéticos para validar comportamento esperado."""
    
    def test_knn_regression_sine_function(self):
        """Testa k-NN com função seno sintética."""
        # Gera dados da função y = sin(x) + ruído
        np.random.seed(42)
        X_train = np.linspace(0, 2*np.pi, 100).reshape(-1, 1)
        y_train = np.sin(X_train.flatten()) + 0.1 * np.random.randn(100)
        
        # Pontos de consulta
        X_query = np.array([[np.pi/2], [np.pi], [3*np.pi/2]])
        
        # Testa diferentes valores de k
        for k in [1, 3, 5]:
            predictions = []
            for x_query in X_query:
                pred = knn_regress(X_train, y_train, x_query.flatten(), k)
                predictions.append(pred)
            
            predictions = np.array(predictions)
            
            # Valores esperados aproximados (seno nos pontos de consulta)
            expected = np.sin(X_query.flatten())
            
            # Verifica se as predições estão próximas dos valores esperados
            # (com tolerância para ruído)
            assert np.allclose(predictions, expected, atol=0.3)
    
    def test_knn_regression_smoothness_increase_with_k(self):
        """Testa se a suavidade aumenta com k."""
        # Dados sintéticos com ruído
        np.random.seed(42)
        X_train = np.linspace(0, 10, 50).reshape(-1, 1)
        y_train = X_train.flatten() + 0.5 * np.random.randn(50)
        
        # Pontos de consulta
        X_query = np.linspace(0, 10, 20).reshape(-1, 1)
        
        predictions_k1 = []
        predictions_k5 = []
        
        for x_query in X_query:
            pred1 = knn_regress(X_train, y_train, x_query.flatten(), k=1)
            pred5 = knn_regress(X_train, y_train, x_query.flatten(), k=5)
            predictions_k1.append(pred1)
            predictions_k5.append(pred5)
        
        predictions_k1 = np.array(predictions_k1)
        predictions_k5 = np.array(predictions_k5)
        
        # k=5 deve ser mais suave que k=1
        # Calcula a variância das predições como medida de suavidade
        variance_k1 = np.var(predictions_k1)
        variance_k5 = np.var(predictions_k5)
        
        # k=5 deve ter menor variância (mais suave)
        assert variance_k5 <= variance_k1


if __name__ == "__main__":
    pytest.main([__file__]) 