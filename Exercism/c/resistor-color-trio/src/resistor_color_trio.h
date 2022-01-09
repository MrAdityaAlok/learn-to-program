#ifndef RESISTOR_COLOR_TRIO_H
#define RESISTOR_COLOR_TRIO_H

#include <stdint.h>

typedef enum {
  BLACK,
  BROWN,
  RED,
  ORANGE,
  YELLOW,
  GREEN,
  BLUE,
  VIOLET,
  GREY,
  WHITE
} resistor_band_t;

enum units { OHMS = 1, KILOOHMS = 1000 };

typedef struct resistor_value {
  uint16_t value;
  uint16_t unit;
} resistor_value_t;

resistor_value_t color_code(resistor_band_t *colors);

#endif
