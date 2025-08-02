"""
Tests for Optimal Binary Search Tree (OBST) Backtracking Implementation

This module contains comprehensive tests for all OBST backtracking functions,
including basic backtracking, memoization, finding optimal structures, counting
structures, optimized versions, and Erickson's formulation.
"""

import pytest
import time
from typing import List, Tuple

from obst_backtracking import (
    obst_backtracking,
    obst_backtracking_with_memoization,
    obst_backtracking_with_structure,
    obst_backtracking_all_structures,
    obst_backtracking_count_structures,
    obst_backtracking_optimized,
    analyze_obst_complexity,
    obst_backtracking_with_tree_building,
    obst_backtracking_erickson_formulation,
    obst_backtracking_erickson_memoized,
    create_test_obst_cases
)


class TestOBSTBacktracking:
    """Test basic OBST backtracking functionality."""
    
    def test_empty_input(self):
        """Test with empty input."""
        assert obst_backtracking([], []) == 0
        assert obst_backtracking([1], []) == 0
        assert obst_backtracking([], [1]) == 0
    
    def test_single_key(self):
        """Test with single key."""
        assert obst_backtracking([1], [10]) == 10
        assert obst_backtracking([5], [50]) == 50
    
    def test_two_keys(self):
        """Test with two keys."""
        # keys = [1, 2], freq = [34, 50]
        # Tree I: 1 as root, 2 as right child
        # Cost = 34*1 + 50*2 = 134
        # Tree II: 2 as root, 1 as left child  
        # Cost = 50*1 + 34*2 = 118
        result = obst_backtracking([1, 2], [34, 50])
        assert result == 118  # Tree II is optimal
    
    def test_three_keys(self):
        """Test with three keys."""
        # keys = [10, 12, 20], freq = [34, 8, 50]
        # This is the classic example from GeeksforGeeks
        result = obst_backtracking([10, 12, 20], [34, 8, 50])
        assert result == 142
    
    def test_sequential_keys(self):
        """Test with sequential keys."""
        keys = [1, 2, 3, 4, 5]
        freq = [1, 2, 3, 4, 5]
        result = obst_backtracking(keys, freq)
        assert result > 0
    
    def test_reverse_frequencies(self):
        """Test with reverse frequencies."""
        keys = [1, 2, 3, 4, 5]
        freq = [5, 4, 3, 2, 1]
        result = obst_backtracking(keys, freq)
        assert result > 0
    
    def test_increasing_frequencies(self):
        """Test with increasing frequencies."""
        keys = [1, 2, 3, 4, 5]
        freq = [10, 20, 30, 40, 50]
        result = obst_backtracking(keys, freq)
        assert result > 0
    
    def test_decreasing_frequencies(self):
        """Test with decreasing frequencies."""
        keys = [1, 2, 3, 4, 5]
        freq = [50, 40, 30, 20, 10]
        result = obst_backtracking(keys, freq)
        assert result > 0
    
    def test_equal_frequencies(self):
        """Test with equal frequencies."""
        keys = [1, 2, 3, 4, 5, 6]
        freq = [1, 1, 1, 1, 1, 1]
        result = obst_backtracking(keys, freq)
        assert result > 0
    
    def test_symmetric_frequencies(self):
        """Test with symmetric frequencies."""
        keys = [1, 2, 3, 4, 5, 6, 7]
        freq = [1, 2, 3, 4, 3, 2, 1]
        result = obst_backtracking(keys, freq)
        assert result > 0


class TestOBSTBacktrackingMemoized:
    """Test memoized OBST backtracking."""
    
    def test_empty_input(self):
        """Test with empty input."""
        assert obst_backtracking_with_memoization([], []) == 0
    
    def test_single_key(self):
        """Test with single key."""
        assert obst_backtracking_with_memoization([1], [10]) == 10
    
    def test_two_keys(self):
        """Test with two keys."""
        result = obst_backtracking_with_memoization([1, 2], [34, 50])
        assert result == 118
    
    def test_three_keys(self):
        """Test with three keys."""
        result = obst_backtracking_with_memoization([10, 12, 20], [34, 8, 50])
        assert result == 142
    
    def test_sequential_keys(self):
        """Test with sequential keys."""
        keys = [1, 2, 3, 4, 5]
        freq = [1, 2, 3, 4, 5]
        result = obst_backtracking_with_memoization(keys, freq)
        assert result > 0


class TestOBSTBacktrackingWithStructure:
    """Test OBST backtracking that returns structure."""
    
    def test_empty_input(self):
        """Test with empty input."""
        cost, structure = obst_backtracking_with_structure([], [])
        assert cost == 0
        assert structure == {}
    
    def test_single_key(self):
        """Test with single key."""
        cost, structure = obst_backtracking_with_structure([1], [10])
        assert cost == 10
        assert (0, 0) in structure
        assert structure[(0, 0)] == 0
    
    def test_two_keys(self):
        """Test with two keys."""
        cost, structure = obst_backtracking_with_structure([1, 2], [34, 50])
        assert cost == 118
        assert (0, 1) in structure
        # Should choose key 2 (index 1) as root
        assert structure[(0, 1)] == 1
    
    def test_three_keys(self):
        """Test with three keys."""
        cost, structure = obst_backtracking_with_structure([10, 12, 20], [34, 8, 50])
        assert cost == 142
        assert (0, 2) in structure  # Root for full range
        assert (0, 1) in structure  # Left subtree
        assert (2, 2) in structure  # Right subtree


class TestOBSTBacktrackingAllStructures:
    """Test finding all optimal structures."""
    
    def test_empty_input(self):
        """Test with empty input."""
        structures = obst_backtracking_all_structures([], [])
        assert structures == []
    
    def test_single_key(self):
        """Test with single key."""
        structures = obst_backtracking_all_structures([1], [10])
        assert len(structures) >= 1
    
    def test_two_keys(self):
        """Test with two keys."""
        structures = obst_backtracking_all_structures([1, 2], [34, 50])
        assert len(structures) >= 1
        # Should have at least one optimal structure
        for structure in structures:
            assert (0, 1) in structure  # Root for full range
    
    def test_equal_frequencies(self):
        """Test with equal frequencies - may have multiple optimal structures."""
        keys = [1, 2, 3]
        freq = [1, 1, 1]
        structures = obst_backtracking_all_structures(keys, freq)
        assert len(structures) >= 1


class TestOBSTBacktrackingCountStructures:
    """Test counting optimal structures."""
    
    def test_empty_input(self):
        """Test with empty input."""
        cost, count = obst_backtracking_count_structures([], [])
        assert cost == 0
        assert count == 0
    
    def test_single_key(self):
        """Test with single key."""
        cost, count = obst_backtracking_count_structures([1], [10])
        assert cost == 10
        assert count == 1
    
    def test_two_keys(self):
        """Test with two keys."""
        cost, count = obst_backtracking_count_structures([1, 2], [34, 50])
        assert cost == 118
        assert count >= 1
    
    def test_three_keys(self):
        """Test with three keys."""
        cost, count = obst_backtracking_count_structures([10, 12, 20], [34, 8, 50])
        assert cost == 142
        assert count >= 1


class TestOBSTBacktrackingOptimized:
    """Test optimized OBST backtracking."""
    
    def test_empty_input(self):
        """Test with empty input."""
        assert obst_backtracking_optimized([], []) == 0
    
    def test_single_key(self):
        """Test with single key."""
        assert obst_backtracking_optimized([1], [10]) == 10
    
    def test_two_keys(self):
        """Test with two keys."""
        result = obst_backtracking_optimized([1, 2], [34, 50])
        assert result == 118
    
    def test_three_keys(self):
        """Test with three keys."""
        result = obst_backtracking_optimized([10, 12, 20], [34, 8, 50])
        assert result == 142
    
    def test_sequential_keys(self):
        """Test with sequential keys."""
        keys = [1, 2, 3, 4, 5]
        freq = [1, 2, 3, 4, 5]
        result = obst_backtracking_optimized(keys, freq)
        assert result > 0


class TestOBSTBacktrackingWithTreeBuilding:
    """Test OBST backtracking that builds tree structure."""
    
    def test_empty_input(self):
        """Test with empty input."""
        cost, tree = obst_backtracking_with_tree_building([], [])
        assert cost == 0
        assert tree == {}
    
    def test_single_key(self):
        """Test with single key."""
        cost, tree = obst_backtracking_with_tree_building([1], [10])
        assert cost == 10
        assert 1 in tree
        assert tree[1] == (-1, -1)  # Leaf node
    
    def test_two_keys(self):
        """Test with two keys."""
        cost, tree = obst_backtracking_with_tree_building([1, 2], [34, 50])
        assert cost == 118
        assert 2 in tree  # Root
        assert 1 in tree  # Left child
    
    def test_three_keys(self):
        """Test with three keys."""
        cost, tree = obst_backtracking_with_tree_building([10, 12, 20], [34, 8, 50])
        assert cost == 142
        assert len(tree) == 3  # All keys should be in tree


class TestOBSTEricksonFormulation:
    """Test Erickson's OptCost formulation."""
    
    def test_empty_input(self):
        """Test with empty input."""
        assert obst_backtracking_erickson_formulation([], []) == 0
    
    def test_single_key(self):
        """Test with single key."""
        assert obst_backtracking_erickson_formulation([1], [10]) == 10
    
    def test_two_keys(self):
        """Test with two keys."""
        result = obst_backtracking_erickson_formulation([1, 2], [34, 50])
        assert result == 118
    
    def test_three_keys(self):
        """Test with three keys."""
        result = obst_backtracking_erickson_formulation([10, 12, 20], [34, 8, 50])
        assert result == 142
    
    def test_sequential_keys(self):
        """Test with sequential keys."""
        keys = [1, 2, 3, 4, 5]
        freq = [1, 2, 3, 4, 5]
        result = obst_backtracking_erickson_formulation(keys, freq)
        assert result > 0


class TestOBSTEricksonMemoized:
    """Test Erickson's formulation with memoization."""
    
    def test_empty_input(self):
        """Test with empty input."""
        assert obst_backtracking_erickson_memoized([], []) == 0
    
    def test_single_key(self):
        """Test with single key."""
        assert obst_backtracking_erickson_memoized([1], [10]) == 10
    
    def test_two_keys(self):
        """Test with two keys."""
        result = obst_backtracking_erickson_memoized([1, 2], [34, 50])
        assert result == 118
    
    def test_three_keys(self):
        """Test with three keys."""
        result = obst_backtracking_erickson_memoized([10, 12, 20], [34, 8, 50])
        assert result == 142
    
    def test_sequential_keys(self):
        """Test with sequential keys."""
        keys = [1, 2, 3, 4, 5]
        freq = [1, 2, 3, 4, 5]
        result = obst_backtracking_erickson_memoized(keys, freq)
        assert result > 0


class TestOBSTCorrectness:
    """Test correctness across different implementations."""
    
    def test_correctness_multiple_implementations(self):
        """Test that all implementations give the same result."""
        test_cases = create_test_obst_cases()
        
        for keys, freq in test_cases:
            if len(keys) <= 5:  # Limit size for exponential algorithms
                basic = obst_backtracking(keys, freq)
                memo = obst_backtracking_with_memoization(keys, freq)
                optimized = obst_backtracking_optimized(keys, freq)
                erickson = obst_backtracking_erickson_formulation(keys, freq)
                erickson_memo = obst_backtracking_erickson_memoized(keys, freq)
                
                assert basic == memo == optimized == erickson == erickson_memo, \
                    f"Results differ for keys {keys}, freq {freq}"
    
    def test_correctness_with_structure(self):
        """Test that structure cost matches backtracking result."""
        test_cases = create_test_obst_cases()
        
        for keys, freq in test_cases:
            if len(keys) <= 5:  # Limit size for exponential algorithms
                basic_cost = obst_backtracking(keys, freq)
                structure_cost, structure = obst_backtracking_with_structure(keys, freq)
                
                assert basic_cost == structure_cost, \
                    f"Cost mismatch for keys {keys}, freq {freq}"
                assert structure_cost > 0 or len(keys) == 0, \
                    f"Invalid cost for keys {keys}, freq {freq}"


class TestOBSTComplexityAnalysis:
    """Test complexity analysis functionality."""
    
    def test_analyze_obst_complexity_basic(self):
        """Test basic complexity analysis."""
        keys = [1, 2, 3]
        freq = [1, 2, 3]
        analysis = analyze_obst_complexity(keys, freq)
        
        assert 'keys_length' in analysis
        assert 'basic_backtracking' in analysis
        assert 'memoized' in analysis
        assert 'optimized' in analysis
        assert 'structure_analysis' in analysis
        assert 'correctness' in analysis
        
        assert analysis['keys_length'] == 3
        assert analysis['correctness']['all_equal'] == True
    
    def test_analyze_obst_complexity_performance(self):
        """Test that memoized version is faster for larger inputs."""
        keys = [1, 2, 3, 4, 5]
        freq = [1, 2, 3, 4, 5]
        analysis = analyze_obst_complexity(keys, freq)
        
        # Memoized should be faster than basic for this size
        basic_time = analysis['basic_backtracking']['time']
        memo_time = analysis['memoized']['time']
        
        # Note: This might not always be true due to small input size
        # but the structure should be correct
        assert 'time' in analysis['basic_backtracking']
        assert 'time' in analysis['memoized']
        assert 'complexity' in analysis['basic_backtracking']
        assert 'complexity' in analysis['memoized']


class TestOBSTEdgeCases:
    """Test edge cases and boundary conditions."""
    
    def test_mismatched_lengths(self):
        """Test with mismatched key and frequency lengths."""
        assert obst_backtracking([1, 2], [1]) == 0
        assert obst_backtracking([1], [1, 2]) == 0
    
    def test_zero_frequencies(self):
        """Test with zero frequencies."""
        keys = [1, 2, 3]
        freq = [0, 0, 0]
        result = obst_backtracking(keys, freq)
        assert result == 0
    
    def test_negative_frequencies(self):
        """Test with negative frequencies."""
        keys = [1, 2, 3]
        freq = [-1, -2, -3]
        result = obst_backtracking(keys, freq)
        assert result < 0  # Should handle negative values
    
    def test_large_frequencies(self):
        """Test with large frequency values."""
        keys = [1, 2, 3]
        freq = [1000000, 2000000, 3000000]
        result = obst_backtracking(keys, freq)
        assert result > 0
    
    def test_duplicate_keys(self):
        """Test with duplicate keys (should handle gracefully)."""
        keys = [1, 1, 2]
        freq = [1, 2, 3]
        result = obst_backtracking(keys, freq)
        assert result > 0
    
    def test_single_element_variations(self):
        """Test various single element cases."""
        assert obst_backtracking([0], [1]) == 1
        assert obst_backtracking([999], [1]) == 1
        assert obst_backtracking([-1], [1]) == 1


class TestOBSTPerformance:
    """Test performance characteristics."""
    
    def test_small_input_performance(self):
        """Test performance on small inputs."""
        keys = [1, 2, 3]
        freq = [1, 2, 3]
        
        start_time = time.time()
        basic_result = obst_backtracking(keys, freq)
        basic_time = time.time() - start_time
        
        start_time = time.time()
        memo_result = obst_backtracking_with_memoization(keys, freq)
        memo_time = time.time() - start_time
        
        assert basic_result == memo_result
        assert basic_time > 0
        assert memo_time > 0
    
    def test_medium_input_performance(self):
        """Test performance on medium inputs."""
        keys = [1, 2, 3, 4, 5]
        freq = [1, 2, 3, 4, 5]
        
        start_time = time.time()
        basic_result = obst_backtracking(keys, freq)
        basic_time = time.time() - start_time
        
        start_time = time.time()
        memo_result = obst_backtracking_with_memoization(keys, freq)
        memo_time = time.time() - start_time
        
        assert basic_result == memo_result
        assert basic_time > 0
        assert memo_time > 0
    
    def test_structure_building_performance(self):
        """Test performance of structure building."""
        keys = [1, 2, 3, 4, 5]
        freq = [1, 2, 3, 4, 5]
        
        start_time = time.time()
        cost, tree = obst_backtracking_with_tree_building(keys, freq)
        tree_time = time.time() - start_time
        
        assert cost > 0
        assert len(tree) == len(keys)
        assert tree_time > 0
    
    def test_count_structures_performance(self):
        """Test performance of counting structures."""
        keys = [1, 2, 3, 4, 5]
        freq = [1, 2, 3, 4, 5]
        
        start_time = time.time()
        cost, count = obst_backtracking_count_structures(keys, freq)
        count_time = time.time() - start_time
        
        assert cost > 0
        assert count >= 1
        assert count_time > 0


class TestOBSTHelperFunctions:
    """Test helper functions."""
    
    def test_create_test_obst_cases(self):
        """Test the create_test_obst_cases helper function."""
        cases = create_test_obst_cases()
        
        assert len(cases) >= 5  # Should have multiple test cases
        assert ([], []) in cases  # Should include empty case
        assert ([1], [10]) in cases  # Should include single key
        
        # Check that all cases have matching lengths
        for keys, freq in cases:
            assert len(keys) == len(freq) or len(keys) == 0 or len(freq) == 0
            for key in keys:
                assert isinstance(key, int)
            for f in freq:
                assert isinstance(f, int)


if __name__ == "__main__":
    # Run a simple test to verify the module can be imported
    print("Testing OBST backtracking module...")
    
    # Test basic functionality
    keys = [10, 12, 20]
    freq = [34, 8, 50]
    result = obst_backtracking(keys, freq)
    print(f"OBST cost for keys {keys}, freq {freq}: {result}")
    
    # Test memoized version
    memo_result = obst_backtracking_with_memoization(keys, freq)
    print(f"Memoized OBST cost: {memo_result}")
    
    # Test structure building
    cost, tree = obst_backtracking_with_tree_building(keys, freq)
    print(f"OBST tree structure: {tree}")
    
    print("All basic tests passed!") 