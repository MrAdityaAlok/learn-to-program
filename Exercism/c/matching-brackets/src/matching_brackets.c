#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "matching_brackets.h"

static int top = -1;
static char *stack_array = NULL;
static int stack_size = 0;

static void pop() { --top; }

static void *realloc_or_die(void *pointer, size_t size) {
  void *ptr = realloc(pointer, size);
  if (!ptr) {
    free(ptr);
    exit(1);
  }
  return ptr;
}

static void insert(char input) {
  stack_array = realloc_or_die(stack_array, ++stack_size * sizeof(char));
  stack_array[++top] = input;
}

static char peek() { return top != -1 ? stack_array[top] : -1; }

static bool is_opening_bracket(const char input) {
  if (input == '[' || input == '{' || input == '(') return true;
  return false;
}

static bool is_closing_bracket(const char input) {
  if (input == ']' || input == '}' || input == ')') return true;
  return false;
}

static void top_reset() { top = -1; }

static void dismiss() {
  top_reset();
  stack_size = 0;
  if (stack_array) {
    free(stack_array);
    stack_array = NULL;
  }
}

static bool extract_and_insert_brackets(const char *input) {
  bool _return = true;
  for (size_t i = 0; i < strlen(input); i++) {
    if (is_opening_bracket(input[i])) {
      insert(input[i]);
    } else if (is_closing_bracket(input[i])) {
      if (input[i] - peek() == 1 || input[i] - peek() == 2) {
        pop();
      } else {
        top_reset();  // when breaks in between
        _return = false;
        break;
      }
    }
  }

  if (top != -1) _return = false;
  dismiss();
  return _return;
}

bool is_paired(const char *input) {
  if (!input || !*input) return true;
  return extract_and_insert_brackets(input);
}
