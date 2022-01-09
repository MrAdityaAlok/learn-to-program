#include "space_age.h"
#define EARTH_SECONDS_IN_A_YEAR 31557600.0

float year_duration[] = {0.2408467, 0.61519726, 1.0,       1.8808158,
                         11.862615, 29.447498,  84.016846, 164.79132};

float age(planet_t planet, int64_t seconds) {
  float age =
      (float)seconds / (float)(year_duration[planet] * EARTH_SECONDS_IN_A_YEAR);
  return age;
}
