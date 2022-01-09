#include <string.h>
#include <time.h>

#include "meetup.h"

static int day_of_week_to_num(const char *day_of_week) {
  if (!strcmp(day_of_week, "Monday"))
    return 1;
  else if (!strcmp(day_of_week, "Tuesday"))
    return 2;
  else if (!strcmp(day_of_week, "Wednesday"))
    return 3;
  else if (!strcmp(day_of_week, "Thursday"))
    return 4;
  else if (!strcmp(day_of_week, "Friday"))
    return 5;
  else if (!strcmp(day_of_week, "Saturday"))
    return 6;
  else if (!strcmp(day_of_week, "Sunday"))
    return 0;
  else
    return -1;
}

static int is_leap_year(int year) {
  if ((year % 400 == 0) || ((year % 4 == 0) && (year % 100 != 0))) return 1;
  return 0;
}

static int days_in_month(int month, int year) {
  int days[12] = {
      31, is_leap_year(year) ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  return days[month];
}

// int dayofweek(int d, int m, int y) {
// Sakamoto's method from
// https://en.m.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Methods_in_computer_code
// y -= m < 3;
//  return (y  + y / 4 - y / 100 + y / 400 + "-bed=pen+mad."[m] + d) % 7;
//}

int meetup_day_of_month(unsigned int year, unsigned int month, const char *week,
                        const char *day_of_week) {
  struct tm start = {
      .tm_year = year - 1900,
      .tm_mon = month - 1};  // when initializing this way, everything else is
                             // initialized with a default value (int to 0),
                             // other wise given a random value.

  int day_to_find = day_of_week_to_num(day_of_week);

  if (!strcmp(week, "first"))
    start.tm_mday = 1;
  else if (!strcmp(week, "second"))
    start.tm_mday = 8;
  else if (!strcmp(week, "third"))
    start.tm_mday = 15;
  else if (!strcmp(week, "fourth"))
    start.tm_mday = 22;
  else if (!strcmp(week, "teenth"))
    start.tm_mday = 13;
  else if (!strcmp(week, "fifth")) {
    if (!is_leap_year(year) && month == 2) return -1;
    start.tm_mday = 29;
  } else if (!strcmp(week, "last")) {
    start.tm_mday = days_in_month(start.tm_mon, year);
    mktime(&start);  // to get day on that date
    int diff = start.tm_wday - day_to_find;
    start.tm_mday -= diff < 0 ? diff + 7 : diff;  // when day_to_find is behind
  }

  mktime(&start);
  int diff = day_to_find - start.tm_wday;
  start.tm_mday += diff < 0 ? diff + 7 : diff;

  return start.tm_mday;
}
