from __future__ import annotations


def range_sum(nums: list[int], queries: list[tuple[int, int]]) -> list[int]:
    """Calcula a soma dos elementos em intervalos especificados.

    Cada par ``(inicio, fim)`` em ``queries`` representa um intervalo inclusivo
    sobre ``nums``. A função deve retornar a soma de cada intervalo na mesma
    ordem fornecida.

    Args:
        nums: lista de inteiros.
        queries: lista de tuplas ``(inicio, fim)`` onde ``0 ≤ inicio ≤ fim < len(nums)``.

    Returns:
        Lista de inteiros com as somas de cada intervalo.
    """
    raise NotImplementedError("Implementar esta função")
