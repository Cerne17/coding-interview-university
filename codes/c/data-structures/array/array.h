#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int *data;    // Pointer to the data
  int size;     // The current size of the array
  int capacity; // The max capacity of the array
} DynamicArray;
