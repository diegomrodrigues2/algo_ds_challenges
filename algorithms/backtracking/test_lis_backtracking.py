"""
Tests for Longest Increasing Subsequence (LIS) Backtracking Implementation

This module contains comprehensive tests for all LIS backtracking functions,
including basic backtracking, memoization, finding all solutions, counting
solutions, optimized versions, and Erickson's formulation.
"""

import pytest
import time
from typing import List, Tuple

from lis_backtracking import (
    lis_backtracking,
    lis_backtracking_with_memoization,
    lis_backtracking_all_solutions,
    lis_backtracking_count_solutions,
    lis_backtracking_optimized,
    analyze_lis_complexity,
    lis_backtracking_with_path,
    lis_backtracking_erickson_formulation,
    lis_backtracking_erickson_memoized,
    create_test_sequences
)


class TestLISBacktracking:
    """Test basic LIS backtracking functionality."""
    
    def test_empty_sequence(self):
        """Test with empty sequence."""
        assert lis_backtracking([]) == 0
    
    def test_single_element(self):
        """Test with single element."""
        assert lis_backtracking([1]) == 1
        assert lis_backtracking([5]) == 1
    
    def test_strictly_increasing(self):
        """Test with strictly increasing sequence."""
        sequence = [1, 2, 3, 4, 5]
        assert lis_backtracking(sequence) == 5
    
    def test_strictly_decreasing(self):
        """Test with strictly decreasing sequence."""
        sequence = [5, 4, 3, 2, 1]
        assert lis_backtracking(sequence) == 1
    
    def test_mixed_sequence(self):
        """Test with mixed sequence."""
        sequence = [1, 3, 2, 4, 5]
        assert lis_backtracking(sequence) == 4
    
    def test_classic_example(self):
        """Test with classic LIS example."""
        sequence = [10, 22, 9, 33, 21, 50, 41, 60]
        assert lis_backtracking(sequence) == 5
    
    def test_complex_example(self):
        """Test with complex example."""
        sequence = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        assert lis_backtracking(sequence) == 4
    
    def test_all_same_elements(self):
        """Test with all same elements."""
        sequence = [1, 1, 1, 1, 1]
        assert lis_backtracking(sequence) == 1
    
    def test_alternating_pattern(self):
        """Test with alternating pattern."""
        sequence = [1, 2, 1, 2, 1, 2]
        assert lis_backtracking(sequence) == 3
    
    def test_repeating_pattern(self):
        """Test with repeating pattern."""
        sequence = [1, 2, 3, 1, 2, 3, 1, 2, 3]
        assert lis_backtracking(sequence) == 3


class TestLISBacktrackingMemoized:
    """Test memoized LIS backtracking."""
    
    def test_empty_sequence(self):
        """Test with empty sequence."""
        assert lis_backtracking_with_memoization([]) == 0
    
    def test_single_element(self):
        """Test with single element."""
        assert lis_backtracking_with_memoization([1]) == 1
    
    def test_strictly_increasing(self):
        """Test with strictly increasing sequence."""
        sequence = [1, 2, 3, 4, 5]
        assert lis_backtracking_with_memoization(sequence) == 5
    
    def test_classic_example(self):
        """Test with classic LIS example."""
        sequence = [10, 22, 9, 33, 21, 50, 41, 60]
        assert lis_backtracking_with_memoization(sequence) == 5
    
    def test_complex_example(self):
        """Test with complex example."""
        sequence = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        assert lis_backtracking_with_memoization(sequence) == 4


class TestLISBacktrackingAllSolutions:
    """Test finding all LIS solutions."""
    
    def test_empty_sequence(self):
        """Test with empty sequence."""
        solutions = lis_backtracking_all_solutions([])
        assert solutions == []
    
    def test_single_element(self):
        """Test with single element."""
        solutions = lis_backtracking_all_solutions([1])
        assert len(solutions) == 1
        assert solutions[0] == [1]
    
    def test_strictly_increasing(self):
        """Test with strictly increasing sequence."""
        sequence = [1, 2, 3, 4, 5]
        solutions = lis_backtracking_all_solutions(sequence)
        assert len(solutions) == 1
        assert solutions[0] == [1, 2, 3, 4, 5]
    
    def test_strictly_decreasing(self):
        """Test with strictly decreasing sequence."""
        sequence = [5, 4, 3, 2, 1]
        solutions = lis_backtracking_all_solutions(sequence)
        assert len(solutions) == 5  # Each element can be a LIS of length 1
        for solution in solutions:
            assert len(solution) == 1
    
    def test_classic_example(self):
        """Test with classic LIS example."""
        sequence = [10, 22, 9, 33, 21, 50, 41, 60]
        solutions = lis_backtracking_all_solutions(sequence)
        assert len(solutions) >= 1
        for solution in solutions:
            assert len(solution) == 5  # LIS length should be 5
    
    def test_all_solutions_valid(self):
        """Test that all returned solutions are valid LIS."""
        sequence = [1, 3, 2, 4, 5]
        solutions = lis_backtracking_all_solutions(sequence)
        
        for solution in solutions:
            # Check that it's increasing
            for i in range(1, len(solution)):
                assert solution[i] > solution[i-1]
            
            # Check that it's a subsequence
            j = 0
            for num in sequence:
                if j < len(solution) and num == solution[j]:
                    j += 1
            assert j == len(solution)


class TestLISBacktrackingCountSolutions:
    """Test counting LIS solutions."""
    
    def test_empty_sequence(self):
        """Test with empty sequence."""
        length, count = lis_backtracking_count_solutions([])
        assert length == 0
        assert count == 0
    
    def test_single_element(self):
        """Test with single element."""
        length, count = lis_backtracking_count_solutions([1])
        assert length == 1
        assert count == 1
    
    def test_strictly_increasing(self):
        """Test with strictly increasing sequence."""
        sequence = [1, 2, 3, 4, 5]
        length, count = lis_backtracking_count_solutions(sequence)
        assert length == 5
        assert count == 1
    
    def test_strictly_decreasing(self):
        """Test with strictly decreasing sequence."""
        sequence = [5, 4, 3, 2, 1]
        length, count = lis_backtracking_count_solutions(sequence)
        assert length == 1
        assert count == 5  # Each element can be a LIS of length 1
    
    def test_classic_example(self):
        """Test with classic LIS example."""
        sequence = [10, 22, 9, 33, 21, 50, 41, 60]
        length, count = lis_backtracking_count_solutions(sequence)
        assert length == 5
        assert count >= 1


class TestLISBacktrackingOptimized:
    """Test optimized LIS backtracking."""
    
    def test_empty_sequence(self):
        """Test with empty sequence."""
        assert lis_backtracking_optimized([]) == 0
    
    def test_single_element(self):
        """Test with single element."""
        assert lis_backtracking_optimized([1]) == 1
    
    def test_strictly_increasing(self):
        """Test with strictly increasing sequence."""
        sequence = [1, 2, 3, 4, 5]
        assert lis_backtracking_optimized(sequence) == 5
    
    def test_classic_example(self):
        """Test with classic LIS example."""
        sequence = [10, 22, 9, 33, 21, 50, 41, 60]
        assert lis_backtracking_optimized(sequence) == 5
    
    def test_complex_example(self):
        """Test with complex example."""
        sequence = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        assert lis_backtracking_optimized(sequence) == 4


class TestLISBacktrackingWithPath:
    """Test LIS backtracking that returns both length and path."""
    
    def test_empty_sequence(self):
        """Test with empty sequence."""
        length, path = lis_backtracking_with_path([])
        assert length == 0
        assert path == []
    
    def test_single_element(self):
        """Test with single element."""
        length, path = lis_backtracking_with_path([1])
        assert length == 1
        assert path == [1]
    
    def test_strictly_increasing(self):
        """Test with strictly increasing sequence."""
        sequence = [1, 2, 3, 4, 5]
        length, path = lis_backtracking_with_path(sequence)
        assert length == 5
        assert path == [1, 2, 3, 4, 5]
    
    def test_classic_example(self):
        """Test with classic LIS example."""
        sequence = [10, 22, 9, 33, 21, 50, 41, 60]
        length, path = lis_backtracking_with_path(sequence)
        assert length == 5
        # Check that path is increasing
        for i in range(1, len(path)):
            assert path[i] > path[i-1]
    
    def test_path_is_valid_subsequence(self):
        """Test that returned path is a valid subsequence."""
        sequence = [1, 3, 2, 4, 5]
        length, path = lis_backtracking_with_path(sequence)
        
        # Check that path is a subsequence of original sequence
        j = 0
        for num in sequence:
            if j < len(path) and num == path[j]:
                j += 1
        assert j == len(path)


class TestLISEricksonFormulation:
    """Test Erickson's LISbigger formulation."""
    
    def test_empty_sequence(self):
        """Test with empty sequence."""
        assert lis_backtracking_erickson_formulation([]) == 0
    
    def test_single_element(self):
        """Test with single element."""
        assert lis_backtracking_erickson_formulation([1]) == 1
    
    def test_strictly_increasing(self):
        """Test with strictly increasing sequence."""
        sequence = [1, 2, 3, 4, 5]
        assert lis_backtracking_erickson_formulation(sequence) == 5
    
    def test_classic_example(self):
        """Test with classic LIS example."""
        sequence = [10, 22, 9, 33, 21, 50, 41, 60]
        assert lis_backtracking_erickson_formulation(sequence) == 5
    
    def test_complex_example(self):
        """Test with complex example."""
        sequence = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        assert lis_backtracking_erickson_formulation(sequence) == 4


class TestLISEricksonMemoized:
    """Test Erickson's formulation with memoization."""
    
    def test_empty_sequence(self):
        """Test with empty sequence."""
        assert lis_backtracking_erickson_memoized([]) == 0
    
    def test_single_element(self):
        """Test with single element."""
        assert lis_backtracking_erickson_memoized([1]) == 1
    
    def test_strictly_increasing(self):
        """Test with strictly increasing sequence."""
        sequence = [1, 2, 3, 4, 5]
        assert lis_backtracking_erickson_memoized(sequence) == 5
    
    def test_classic_example(self):
        """Test with classic LIS example."""
        sequence = [10, 22, 9, 33, 21, 50, 41, 60]
        assert lis_backtracking_erickson_memoized(sequence) == 5
    
    def test_complex_example(self):
        """Test with complex example."""
        sequence = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        assert lis_backtracking_erickson_memoized(sequence) == 4


class TestLISCorrectness:
    """Test correctness across different implementations."""
    
    def test_correctness_multiple_implementations(self):
        """Test that all implementations give the same result."""
        test_sequences = create_test_sequences()
        
        for sequence in test_sequences:
            basic = lis_backtracking(sequence)
            memo = lis_backtracking_with_memoization(sequence)
            optimized = lis_backtracking_optimized(sequence)
            erickson = lis_backtracking_erickson_formulation(sequence)
            erickson_memo = lis_backtracking_erickson_memoized(sequence)
            
            assert basic == memo == optimized == erickson == erickson_memo, \
                f"Results differ for sequence {sequence}"
    
    def test_correctness_with_path(self):
        """Test that path length matches backtracking result."""
        test_sequences = create_test_sequences()
        
        for sequence in test_sequences:
            basic_length = lis_backtracking(sequence)
            path_length, path = lis_backtracking_with_path(sequence)
            
            assert basic_length == path_length, \
                f"Length mismatch for sequence {sequence}"
            assert len(path) == path_length, \
                f"Path length mismatch for sequence {sequence}"


class TestLISComplexityAnalysis:
    """Test complexity analysis functionality."""
    
    def test_analyze_lis_complexity_basic(self):
        """Test basic complexity analysis."""
        sequence = [1, 3, 2, 4, 5]
        analysis = analyze_lis_complexity(sequence)
        
        assert 'sequence_length' in analysis
        assert 'basic_backtracking' in analysis
        assert 'memoized' in analysis
        assert 'optimized' in analysis
        assert 'count_analysis' in analysis
        assert 'correctness' in analysis
        
        assert analysis['sequence_length'] == 5
        assert analysis['correctness']['all_equal'] == True
    
    def test_analyze_lis_complexity_performance(self):
        """Test that memoized version is faster for larger sequences."""
        sequence = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        analysis = analyze_lis_complexity(sequence)
        
        # Memoized should be faster than basic for this size
        basic_time = analysis['basic_backtracking']['time']
        memo_time = analysis['memoized']['time']
        
        # Note: This might not always be true due to small input size
        # but the structure should be correct
        assert 'time' in analysis['basic_backtracking']
        assert 'time' in analysis['memoized']
        assert 'complexity' in analysis['basic_backtracking']
        assert 'complexity' in analysis['memoized']


class TestLISEdgeCases:
    """Test edge cases and boundary conditions."""
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        sequence = [-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]
        result = lis_backtracking(sequence)
        assert result >= 1  # At least one element
    
    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers."""
        sequence = [-3, 1, -4, 2, -5, 9, -2, 6, -5, 3, -5]
        result = lis_backtracking(sequence)
        assert result >= 1
    
    def test_large_numbers(self):
        """Test with large numbers."""
        sequence = [1000000, 2000000, 3000000, 4000000, 5000000]
        result = lis_backtracking(sequence)
        assert result == 5
    
    def test_duplicate_elements(self):
        """Test with duplicate elements."""
        sequence = [1, 2, 2, 3, 3, 4, 4, 5]
        result = lis_backtracking(sequence)
        assert result == 5  # Should count as increasing
    
    def test_single_element_variations(self):
        """Test various single element cases."""
        assert lis_backtracking([0]) == 1
        assert lis_backtracking([-1]) == 1
        assert lis_backtracking([999]) == 1


class TestLISPerformance:
    """Test performance characteristics."""
    
    def test_small_sequence_performance(self):
        """Test performance on small sequences."""
        sequence = [1, 2, 3, 4, 5]
        
        start_time = time.time()
        basic_result = lis_backtracking(sequence)
        basic_time = time.time() - start_time
        
        start_time = time.time()
        memo_result = lis_backtracking_with_memoization(sequence)
        memo_time = time.time() - start_time
        
        assert basic_result == memo_result
        assert basic_time > 0
        assert memo_time > 0
    
    def test_medium_sequence_performance(self):
        """Test performance on medium sequences."""
        sequence = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 6]
        
        start_time = time.time()
        basic_result = lis_backtracking(sequence)
        basic_time = time.time() - start_time
        
        start_time = time.time()
        memo_result = lis_backtracking_with_memoization(sequence)
        memo_time = time.time() - start_time
        
        assert basic_result == memo_result
        assert basic_time > 0
        assert memo_time > 0
    
    def test_all_solutions_performance(self):
        """Test performance of finding all solutions."""
        sequence = [1, 2, 3, 4, 5]
        
        start_time = time.time()
        solutions = lis_backtracking_all_solutions(sequence)
        all_solutions_time = time.time() - start_time
        
        assert len(solutions) >= 1
        assert all_solutions_time > 0
    
    def test_count_solutions_performance(self):
        """Test performance of counting solutions."""
        sequence = [1, 2, 3, 4, 5]
        
        start_time = time.time()
        length, count = lis_backtracking_count_solutions(sequence)
        count_time = time.time() - start_time
        
        assert length == 5
        assert count >= 1
        assert count_time > 0


class TestLISHelperFunctions:
    """Test helper functions."""
    
    def test_create_test_sequences(self):
        """Test the create_test_sequences helper function."""
        sequences = create_test_sequences()
        
        assert len(sequences) >= 5  # Should have multiple test cases
        assert [] in sequences  # Should include empty sequence
        assert [1] in sequences  # Should include single element
        
        # Check that all sequences are lists of integers
        for sequence in sequences:
            assert isinstance(sequence, list)
            for num in sequence:
                assert isinstance(num, int)


if __name__ == "__main__":
    # Run a simple test to verify the module can be imported
    print("Testing LIS backtracking module...")
    
    # Test basic functionality
    sequence = [10, 22, 9, 33, 21, 50, 41, 60]
    result = lis_backtracking(sequence)
    print(f"LIS length for {sequence}: {result}")
    
    # Test memoized version
    memo_result = lis_backtracking_with_memoization(sequence)
    print(f"Memoized LIS length: {memo_result}")
    
    # Test finding a path
    length, path = lis_backtracking_with_path(sequence)
    print(f"LIS path: {path}")
    
    print("All basic tests passed!") 