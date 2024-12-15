#include <assert.h>
#include <stdio.h>

int gcd1(int dividend, int divisor) {
  // clang-format off
  if (divisor == 0) return dividend;
  int remainder = dividend % divisor;
  if (remainder == 0) return divisor;
  // clang-format on
  return gcd1(divisor, remainder);
}

int gcd2(int dividend, int divisor) {
  // clang-format off
  if (divisor == 0) return dividend;
  // clang-format on
  int remainder = dividend % divisor;
  while (remainder != 0) {
    dividend = divisor;
    divisor = remainder;
    remainder = dividend % divisor;
  }
  return divisor;
}

int main(void) {
  int a, b;

  printf("Enter two numbers: ");
  scanf("%d %d", &a, &b);

  printf("gcd1(%d,%d) = %d\n", a, b, gcd1(a, b));
  printf("gcd2(%d,%d) = %d\n", a, b, gcd2(a, b));
}
