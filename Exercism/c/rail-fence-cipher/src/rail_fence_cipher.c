/**
 * ALGORITHM idea taken from
 * https://www.sersc.org/journals/index.php/IJFGCN/article/view/657
 */
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

#include "rail_fence_cipher.h"

char *encode_decode(char *input, size_t rails, uint8_t to_encode) {
  size_t length = strlen(input);
  char *output = malloc((length + 1) * sizeof(char));
  size_t j = 0, repeat = 2 * (rails - 1), current_rail = 0;
  for (size_t i = 0; i < length; i++) {
    if (to_encode)
      output[i] = input[j];
    else
      output[j] = input[i];

    if (current_rail == 0 ||
        current_rail == rails - 1)  // if first or last rails
      j += repeat;
    else if (j % repeat < rails)  // when going down
      j += repeat - (2 * current_rail);
    else  // wgen going up
      j += current_rail * 2;

    if (j >= length) j = ++current_rail;
  }
  output[length] = '\0';
  return output;
}

char *encode(char *text, size_t rails) { return encode_decode(text, rails, 1); }

char *decode(char *text, size_t rails) { return encode_decode(text, rails, 0); }
