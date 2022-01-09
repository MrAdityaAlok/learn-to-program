#include <stdio.h>

#include "resistor_color.h"

static resistor_band_t band[] = {BLACK, BROWN, RED,    ORANGE, YELLOW,
                                 GREEN, BLUE,  VIOLET, GREY,   WHITE};

const resistor_band_t* colors(void) { return band; }

uint16_t color_code(resistor_band_t color) { return color; }
