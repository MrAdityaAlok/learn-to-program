#include <assert.h>
#include <stdio.h>

void bubble_sort(int *arr, int arrlen, int asc) {
  int swapped;
  for (int i = 0; i < arrlen - 1; i++) {
    swapped = 0;
    for (int j = 0; j < arrlen - i - 1; j++) {
      if ((asc == 1 && arr[j] > arr[j + 1]) ||
          (asc == 0 && arr[j] < arr[j + 1])) {
        int temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
        swapped = 1;
      }
    }
    if (swapped == 0)
      break;
  }
}

void selection_sort(int *arr, int arrlen, int asc) {
  int m;
  for (int i = 0; i < arrlen; i++) {
    m = i;
    for (int j = i + 1; j < arrlen; j++) {
      if ((asc == 1 && arr[j] < arr[m]) || (asc == 0 && arr[j] > arr[m])) {
        m = j;
      }
    }
    if (i == m)
      break;

    int temp = arr[i];
    arr[i] = arr[m];
    arr[m] = temp;
  }
}

void test_bubble_sort() {
  int arr1[] = {5, 1, 4, 2, 8};
  int arr2[] = {};
  int arr3[] = {10};
  int arr4[] = {1, 1, 1, 1, 1};
  int arr5[] = {5, 4, 3, 2, 1};

  bubble_sort(arr1, 5, 1);
  assert(arr1[0] == 1 && arr1[1] == 2 && arr1[2] == 4 && arr1[3] == 5 &&
         arr1[4] == 8);

  bubble_sort(arr1, 5, 0);
  assert(arr1[0] == 8 && arr1[1] == 5 && arr1[2] == 4 && arr1[3] == 2 &&
         arr1[4] == 1);

  bubble_sort(arr2, 0, 1); // Test empty array
  bubble_sort(arr3, 1, 1);
  assert(arr3[0] == 10);

  bubble_sort(arr4, 5, 1);
  assert(arr4[0] == 1 && arr4[1] == 1 && arr4[2] == 1 && arr4[3] == 1 &&
         arr4[4] == 1);

  bubble_sort(arr5, 5, 1);
  assert(arr5[0] == 1 && arr5[1] == 2 && arr5[2] == 3 && arr5[3] == 4 &&
         arr5[4] == 5);

  printf("Bubble sort tests passed!\n");
}

void test_selection_sort() {
  int arr1[] = {5, 1, 4, 2, 8};
  int arr2[] = {};
  int arr3[] = {10};
  int arr4[] = {1, 1, 1, 1, 1};
  int arr5[] = {5, 4, 3, 2, 1};

  selection_sort(arr1, 5, 1);
  assert(arr1[0] == 1 && arr1[1] == 2 && arr1[2] == 4 && arr1[3] == 5 &&
         arr1[4] == 8);

  selection_sort(arr1, 5, 0);
  assert(arr1[0] == 8 && arr1[1] == 5 && arr1[2] == 4 && arr1[3] == 2 &&
         arr1[4] == 1);

  selection_sort(arr2, 0, 1);
  selection_sort(arr3, 1, 1);
  assert(arr3[0] == 10);

  selection_sort(arr4, 5, 1);
  assert(arr4[0] == 1 && arr4[1] == 1 && arr4[2] == 1 && arr4[3] == 1 &&
         arr4[4] == 1);

  selection_sort(arr5, 5, 1);
  assert(arr5[0] == 1 && arr5[1] == 2 && arr5[2] == 3 && arr5[3] == 4 &&
         arr5[4] == 5);

  printf("Selection sort tests passed!\n");
}

int main() {
  test_bubble_sort();
  test_selection_sort();
  return 0;
}
