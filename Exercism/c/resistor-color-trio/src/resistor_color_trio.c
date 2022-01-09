#include <math.h>

#include "resistor_color_trio.h"

resistor_value_t color_code(resistor_band_t *colors) {
  int value = (colors[0] * 10 + colors[1]) * pow(10, colors[2]);
  int unit = value >= KILOOHMS ? KILOOHMS : OHMS;
  return (resistor_value_t){.value = unit == OHMS ? value : value / KILOOHMS,
                            .unit = unit};
}
