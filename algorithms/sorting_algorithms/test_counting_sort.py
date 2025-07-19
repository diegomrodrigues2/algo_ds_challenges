"""
Testes para Counting Sort
"""
import pytest
from .counting_sort import counting_sort, counting_sort_simple, counting_sort_objects, Student


class TestCountingSort:
    
    def test_empty_list(self):
        """Testa ordenação de lista vazia"""
        result = counting_sort([])
        assert result == []
    
    def test_single_item(self):
        """Testa ordenação de lista com um item"""
        result = counting_sort([5])
        assert result == [5]
    
    def test_sorted_list(self):
        """Testa lista já ordenada"""
        result = counting_sort([1, 2, 3, 4, 5])
        assert result == [1, 2, 3, 4, 5]
    
    def test_reverse_sorted_list(self):
        """Testa lista ordenada em ordem reversa"""
        result = counting_sort([5, 4, 3, 2, 1])
        assert result == [1, 2, 3, 4, 5]
    
    def test_random_order(self):
        """Testa lista em ordem aleatória"""
        result = counting_sort([3, 1, 4, 1, 5, 9, 2, 6])
        assert result == [1, 1, 2, 3, 4, 5, 6, 9]
    
    def test_duplicate_values(self):
        """Testa valores duplicados (deve manter ordem relativa)"""
        result = counting_sort([3, 1, 3, 2, 1, 3])
        assert result == [1, 1, 2, 3, 3, 3]
    
    def test_all_same_values(self):
        """Testa lista com todos os valores iguais"""
        result = counting_sort([5, 5, 5, 5, 5])
        assert result == [5, 5, 5, 5, 5]
    
    def test_zero_values(self):
        """Testa valores zero"""
        result = counting_sort([5, 0, 3, 1, 0])
        assert result == [0, 0, 1, 3, 5]
    
    def test_consecutive_values(self):
        """Testa valores consecutivos"""
        result = counting_sort([10, 11, 12, 13, 14])
        assert result == [10, 11, 12, 13, 14]
    
    def test_sparse_values(self):
        """Testa valores esparsos"""
        result = counting_sort([1, 10, 100, 1000])
        assert result == [1, 10, 100, 1000]
    
    def test_with_range_parameters(self):
        """Testa com parâmetros de faixa específicos"""
        result = counting_sort([5, 2, 8, 1, 9], min_val=0, max_val=10)
        assert result == [1, 2, 5, 8, 9]
    
    def test_negative_values_should_fail(self):
        """Testa que valores negativos causam erro"""
        with pytest.raises((IndexError, ValueError)):
            counting_sort([-1, 2, 3])
    
    def test_stability(self):
        """Testa que a ordenação é estável"""
        # Criar objetos com valores iguais mas ordem diferente
        class TestObj:
            def __init__(self, val, original_pos):
                self.val = val
                self.original_pos = original_pos
            
            def __eq__(self, other):
                return self.val == other.val and self.original_pos == other.original_pos
        
        items = [
            TestObj(3, 0),  # primeiro 3
            TestObj(1, 1),  # primeiro 1
            TestObj(3, 2),  # segundo 3
            TestObj(2, 3),  # primeiro 2
            TestObj(3, 4),  # terceiro 3
        ]
        
        result = counting_sort_objects(items, lambda x: x.val)
        
        # Verificar que a ordem relativa dos 3s foi mantida
        threes = [item for item in result if item.val == 3]
        assert threes[0].original_pos == 0  # primeiro 3
        assert threes[1].original_pos == 2  # segundo 3
        assert threes[2].original_pos == 4  # terceiro 3


class TestCountingSortSimple:
    """Testes para a versão simplificada"""
    
    def test_empty_list(self):
        """Testa lista vazia"""
        result = counting_sort_simple([])
        assert result == []
    
    def test_single_item(self):
        """Testa um item"""
        result = counting_sort_simple([5])
        assert result == [5]
    
    def test_multiple_items(self):
        """Testa múltiplos itens"""
        result = counting_sort_simple([3, 1, 4, 1, 5])
        assert result == [1, 1, 3, 4, 5]
    
    def test_duplicates(self):
        """Testa duplicatas"""
        result = counting_sort_simple([2, 2, 2, 1, 1])
        assert result == [1, 1, 2, 2, 2]
    
    def test_zero_included(self):
        """Testa incluindo zero"""
        result = counting_sort_simple([5, 0, 3, 1])
        assert result == [0, 1, 3, 5]


class TestCountingSortObjects:
    """Testes para ordenação de objetos"""
    
    def test_empty_list(self):
        """Testa lista vazia de objetos"""
        result = counting_sort_objects([], lambda x: x.grade)
        assert result == []
    
    def test_single_student(self):
        """Testa um estudante"""
        students = [Student("Alice", 85)]
        result = counting_sort_objects(students, lambda x: x.grade)
        assert result == students
    
    def test_multiple_students(self):
        """Testa múltiplos estudantes"""
        students = [
            Student("Alice", 85),
            Student("Bob", 92),
            Student("Charlie", 78),
            Student("David", 85),
            Student("Eve", 90)
        ]
        result = counting_sort_objects(students, lambda x: x.grade)
        
        # Verificar que estão ordenados por nota
        grades = [s.grade for s in result]
        assert grades == [78, 85, 85, 90, 92]
    
    def test_stability_with_objects(self):
        """Testa estabilidade com objetos"""
        students = [
            Student("Alice", 85),   # primeira nota 85
            Student("Bob", 92),
            Student("Charlie", 85), # segunda nota 85
            Student("David", 78)
        ]
        result = counting_sort_objects(students, lambda x: x.grade)
        
        # Verificar que Alice vem antes de Charlie (mesma nota, ordem original)
        alice_index = next(i for i, s in enumerate(result) if s.name == "Alice")
        charlie_index = next(i for i, s in enumerate(result) if s.name == "Charlie")
        assert alice_index < charlie_index
    
    def test_different_key_function(self):
        """Testa função de chave diferente"""
        students = [
            Student("Alice", 85),
            Student("Bob", 92),
            Student("Charlie", 78)
        ]
        # Ordenar pelo comprimento do nome
        result = counting_sort_objects(students, lambda x: len(x.name))
        
        # Alice(5) < Bob(3) < Charlie(7)
        names = [s.name for s in result]
        assert names == ["Bob", "Alice", "Charlie"]


class TestStudentClass:
    """Testes para a classe Student"""
    
    def test_student_creation(self):
        """Testa criação de Student"""
        student = Student("Alice", 85)
        assert student.name == "Alice"
        assert student.grade == 85
    
    def test_student_equality(self):
        """Testa igualdade entre Students"""
        student1 = Student("Alice", 85)
        student2 = Student("Alice", 85)
        student3 = Student("Alice", 90)
        student4 = Student("Bob", 85)
        
        assert student1 == student2
        assert student1 != student3
        assert student1 != student4
        assert student1 != "not_a_student"
    
    def test_student_repr(self):
        """Testa representação string do Student"""
        student = Student("Alice", 85)
        assert repr(student) == "Student(Alice, 85)"


class TestEdgeCases:
    """Testes para casos extremos"""
    
    def test_large_range(self):
        """Testa faixa grande de valores"""
        result = counting_sort([0, 100, 50, 25, 75])
        assert result == [0, 25, 50, 75, 100]
    
    def test_single_value_repeated(self):
        """Testa valor único repetido muitas vezes"""
        result = counting_sort([5] * 100)
        assert result == [5] * 100
    
    def test_maximum_value(self):
        """Testa valor máximo"""
        result = counting_sort([100, 50, 100, 25])
        assert result == [25, 50, 100, 100]
    
    def test_minimum_value(self):
        """Testa valor mínimo (zero)"""
        result = counting_sort([0, 5, 0, 3])
        assert result == [0, 0, 3, 5] 