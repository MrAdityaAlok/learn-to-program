#include <math.h>

#include "square_root.h"

float estimate(float S); // function prototype for gcc

float estimate(float S) {
  /* a good estimate (According to a wikipedia article which I found
   * here):
   * https://www.physicsforums.com/threads/seed-values-for-estimating-square-roots.445749/)
   */
  int D = log10(S) + 1;
  int even_or_odd = D % 2 == 0;
  float n = even_or_odd ? (D - 2) / 2 : (D - 1) / 2;
  float estimated = even_or_odd ? 6 * pow(10, n) : 2 * pow(10, n);

  return estimated;
}
uint16_t square_root(float S) {
  /* Using Babylonian
   * method(https://en.m.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method)
   */
  float x = estimate(S);
  float y = S / x;
  while (fabs(x - y) > ACCURACY) {
    x = (x + y) * 0.5;
    y = S / x;
  }
  return x;
}
