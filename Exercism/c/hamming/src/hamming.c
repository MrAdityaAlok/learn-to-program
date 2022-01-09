#include "hamming.h"
#include <string.h>

int64_t compute(const char *lhs, const char *rhs) {
  //  if (strlen(lhs) != strlen(rhs))
  //   return -1;

  int64_t hamming_distance = 0;
  size_t i;
  for (i = 0; lhs[i] && rhs[i]; i++) {
    if (lhs[i] != rhs[i])
      hamming_distance++;
  }
  // if either of them is longer, return -1
  return rhs[i] != '\0' || lhs[i] != '\0' ? -1 : hamming_distance;
}
