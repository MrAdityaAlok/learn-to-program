#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int linear_search(int *arr, int v, int arrlen) {
  for (int i = 0; i < arrlen; i++) {
    if (arr[i] == v) {
      return i;
    }
  }
  return -1;
}

// Assume sorted (ascending order)
int binary_search(int *arr, int v, int arrlen) {
  int min_index = 0, max_index = arrlen - 1, mid;
  while (min_index <= max_index) {
    mid = (max_index + min_index) / 2;
    if (arr[mid] == v)
      return mid;
    if (arr[mid] > v)
      max_index = mid - 1;
    else
      min_index = mid + 1;
  }
  return -1;
}

void test_linear_search() {
  int arr1[] = {1, 2, 3, 4, 5};
  int arr2[] = {};
  int arr3[] = {10};
  int arr4[] = {1, 1, 1, 1, 1}; // Test with duplicate values

  assert(linear_search(arr1, 3, 5) == 2);
  assert(linear_search(arr1, 6, 5) == -1);
  assert(linear_search(arr2, 1, 0) == -1);
  assert(linear_search(arr3, 10, 1) == 0);
  assert(linear_search(arr3, 11, 1) == -1);
  assert(linear_search(arr4, 1, 5) == 0); // Check first occurrence of duplicate

  printf("Linear search tests passed!\n");
}

void test_binary_search() {
  int arr1[] = {1, 2, 3, 4, 5};
  int arr2[] = {};
  int arr3[] = {10};
  int arr4[] = {2, 4, 6, 8, 10, 12};
  int arr5[] = {1, 1, 1, 1, 1}; // Test with all same values
  int arr6[] = {1, 2, 2, 2, 3}; // Test with some duplicates

  assert(binary_search(arr1, 3, 5) == 2);
  assert(binary_search(arr1, 6, 5) == -1);
  assert(binary_search(arr2, 1, 0) == -1);
  assert(binary_search(arr3, 10, 1) == 0);
  assert(binary_search(arr3, 11, 1) == -1);
  assert(binary_search(arr4, 8, 6) == 3);
  assert(binary_search(arr4, 1, 6) == -1);
  assert(binary_search(arr4, 13, 6) == -1);
  printf("Returned: %d\n", binary_search(arr4, 2, 6));
  assert(binary_search(arr4, 2, 6) == 0);
  assert(binary_search(arr4, 12, 6) == 5);
  assert(binary_search(arr5, 1, 5) == 2); // Should return *an* index where 1 is
  assert(binary_search(arr6, 2, 5) >= 1 &&
         binary_search(arr6, 2, 5) <= 3); // Test duplicate existence

  // More extensive testing with larger arrays and random numbers
  const int large_array_size = 1000;
  int *large_arr = (int *)malloc(large_array_size * sizeof(int));
  srand(time(NULL)); // Seed the random number generator

  for (int i = 0; i < large_array_size; i++) {
    large_arr[i] = i * 2; // Create a sorted array
  }

  for (int i = 0; i < 100; i++) { // Test 100 random values
    int random_index = rand() % large_array_size;
    int value = large_arr[random_index];
    assert(binary_search(large_arr, value, large_array_size) == random_index);
    int not_present = (rand() % large_array_size) * 2 +
                      1; // Generate odd values that are not present
    assert(binary_search(large_arr, not_present, large_array_size) == -1);
  }

  free(large_arr);

  printf("Binary search tests passed!\n");
}

int main() {
  test_linear_search();
  test_binary_search();
  return 0;
}
