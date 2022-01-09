#include <ctype.h>
#include <stdbool.h>
#include <stddef.h>
#include <string.h>

#include "pangram.h"

bool is_pangram(const char *sentence) {
  // if NULL of empty ""
  if (!sentence || !*sentence) return false;
  bool check[26] = {false};
  for (; *sentence; sentence++) {
    if (isalpha((unsigned char)*sentence))
      check[tolower(*sentence) - 'a'] = true;
  }
  for (size_t i = 0; i < 26; i++) {
    if (!check[i])  // if false i.e any letter not present
      return false;
  }
  return true;
}
