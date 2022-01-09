#ifndef DARTS_H
#define DARTS_H

#include <stdint.h>
// coordinate struct 
typedef struct{
  float x,y;
}coordinate_t;

// score function 
uint8_t score(coordinate_t coordinates);

#endif
