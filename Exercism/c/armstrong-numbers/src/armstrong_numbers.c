#include "armstrong_numbers.h"
#include <math.h>

bool is_armstrong_number(int candidate){  
  if (candidate < 0) return false; 
  // count no of digits 
  int digits = (candidate == 0) ? 1 : log10(candidate)+1;

  int sum_of_square_of_digits = 0;
  
  for(int num=candidate; num != 0; num /=10){
    sum_of_square_of_digits += pow(num % 10, digits);
  }
  
  return (sum_of_square_of_digits == candidate);
}
