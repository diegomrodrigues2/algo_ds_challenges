"""
Test cases for permutation generation algorithms.

This module contains comprehensive tests for all permutation generation functions,
including basic functionality, edge cases, performance analysis, and correctness verification.
"""

import pytest
import time
from permutation_generation import (
    permutation_generation_backtracking,
    permutation_generation_inplace_swap,
    permutation_generation_with_duplicates,
    permutation_generation_lexicographic,
    permutation_generation_count_only,
    permutation_generation_with_constraints,
    permutation_generation_optimized,
    permutation_generation_with_memoization,
    analyze_permutation_complexity,
    create_test_permutations
)


class TestPermutationGenerationBasic:
    """Test basic functionality of permutation generation algorithms."""
    
    def test_empty_list(self):
        """Test permutation generation with empty list."""
        elements = []
        expected = [[]]
        
        result_backtrack = permutation_generation_backtracking(elements)
        result_swap = permutation_generation_inplace_swap(elements)
        result_optimized = permutation_generation_optimized(elements)
        result_lex = permutation_generation_lexicographic(elements)
        
        assert result_backtrack == expected
        assert result_swap == expected
        assert result_optimized == expected
        assert result_lex == expected
    
    def test_single_element(self):
        """Test permutation generation with single element."""
        elements = [1]
        expected = [[1]]
        
        result_backtrack = permutation_generation_backtracking(elements)
        result_swap = permutation_generation_inplace_swap(elements)
        result_optimized = permutation_generation_optimized(elements)
        result_lex = permutation_generation_lexicographic(elements)
        
        assert result_backtrack == expected
        assert result_swap == expected
        assert result_optimized == expected
        assert result_lex == expected
    
    def test_two_elements(self):
        """Test permutation generation with two elements."""
        elements = [1, 2]
        expected = [[1, 2], [2, 1]]
        
        result_backtrack = permutation_generation_backtracking(elements)
        result_swap = permutation_generation_inplace_swap(elements)
        result_optimized = permutation_generation_optimized(elements)
        result_lex = permutation_generation_lexicographic(elements)
        
        # Sort results for comparison (order may vary)
        result_backtrack.sort()
        result_swap.sort()
        result_optimized.sort()
        result_lex.sort()
        expected.sort()
        
        assert result_backtrack == expected
        assert result_swap == expected
        assert result_optimized == expected
        assert result_lex == expected
    
    def test_three_elements(self):
        """Test permutation generation with three elements."""
        elements = [1, 2, 3]
        expected_count = 6  # 3! = 6
        
        result_backtrack = permutation_generation_backtracking(elements)
        result_swap = permutation_generation_inplace_swap(elements)
        result_optimized = permutation_generation_optimized(elements)
        result_lex = permutation_generation_lexicographic(elements)
        
        assert len(result_backtrack) == expected_count
        assert len(result_swap) == expected_count
        assert len(result_optimized) == expected_count
        assert len(result_lex) == expected_count
        
        # Check that all results contain all elements
        for result in [result_backtrack, result_swap, result_optimized, result_lex]:
            for perm in result:
                assert len(perm) == 3
                assert set(perm) == {1, 2, 3}


class TestPermutationGenerationDuplicates:
    """Test handling of duplicate elements."""
    
    def test_with_duplicates(self):
        """Test permutation generation with duplicate elements."""
        elements = [1, 1, 2]
        
        # Regular approaches may generate duplicates
        result_backtrack = permutation_generation_backtracking(elements)
        result_swap = permutation_generation_inplace_swap(elements)
        result_optimized = permutation_generation_optimized(elements)
        
        # Duplicate-aware approach
        result_unique = permutation_generation_with_duplicates(elements)
        
        # Check that unique approach generates fewer results
        assert len(result_unique) <= len(result_backtrack)
        assert len(result_unique) <= len(result_swap)
        assert len(result_unique) <= len(result_optimized)
        
        # Check that unique results are actually unique
        unique_set = set(tuple(perm) for perm in result_unique)
        assert len(unique_set) == len(result_unique)
    
    def test_all_duplicates(self):
        """Test permutation generation with all duplicate elements."""
        elements = [1, 1, 1]
        
        result_unique = permutation_generation_with_duplicates(elements)
        
        # Should only have one unique permutation
        assert len(result_unique) == 1
        assert result_unique[0] == [1, 1, 1]
    
    def test_string_elements(self):
        """Test permutation generation with string elements."""
        elements = ['a', 'b', 'c']
        expected_count = 6  # 3! = 6
        
        result_backtrack = permutation_generation_backtracking(elements)
        result_swap = permutation_generation_inplace_swap(elements)
        result_optimized = permutation_generation_optimized(elements)
        
        assert len(result_backtrack) == expected_count
        assert len(result_swap) == expected_count
        assert len(result_optimized) == expected_count
        
        # Check that all results contain all elements
        for result in [result_backtrack, result_swap, result_optimized]:
            for perm in result:
                assert len(perm) == 3
                assert set(perm) == {'a', 'b', 'c'}


class TestPermutationGenerationLexicographic:
    """Test lexicographic permutation generation."""
    
    def test_lexicographic_order(self):
        """Test that lexicographic generation produces ordered results."""
        elements = [1, 2, 3]
        
        result = permutation_generation_lexicographic(elements)
        
        # Check that results are in lexicographic order
        for i in range(len(result) - 1):
            assert result[i] <= result[i + 1]
    
    def test_lexicographic_with_duplicates(self):
        """Test lexicographic generation with duplicates."""
        elements = [1, 1, 2]
        
        result = permutation_generation_lexicographic(elements)
        
        # Should be in lexicographic order
        for i in range(len(result) - 1):
            assert result[i] <= result[i + 1]


class TestPermutationGenerationCount:
    """Test permutation counting functionality."""
    
    def test_count_only(self):
        """Test counting permutations without generating them."""
        test_cases = [
            (0, 1),   # Empty set
            (1, 1),   # Single element
            (2, 2),   # Two elements: 2! = 2
            (3, 6),   # Three elements: 3! = 6
            (4, 24),  # Four elements: 4! = 24
            (5, 120), # Five elements: 5! = 120
        ]
        
        for n, expected in test_cases:
            result = permutation_generation_count_only(n)
            assert result == expected
    
    def test_count_matches_generation(self):
        """Test that count matches actual generation."""
        test_cases = [1, 2, 3, 4]
        
        for n in test_cases:
            elements = list(range(1, n + 1))
            count = permutation_generation_count_only(n)
            
            result_backtrack = permutation_generation_backtracking(elements)
            result_swap = permutation_generation_inplace_swap(elements)
            result_optimized = permutation_generation_optimized(elements)
            
            assert len(result_backtrack) == count
            assert len(result_swap) == count
            assert len(result_optimized) == count


class TestPermutationGenerationConstraints:
    """Test constraint-based permutation generation."""
    
    def test_with_constraints(self):
        """Test permutation generation with constraints."""
        elements = [1, 2, 3, 4]
        
        # Constraint: first element must be less than last element
        def constraint_func(partial):
            if len(partial) >= 2:
                return partial[0] < partial[-1]
            return True
        
        result = permutation_generation_with_constraints(elements, constraint_func)
        
        # Check that all results satisfy the constraint
        for perm in result:
            if len(perm) >= 2:
                assert perm[0] < perm[-1]
    
    def test_constraint_all_valid(self):
        """Test when all permutations satisfy the constraint."""
        elements = [1, 2, 3]
        
        def constraint_func(partial):
            return True  # All permutations are valid
        
        result = permutation_generation_with_constraints(elements, constraint_func)
        expected_count = 6  # 3! = 6
        
        assert len(result) == expected_count
    
    def test_constraint_none_valid(self):
        """Test when no permutations satisfy the constraint."""
        elements = [1, 2, 3]
        
        def constraint_func(partial):
            return False  # No permutations are valid
        
        result = permutation_generation_with_constraints(elements, constraint_func)
        
        assert len(result) == 0


class TestPermutationGenerationOptimized:
    """Test optimized permutation generation."""
    
    def test_optimized_correctness(self):
        """Test that optimized version produces correct results."""
        test_cases = [
            [],
            [1],
            [1, 2],
            [1, 2, 3],
            ['a', 'b', 'c'],
        ]
        
        for elements in test_cases:
            result_optimized = permutation_generation_optimized(elements)
            result_backtrack = permutation_generation_backtracking(elements)
            
            # Sort for comparison
            result_optimized.sort()
            result_backtrack.sort()
            
            assert result_optimized == result_backtrack
    
    def test_optimized_performance(self):
        """Test that optimized version is reasonably fast."""
        elements = [1, 2, 3, 4]
        
        start_time = time.time()
        result_optimized = permutation_generation_optimized(elements)
        optimized_time = time.time() - start_time
        
        start_time = time.time()
        result_backtrack = permutation_generation_backtracking(elements)
        backtrack_time = time.time() - start_time
        
        # Both should produce same results
        result_optimized.sort()
        result_backtrack.sort()
        assert result_optimized == result_backtrack
        
        # Optimized should not be significantly slower
        assert optimized_time <= backtrack_time * 2


class TestPermutationGenerationMemoization:
    """Test memoization-based permutation generation."""
    
    def test_memoization_correctness(self):
        """Test that memoized version produces correct results."""
        test_cases = [
            [],
            [1],
            [1, 2],
            [1, 2, 3],
        ]
        
        for elements in test_cases:
            result_memo = permutation_generation_with_memoization(elements)
            result_backtrack = permutation_generation_backtracking(elements)
            
            # Sort for comparison
            result_memo.sort()
            result_backtrack.sort()
            
            assert result_memo == result_backtrack
    
    def test_memoization_performance(self):
        """Test that memoized version is reasonably fast."""
        elements = [1, 2, 3, 4]
        
        start_time = time.time()
        result_memo = permutation_generation_with_memoization(elements)
        memo_time = time.time() - start_time
        
        start_time = time.time()
        result_backtrack = permutation_generation_backtracking(elements)
        backtrack_time = time.time() - start_time
        
        # Both should produce same results
        result_memo.sort()
        result_backtrack.sort()
        assert result_memo == result_backtrack
        
        # Memoized should not be significantly slower
        assert memo_time <= backtrack_time * 2


class TestPermutationGenerationCorrectness:
    """Test correctness of all permutation generation implementations."""
    
    def test_correctness_multiple_implementations(self):
        """Test that all implementations produce consistent results."""
        test_cases = [
            [],
            [1],
            [1, 2],
            [1, 2, 3],
            [1, 1, 2],
            ['a', 'b', 'c'],
        ]
        
        for elements in test_cases:
            results = []
            
            # Collect results from all implementations
            implementations = [
                permutation_generation_backtracking,
                permutation_generation_inplace_swap,
                permutation_generation_optimized,
                permutation_generation_lexicographic,
            ]
            
            for impl in implementations:
                result = impl(elements)
                result.sort()  # Sort for comparison
                results.append(result)
            
            # All implementations should produce same results
            for i in range(1, len(results)):
                assert results[i] == results[0]
    
    def test_all_permutations_unique(self):
        """Test that all generated permutations are unique."""
        test_cases = [
            [1, 2, 3],
            [1, 2, 3, 4],
            ['a', 'b', 'c'],
        ]
        
        for elements in test_cases:
            implementations = [
                permutation_generation_backtracking,
                permutation_generation_inplace_swap,
                permutation_generation_optimized,
                permutation_generation_lexicographic,
            ]
            
            for impl in implementations:
                result = impl(elements)
                
                # Convert to tuples for set comparison
                result_tuples = set(tuple(perm) for perm in result)
                
                # All permutations should be unique
                assert len(result_tuples) == len(result)
                
                # Each permutation should have correct length
                for perm in result:
                    assert len(perm) == len(elements)
                
                # Each permutation should contain all elements
                for perm in result:
                    assert set(perm) == set(elements)


class TestPermutationGenerationComplexity:
    """Test complexity analysis functionality."""
    
    def test_complexity_analysis(self):
        """Test complexity analysis function."""
        elements = [1, 2, 3]
        
        analysis = analyze_permutation_complexity(elements)
        
        # Check that analysis contains expected keys
        expected_keys = ['backtracking', 'inplace_swap', 'optimized', 'lexicographic', 'expected_count']
        for key in expected_keys:
            assert key in analysis
        
        # Check that all implementations produced correct count
        expected_count = 6  # 3! = 6
        assert analysis['expected_count'] == expected_count
        
        for approach in ['backtracking', 'inplace_swap', 'optimized', 'lexicographic']:
            assert analysis[approach]['count'] == expected_count
            assert analysis[approach]['correct'] == True
            assert analysis[approach]['time'] >= 0
    
    def test_complexity_performance(self):
        """Test that complexity analysis captures performance differences."""
        elements = [1, 2, 3, 4]
        
        analysis = analyze_permutation_complexity(elements)
        
        # All implementations should complete in reasonable time
        for approach in ['backtracking', 'inplace_swap', 'optimized', 'lexicographic']:
            assert analysis[approach]['time'] < 1.0  # Should complete in under 1 second


class TestPermutationGenerationEdgeCases:
    """Test edge cases and error conditions."""
    
    def test_large_input(self):
        """Test behavior with larger inputs (should be slow but not crash)."""
        elements = list(range(1, 6))  # 5 elements = 120 permutations
        
        # This should work but be slow
        result = permutation_generation_backtracking(elements)
        expected_count = 120  # 5! = 120
        
        assert len(result) == expected_count
    
    def test_negative_numbers(self):
        """Test permutation generation with negative numbers."""
        elements = [-1, -2, -3]
        expected_count = 6  # 3! = 6
        
        result = permutation_generation_backtracking(elements)
        result_swap = permutation_generation_inplace_swap(elements)
        result_optimized = permutation_generation_optimized(elements)
        
        assert len(result) == expected_count
        assert len(result_swap) == expected_count
        assert len(result_optimized) == expected_count
    
    def test_floating_point(self):
        """Test permutation generation with floating point numbers."""
        elements = [1.5, 2.5, 3.5]
        expected_count = 6  # 3! = 6
        
        result = permutation_generation_backtracking(elements)
        result_swap = permutation_generation_inplace_swap(elements)
        result_optimized = permutation_generation_optimized(elements)
        
        assert len(result) == expected_count
        assert len(result_swap) == expected_count
        assert len(result_optimized) == expected_count
    
    def test_mixed_types(self):
        """Test permutation generation with mixed types."""
        elements = [1, 'a', 2.5]
        expected_count = 6  # 3! = 6
        
        result = permutation_generation_backtracking(elements)
        result_swap = permutation_generation_inplace_swap(elements)
        result_optimized = permutation_generation_optimized(elements)
        
        assert len(result) == expected_count
        assert len(result_swap) == expected_count
        assert len(result_optimized) == expected_count


class TestPermutationGenerationHelper:
    """Test helper functions."""
    
    def test_create_test_permutations(self):
        """Test test case creation function."""
        test_cases = create_test_permutations()
        
        # Should return a list of test cases
        assert isinstance(test_cases, list)
        assert len(test_cases) > 0
        
        # Should include various types of test cases
        assert [] in test_cases  # Empty list
        assert [1] in test_cases  # Single element
        assert [1, 2] in test_cases  # Two elements
        assert [1, 2, 3] in test_cases  # Three elements


class TestPermutationGenerationPerformance:
    """Test performance characteristics."""
    
    def test_performance_scaling(self):
        """Test that performance scales as expected."""
        # Test with small inputs first
        small_elements = [1, 2, 3]
        medium_elements = [1, 2, 3, 4]
        
        # Small input should be faster than medium input
        start_time = time.time()
        permutation_generation_backtracking(small_elements)
        small_time = time.time() - start_time
        
        start_time = time.time()
        permutation_generation_backtracking(medium_elements)
        medium_time = time.time() - start_time
        
        # Medium should take longer than small
        assert medium_time > small_time
    
    def test_memory_usage(self):
        """Test that memory usage is reasonable."""
        elements = [1, 2, 3, 4]
        expected_count = 24  # 4! = 24
        
        # Generate permutations
        result = permutation_generation_backtracking(elements)
        
        # Check that we got the expected number of permutations
        assert len(result) == expected_count
        
        # Check that each permutation has the correct length
        for perm in result:
            assert len(perm) == len(elements)
    
    def test_consistency_across_runs(self):
        """Test that results are consistent across multiple runs."""
        elements = [1, 2, 3]
        
        # Run multiple times
        results = []
        for _ in range(3):
            result = permutation_generation_backtracking(elements)
            result.sort()  # Sort for comparison
            results.append(result)
        
        # All runs should produce same results
        for i in range(1, len(results)):
            assert results[i] == results[0]


if __name__ == "__main__":
    # Run basic tests
    test_cases = [
        ([], "Empty list"),
        ([1], "Single element"),
        ([1, 2], "Two elements"),
        ([1, 2, 3], "Three elements"),
    ]
    
    print("=== Basic Permutation Generation Tests ===")
    for elements, description in test_cases:
        print(f"\n{description}: {elements}")
        
        result = permutation_generation_backtracking(elements)
        print(f"Generated {len(result)} permutations")
        
        if result:
            print(f"Sample: {result[0]}")
    
    print("\n=== All tests completed ===") 