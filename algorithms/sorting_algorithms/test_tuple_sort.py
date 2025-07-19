"""
Testes para Tuple Sort
"""
import pytest
from .tuple_sort import (
    tuple_sort,
    counting_sort_by_column,
    tuple_sort_with_key_function,
    counting_sort_by_key_function,
    Employee,
    create_employee_tuple,
    get_employee_name,
    get_employee_department,
    get_employee_salary,
    get_employee_age
)


class TestTupleSort:
    
    def test_empty_list(self):
        """Testa ordenação de lista vazia"""
        result = tuple_sort([], [0])
        assert result == []
    
    def test_empty_priorities(self):
        """Testa lista vazia de prioridades"""
        result = tuple_sort([(1, 2), (3, 4)], [])
        assert result == [(1, 2), (3, 4)]
    
    def test_single_tuple(self):
        """Testa ordenação de lista com uma tupla"""
        result = tuple_sort([(5, 3)], [0])
        assert result == [(5, 3)]
    
    def test_single_column_sort(self):
        """Testa ordenação por uma coluna"""
        tuples = [(3, 2), (1, 4), (2, 1)]
        result = tuple_sort(tuples, [0])
        assert result == [(1, 4), (2, 1), (3, 2)]
    
    def test_two_column_sort(self):
        """Testa ordenação por duas colunas com prioridade"""
        tuples = [(3, 2), (1, 4), (3, 1), (2, 3)]
        # Prioridade: coluna 0 (primeira), depois coluna 1 (segunda)
        result = tuple_sort(tuples, [0, 1])
        assert result == [(1, 4), (2, 3), (3, 1), (3, 2)]
    
    def test_reverse_priority_order(self):
        """Testa ordem reversa de prioridades"""
        tuples = [(3, 2), (1, 4), (3, 1), (2, 3)]
        # Prioridade: coluna 1 (segunda), depois coluna 0 (primeira)
        result = tuple_sort(tuples, [1, 0])
        assert result == [(3, 1), (3, 2), (2, 3), (1, 4)]
    
    def test_three_column_sort(self):
        """Testa ordenação por três colunas"""
        tuples = [
            (1, 2, 3),
            (1, 2, 1),
            (1, 1, 3),
            (2, 1, 1),
            (1, 1, 1)
        ]
        # Prioridade: coluna 0, depois 1, depois 2
        result = tuple_sort(tuples, [0, 1, 2])
        expected = [
            (1, 1, 1),
            (1, 1, 3),
            (1, 2, 1),
            (1, 2, 3),
            (2, 1, 1)
        ]
        assert result == expected
    
    def test_stability(self):
        """Testa que a ordenação é estável"""
        tuples = [
            (3, 2, "first"),
            (1, 4, "second"),
            (3, 2, "third"),
            (2, 3, "fourth")
        ]
        result = tuple_sort(tuples, [0, 1])
        
        # Verificar que a ordem relativa dos (3, 2) foi mantida
        threes_with_two = [t for t in result if t[0] == 3 and t[1] == 2]
        assert threes_with_two[0][2] == "first"
        assert threes_with_two[1][2] == "third"
    
    def test_duplicate_values(self):
        """Testa valores duplicados"""
        tuples = [(3, 2), (3, 2), (1, 4), (1, 4)]
        result = tuple_sort(tuples, [0, 1])
        assert result == [(1, 4), (1, 4), (3, 2), (3, 2)]


class TestCountingSortByColumn:
    """Testes para ordenação por coluna específica"""
    
    def test_empty_list(self):
        """Testa lista vazia"""
        result = counting_sort_by_column([], 0)
        assert result == []
    
    def test_single_column(self):
        """Testa ordenação por coluna única"""
        tuples = [(3, 2), (1, 4), (2, 1)]
        result = counting_sort_by_column(tuples, 0)
        assert result == [(1, 4), (2, 1), (3, 2)]
    
    def test_second_column(self):
        """Testa ordenação pela segunda coluna"""
        tuples = [(3, 2), (1, 4), (2, 1)]
        result = counting_sort_by_column(tuples, 1)
        assert result == [(2, 1), (3, 2), (1, 4)]
    
    def test_third_column(self):
        """Testa ordenação pela terceira coluna"""
        tuples = [(1, 2, 3), (1, 2, 1), (1, 1, 3)]
        result = counting_sort_by_column(tuples, 2)
        assert result == [(1, 2, 1), (1, 2, 3), (1, 1, 3)]
    
    def test_stability_by_column(self):
        """Testa estabilidade na ordenação por coluna"""
        tuples = [
            (3, 2, "first"),
            (1, 4, "second"),
            (3, 2, "third"),
            (2, 3, "fourth")
        ]
        result = counting_sort_by_column(tuples, 0)
        
        # Verificar que a ordem relativa dos (3, 2, x) foi mantida
        threes = [t for t in result if t[0] == 3]
        assert threes[0][2] == "first"
        assert threes[1][2] == "third"


class TestTupleSortWithKeyFunction:
    """Testes para ordenação com funções de chave"""
    
    def test_empty_list(self):
        """Testa lista vazia"""
        result = tuple_sort_with_key_function([], [])
        assert result == []
    
    def test_single_key_function(self):
        """Testa ordenação com uma função de chave"""
        employees = [
            Employee("Alice", "IT", 50000, 25),
            Employee("Bob", "HR", 60000, 30),
            Employee("Charlie", "IT", 45000, 28)
        ]
        result = tuple_sort_with_key_function(employees, [get_employee_salary])
        assert result == [
            Employee("Charlie", "IT", 45000, 28),
            Employee("Alice", "IT", 50000, 25),
            Employee("Bob", "HR", 60000, 30)
        ]
    
    def test_multiple_key_functions(self):
        """Testa ordenação com múltiplas funções de chave"""
        employees = [
            Employee("Alice", "IT", 50000, 25),
            Employee("Bob", "HR", 50000, 30),
            Employee("Charlie", "IT", 50000, 28),
            Employee("David", "IT", 60000, 25)
        ]
        # Prioridade: departamento, depois salário, depois idade
        result = tuple_sort_with_key_function(
            employees, 
            [get_employee_department, get_employee_salary, get_employee_age]
        )
        assert result == [
            Employee("Bob", "HR", 50000, 30),
            Employee("Alice", "IT", 50000, 25),
            Employee("Charlie", "IT", 50000, 28),
            Employee("David", "IT", 60000, 25)
        ]
    
    def test_stability_with_key_functions(self):
        """Testa estabilidade com funções de chave"""
        employees = [
            Employee("Alice", "IT", 50000, 25),
            Employee("Bob", "IT", 50000, 30),
            Employee("Charlie", "IT", 50000, 28)
        ]
        result = tuple_sort_with_key_function(employees, [get_employee_salary])
        
        # Verificar que a ordem relativa foi mantida
        assert result[0].name == "Alice"
        assert result[1].name == "Bob"
        assert result[2].name == "Charlie"


class TestCountingSortByKeyFunction:
    """Testes para ordenação por função de chave"""
    
    def test_empty_list(self):
        """Testa lista vazia"""
        result = counting_sort_by_key_function([], get_employee_salary)
        assert result == []
    
    def test_single_employee(self):
        """Testa um funcionário"""
        employees = [Employee("Alice", "IT", 50000, 25)]
        result = counting_sort_by_key_function(employees, get_employee_salary)
        assert result == employees
    
    def test_multiple_employees_by_salary(self):
        """Testa múltiplos funcionários por salário"""
        employees = [
            Employee("Alice", "IT", 50000, 25),
            Employee("Bob", "HR", 60000, 30),
            Employee("Charlie", "IT", 45000, 28)
        ]
        result = counting_sort_by_key_function(employees, get_employee_salary)
        assert result == [
            Employee("Charlie", "IT", 45000, 28),
            Employee("Alice", "IT", 50000, 25),
            Employee("Bob", "HR", 60000, 30)
        ]
    
    def test_by_age(self):
        """Testa ordenação por idade"""
        employees = [
            Employee("Alice", "IT", 50000, 25),
            Employee("Bob", "HR", 60000, 30),
            Employee("Charlie", "IT", 45000, 28)
        ]
        result = counting_sort_by_key_function(employees, get_employee_age)
        assert result == [
            Employee("Alice", "IT", 50000, 25),
            Employee("Charlie", "IT", 45000, 28),
            Employee("Bob", "HR", 60000, 30)
        ]
    
    def test_stability_by_key_function(self):
        """Testa estabilidade por função de chave"""
        employees = [
            Employee("Alice", "IT", 50000, 25),
            Employee("Bob", "HR", 50000, 30),
            Employee("Charlie", "IT", 50000, 28)
        ]
        result = counting_sort_by_key_function(employees, get_employee_salary)
        
        # Verificar que a ordem relativa foi mantida
        assert result[0].name == "Alice"
        assert result[1].name == "Bob"
        assert result[2].name == "Charlie"


class TestEmployeeClass:
    """Testes para a classe Employee"""
    
    def test_employee_creation(self):
        """Testa criação de Employee"""
        employee = Employee("Alice", "IT", 50000, 25)
        assert employee.name == "Alice"
        assert employee.department == "IT"
        assert employee.salary == 50000
        assert employee.age == 25
    
    def test_employee_equality(self):
        """Testa igualdade entre Employees"""
        emp1 = Employee("Alice", "IT", 50000, 25)
        emp2 = Employee("Alice", "IT", 50000, 25)
        emp3 = Employee("Alice", "IT", 60000, 25)
        emp4 = Employee("Bob", "IT", 50000, 25)
        
        assert emp1 == emp2
        assert emp1 != emp3
        assert emp1 != emp4
        assert emp1 != "not_an_employee"
    
    def test_employee_repr(self):
        """Testa representação string do Employee"""
        employee = Employee("Alice", "IT", 50000, 25)
        assert repr(employee) == "Employee(Alice, IT, 50000, 25)"


class TestHelperFunctions:
    """Testes para funções auxiliares"""
    
    def test_create_employee_tuple(self):
        """Testa conversão de Employee para tupla"""
        employee = Employee("Alice", "IT", 50000, 25)
        tuple_ = create_employee_tuple(employee)
        assert tuple_ == ("Alice", "IT", 50000, 25)
    
    def test_get_employee_name(self):
        """Testa extração de nome"""
        employee = Employee("Alice", "IT", 50000, 25)
        assert get_employee_name(employee) == "Alice"
    
    def test_get_employee_department(self):
        """Testa extração de departamento"""
        employee = Employee("Alice", "IT", 50000, 25)
        assert get_employee_department(employee) == "IT"
    
    def test_get_employee_salary(self):
        """Testa extração de salário"""
        employee = Employee("Alice", "IT", 50000, 25)
        assert get_employee_salary(employee) == 50000
    
    def test_get_employee_age(self):
        """Testa extração de idade"""
        employee = Employee("Alice", "IT", 50000, 25)
        assert get_employee_age(employee) == 25


class TestEdgeCases:
    """Testes para casos extremos"""
    
    def test_large_numbers(self):
        """Testa números grandes"""
        tuples = [(1000, 100), (100, 10), (10, 1), (1, 1000)]
        result = tuple_sort(tuples, [0, 1])
        assert result == [(1, 1000), (10, 1), (100, 10), (1000, 100)]
    
    def test_zero_values(self):
        """Testa valores zero"""
        tuples = [(5, 0), (0, 3), (1, 0), (0, 1)]
        result = tuple_sort(tuples, [0, 1])
        assert result == [(0, 1), (0, 3), (1, 0), (5, 0)]
    
    def test_negative_values(self):
        """Testa valores negativos"""
        tuples = [(-1, 2), (3, -4), (-5, -6), (7, 8)]
        result = tuple_sort(tuples, [0, 1])
        assert result == [(-5, -6), (-1, 2), (3, -4), (7, 8)]
    
    def test_many_columns(self):
        """Testa muitas colunas"""
        tuples = [
            (1, 2, 3, 4, 5),
            (1, 2, 3, 4, 4),
            (1, 2, 3, 3, 5),
            (1, 1, 3, 4, 5)
        ]
        result = tuple_sort(tuples, [0, 1, 2, 3, 4])
        expected = [
            (1, 1, 3, 4, 5),
            (1, 2, 3, 3, 5),
            (1, 2, 3, 4, 4),
            (1, 2, 3, 4, 5)
        ]
        assert result == expected


class TestPerformance:
    """Testes de performance"""
    
    def test_large_dataset_performance(self):
        """Testa performance com dataset grande"""
        import time
        
        # Criar dataset grande
        employees = []
        for i in range(1000):
            employees.append(Employee(f"Emp{i}", "Dept{i%10}", 30000 + i, 20 + i%50))
        
        start_time = time.time()
        result = tuple_sort_with_key_function(
            employees, 
            [get_employee_department, get_employee_salary, get_employee_age]
        )
        end_time = time.time()
        
        # Verificar que está ordenado
        assert len(result) == 1000
        
        # Verificar que não demorou muito
        assert end_time - start_time < 2.0  # menos de 2 segundos 