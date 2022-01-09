#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "rna_transcription.h"

static char complement_of(char nucleotide) {
  switch (nucleotide) {
    case 'A':
      return 'U';
    case 'T':
      return 'A';
    case 'G':
      return 'C';
    case 'C':
      return 'G';
    default:
      return 0;
  }
}
static void *malloc_or_die(unsigned long size) {
  void *ptr = malloc(size);
  if (!ptr) exit(1);  // memory will be freed by OS
  return ptr;
}

char *to_rna(const char *dna) {
  if (!dna || !*dna) return "";

  char *rna = malloc_or_die((strlen(dna) + 1) * sizeof(char));

  size_t i = 0;
  for (; dna[i]; i++) {
    rna[i] = complement_of(dna[i]);
  }
  rna[i] = '\0';
  return rna;
}
