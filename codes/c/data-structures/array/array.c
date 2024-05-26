#include "array.h"
#include <stdio.h>
#include <stdlib.h>

void initArray(DynamicArray *arr, int initialCapacity) {
  arr->data = (int *)malloc(initialCapacity * sizeof(int));
  arr->size = 0;
  arr->capacity = initialCapacity;
}

void resizeArray(DynamicArray *arr, int newCapacity) {
  int *temp = (int *)realloc(arr->data, newCapacity * sizeof(int));
  if (temp) {
    arr->data = temp;
    arr->capacity = newCapacity;
  } else {
    printf("Could not resize the array.");
    exit(1);
  }
}

void addElement(DynamicArray *arr, int element) {
  if (arr->size == arr->capacity) {
    resizeArray(arr, arr->capacity * 2);
  }
  arr->data[arr->size++] = element;
}

void removeElement(DynamicArray *arr, int index) {
  if (index < 0 || index > arr->size - 1) {
    printf("Error: Index out of Boundaries.");
    exit(1);
  }
  for (int i = index; i < arr->size - 1; i++) {
    arr->data[i] = arr->data[i + 1];
  }
  arr->size--;
}

void deleteArray(DynamicArray *arr) {
  arr->data = NULL;
  arr->size = 0;
  arr->capacity = 0;
}

int main() {
  DynamicArray arr;
  initArray(&arr, 2);

  addElement(&arr, 10);
  addElement(&arr, 20);
  addElement(&arr, 30);

  printf("Array: ");
  for (int i = 0; i < arr.size; i++) {
    printf("%d ", arr.data[i]);
  }
  printf("\n");

  removeElement(&arr, 1);

  printf("Array after deletion: ");
  for (int i = 0; i < arr.size; i++) {
    printf("%d ", arr.data[i]);
  }
  printf("\n");

  deleteArray(&arr);
  return 0;
}
