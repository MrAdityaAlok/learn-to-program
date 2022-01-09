#include "difference_of_squares.h"

unsigned int sum_of_squares(unsigned int number) {
  return number * (number + 1) * (2 * number + 1) / 6;
}

unsigned square_of_sum(unsigned int number) {
  return number * number * (number + 1) * (number + 1) / 4;
}

unsigned int difference_of_squares(unsigned int number) {
  return square_of_sum(number) - sum_of_squares(number);
}
