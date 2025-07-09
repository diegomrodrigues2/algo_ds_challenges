from .huffman_decoding import huffman_decoding


def test_basic_decoding():
    code_map = {'a': '0', 'b': '10', 'c': '11'}
    encoded = '011011'
    assert huffman_decoding(encoded, code_map) == 'acac'


def test_complex_decoding():
    code_map = {'a': '0', 'b': '10', 'c': '110', ' ': '111'}
    encoded = '0101101110'
    assert huffman_decoding(encoded, code_map) == 'abc a'


def test_empty_string():
    assert huffman_decoding('', {'a': '0'}) == ''
