#include "grains.h"

uint64_t square(uint8_t index) {
  if (index < 1 || index > 64) return 0;
  //  return pow(2, index - 1);
  return 1ULL << (index - 1);
}

uint64_t total(void) {
  return ~0ULL; /** ULL since type is guaranteed to have at least 64 bits.
                 * unsigned long has at least 32 bits
                 *
                 * ~0ULL same as highest value of unsigned long(i.e atleast
                 * 2^64)
                 * '~a' on unsigned integer type value gives : [highest value of
                 * that data type  -(a+1)] this is due to 2's complement
                 * #https://www.programiz.com/c-programming/bitwise-operators
                 * we can also use : -1, instead
                 * reason : fact that unsigned types use a modulo-arithmetic
                 * (i.e. they "wrap around")
                 */

  /**
   *Some other implementations of total()
   *
   *return 18446744073709551615;
  return 0xFFFFFFFFFFFFFFFF;
  return (1ULL << 63) * 2 - 1;
  return (1ULL << 32 << 32) - 1;
  return (2ULL << 63) - 1;
  return UINT64_MAX;
  return ~UINT64_C(0);
  return UINT64_C(-1);
  return 2 * square(64) - 1;
  *
  * because the return type is uint64_t you could rely on the implicit
  conversion to that type and write return ULLONG_MAX; return -1; *With
  optimizations turned on the compiler will generate the same instructions for
  all of them
  */
}
