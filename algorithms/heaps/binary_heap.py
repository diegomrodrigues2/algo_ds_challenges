from __future__ import annotations


class BinaryHeap:
    """Min-heap binário simples."""

    def __init__(self) -> None:
        self._data: list[int] = []

    def insert(self, value: int) -> None:
        """Insere um valor na heap."""
        self._data.append(value)

        self._sift_up(self.size() - 1)

    def _sift_up(self, idx):
        """Sobe um elemento até o heap ficar correto."""
        while idx > 0:
            parent = (idx - 1) // 2
            if self._data[idx] < self._data[parent]:
                aux = self._data[idx]
                self._data[idx] = self._data[parent]
                self._data[parent] = aux

                idx = parent
            else:
                break

    def _sift_down(self, idx):
        n = self.size() - 1
        while True:
            left = 2*idx
            right = 2*idx + 1

            smallest = idx

            if left <= n and self._data[left] < self._data[smallest]:
                smallest = left
            if right <= n and self._data[right] < self._data[smallest]:
                smallest = right
            
            if smallest != idx:
                aux = self._data[idx]
                self._data[idx] = self._data[smallest]
                self._data[smallest] = aux

                idx = smallest
            else:
                break

    def extract_min(self) -> int:
        """Remove e retorna o menor valor da heap."""
        if self.size() == 0:
            raise IndexError("Heap is empty")
        
        min = self._data[0]
        
        if self.size() == 1:
            self._data.pop()
        else:
            last = self._data.pop()
            self._data[0] = last
            self._sift_down(0)
        
        return min

    def peek(self) -> int:
        """Retorna o menor valor sem removê-lo."""
        return self._data[0]

    def size(self) -> int:
        """Retorna o número de elementos na heap."""
        return len(self._data)
