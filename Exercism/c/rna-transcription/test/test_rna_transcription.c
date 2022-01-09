#include <stdlib.h>

#include "../src/rna_transcription.h"
#include "vendor/unity.h"

void setUp(void) {}

void tearDown(void) {}

static void check_transcription(const char *dna, const char *expected) {
  char *rna = to_rna(dna);
  TEST_ASSERT_EQUAL_STRING(expected, rna);
  // free(rna);
}

static void test_empty_rna_sequence(void) { check_transcription("", ""); }

static void test_rna_complement_of_cytosine_is_guanine(void) {
  check_transcription("C", "G");
}

static void test_rna_complement_of_guanine_is_cytosine(void) {
  check_transcription("G", "C");
}

static void test_rna_complement_of_thymine_is_adenine(void) {
  check_transcription("T", "A");
}

static void test_rna_complement_of_adenine_is_uracil(void) {
  check_transcription("A", "U");
}

static void test_rna_complement(void) {
  check_transcription("ACGTGGTCTTAA", "UGCACCAGAAUU");
}

int main(void) {
  UnityBegin("test/test_rna_transcription.c");

  RUN_TEST(test_empty_rna_sequence);
  RUN_TEST(test_rna_complement_of_cytosine_is_guanine);
  RUN_TEST(test_rna_complement_of_guanine_is_cytosine);
  RUN_TEST(test_rna_complement_of_thymine_is_adenine);
  RUN_TEST(test_rna_complement_of_adenine_is_uracil);
  RUN_TEST(test_rna_complement);

  return UnityEnd();
}
