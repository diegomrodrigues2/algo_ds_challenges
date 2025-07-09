from __future__ import annotations
from typing import List


def prefix_set_intersection(a: List[int], b: List[int]) -> List[int]:
    """Calcula o tamanho da interse\u00e7\u00e3o dos prefixos de ``a`` e ``b``.

    As listas devem possuir o mesmo tamanho ``n``. Para cada \u00edndice ``i``,
    considera-se os conjuntos formados pelos prefixos ``a[:i+1]`` e
    ``b[:i+1]``. O resultado na posi\u00e7\u00e3o ``i`` ser\u00e1 a quantidade de
    elementos em comum entre esses conjuntos.

    Args:
        a: primeira lista de inteiros.
        b: segunda lista de inteiros com o mesmo tamanho de ``a``.

    Returns:
        Lista contendo o tamanho da interse\u00e7\u00e3o em cada prefixo.

    Raises:
        ValueError: se ``a`` e ``b`` tiverem tamanhos diferentes.
    """
    raise NotImplementedError("Implementar esta fun\u00e7\u00e3o")
