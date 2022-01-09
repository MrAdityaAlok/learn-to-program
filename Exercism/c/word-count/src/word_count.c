#include <ctype.h>
#include <stdbool.h>
#include <stdint.h>
#include <string.h>

#include "word_count.h"

static unsigned int unique_word_count = 0;

static uint8_t added_word_position;
bool not_added(const char *word, const word_count_word_t *words) {
  for (unsigned int i = 0; i < unique_word_count; i++) {
    if (strcmp(word, words[i].text) == 0) {
      added_word_position = i;
      return false;
    }
  }
  return true;
}

void add_word(const char *word, word_count_word_t *words) {
  int position = unique_word_count;
  if (not_added(word, words)) {
    strcpy(words[position].text, word);
    words[position].count++;
    unique_word_count++;
  } else {
    words[added_word_position].count++;
  }
}

bool is_delimeter(char ch) { return !(isalnum(ch) || ch == '\''); }

int count_words(const char *sentence, word_count_word_t *words) {
  char scanned_word[MAX_WORD_LENGTH + 1];
  unique_word_count = 0;
  bool word_added = false;
  for (size_t word_length = 0; *sentence; sentence++) {
    if (word_length == 0 && is_delimeter(*sentence))
      continue;
    else if (word_length > MAX_WORD_LENGTH)
      return EXCESSIVE_LENGTH_WORD;

    if (is_delimeter(*sentence)) {
      if (!word_added) {
        if (unique_word_count > MAX_WORDS) return EXCESSIVE_NUMBER_OF_WORDS;
        add_word(scanned_word, words);
        word_added = true;
      }
      word_length = 0;

    } else {
      if (isalnum(*sentence) ||
          (word_length > 0 && *sentence == '\'' && isalnum(*(sentence + 1)))) {
        scanned_word[word_length++] = tolower(*sentence);
        scanned_word[word_length] = '\0';
      }
      word_added = false;
    }
  }
  // when last word ends with \0 , delimeter is never reached
  if (!word_added) {
    add_word(scanned_word, words);
  }
  return unique_word_count;
}
