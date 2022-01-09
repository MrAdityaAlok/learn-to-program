#include "darts.h"
#include <math.h>

uint8_t score(coordinate_t coordinates){
  uint8_t score;
  float distance_from_origin = sqrt(coordinates.x * coordinates.x + coordinates.y * coordinates.y);

  if(distance_from_origin <= 1.0)
    score = 10;
  else if (distance_from_origin <= 5.0)
    score = 5;
  else if (distance_from_origin <= 10.0)
    score = 1;
  else
   score = 0;
  return score;
}
