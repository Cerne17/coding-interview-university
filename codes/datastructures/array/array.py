class DynamicArray:
    def __init__(self, initial_capacity: int = 2):
        self._data = [None] * initial_capacity
        self._size = 0
        self.capacity = initial_capacity

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if not 0 <= index < self._size:
            raise IndexError('Index out of range')
        return self._data[index]

    def __setitem__(self, index, value):
        if not 0 <= index < self._size:
            raise IndexError('Index out of range.')
        self._data[index] = value

    def _resize(self, new_capacity):
        new_data = self._data + [None] * (new_capacity - self.capacity)
        self._data = new_data
        self.capacity = new_capacity

    def append(self, value):
        if self._size == self.capacity:
            self._resize(self.capacity * 2)
        self._data[self._size] = value
        self._size += 1

    def remove(self, index):
        if not 0 <= index < self._size:
            raise IndexError('Index out of range.')
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._size -= 1

    def __str__(self):
        return str([self._data[i] for i in range(self._size)])


if __name__ == "__main__":
    arr = DynamicArray()

    arr.append(10)
    arr.append(20)
    arr.append(30)

    print("Array:", arr)  # Output: Array: [10, 20, 30]

    arr.remove(1)

    # Output: Array após remoção: [10, 30]
    print("Array após remoção:", arr)

    arr.append(40)
    arr.append(50)

    # Output: Array após adições: [10, 30, 40, 50]
    print("Array após adições:", arr)

    print("Elemento no índice 2:", arr[2])  # Output: Elemento no índice 2: 40

    arr[2] = 100
    # Output: Array após atualização: [10, 30, 100, 50]
    print("Array após atualização:", arr)
