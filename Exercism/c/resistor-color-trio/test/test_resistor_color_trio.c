#include "../src/resistor_color_trio.h"
#include "vendor/unity.h"

void setUp(void) {}

void tearDown(void) {}

static void test_orange_orange_black(void) {
  resistor_value_t actual =
      color_code((resistor_band_t[]){ORANGE, ORANGE, BLACK});
  TEST_ASSERT_EQUAL_UINT16(33, actual.value);
  TEST_ASSERT_EQUAL(OHMS, actual.unit);
}

static void test_blue_grey_brown(void) {
  resistor_value_t actual = color_code((resistor_band_t[]){BLUE, GREY, BROWN});
  TEST_ASSERT_EQUAL_UINT16(680, actual.value);
  TEST_ASSERT_EQUAL(OHMS, actual.unit);
}

static void test_red_black_red(void) {
  resistor_value_t actual = color_code((resistor_band_t[]){RED, BLACK, RED});
  TEST_ASSERT_EQUAL_UINT16(2, actual.value);
  TEST_ASSERT_EQUAL(KILOOHMS, actual.unit);
}

static void test_green_brown_orange(void) {
  resistor_value_t actual =
      color_code((resistor_band_t[]){GREEN, BROWN, ORANGE});
  TEST_ASSERT_EQUAL_UINT16(51, actual.value);
  TEST_ASSERT_EQUAL(KILOOHMS, actual.unit);
}

static void test_yellow_violet_yellow(void) {
  resistor_value_t actual =
      color_code((resistor_band_t[]){YELLOW, VIOLET, YELLOW});
  TEST_ASSERT_EQUAL_UINT16(470, actual.value);
  TEST_ASSERT_EQUAL(KILOOHMS, actual.unit);
}

int main(void) {
  UnityBegin("test/test_resistor_color_trio.c");

  RUN_TEST(test_orange_orange_black);
  RUN_TEST(test_blue_grey_brown);
  RUN_TEST(test_red_black_red);
  RUN_TEST(test_green_brown_orange);
  RUN_TEST(test_yellow_violet_yellow);

  return UnityEnd();
}
