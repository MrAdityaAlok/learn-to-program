#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "acronym.h"

static void *realloc_or_die(void *pointer, size_t size) {
  void *ptr = realloc(pointer, size);
  if (!ptr) exit(1);
  return ptr;
  /**
   * since the operating system will release the allocated memory after the
   * program has finished we could simplify that by omitting the free():
   */
}

char *abbreviate(const char *phrase) {
  // !phrase for NULL and !*phrase for empty string, a.k.a ""
  if (!phrase || !*phrase) return NULL;

  char *abbreviated = NULL;
  abbreviated =
      realloc_or_die(abbreviated, (strlen(phrase) + 3) / 2 * sizeof(char));
  bool reading = true;
  unsigned int index = 0;
  for (; *phrase; phrase++) {
    unsigned char ch = *phrase;
    // if reading and char is a letter then append to abbreviated
    if (reading && isalpha(ch))
      abbreviated[index++] =
          toupper(ch);  // length++ first uses value then increments by 1

    reading = !isalpha(ch) && ch != '\'';
  }
  abbreviated[index] = '\0';
  return abbreviated;
}
