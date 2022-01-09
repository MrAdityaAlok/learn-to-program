#include "isogram.h"
#include <string.h>
#include <ctype.h>

bool is_isogram(const char phrase[]){
  if(phrase == NULL)
    return false;

  bool check[26]  = {false};
  for (size_t i = 0; phrase[i]; i++) {
    unsigned char unsigned_value = phrase[i];
    
    if(isalpha(unsigned_value)){
      char lower_case = tolower(unsigned_value);
      
      if(check[lower_case - 'a'])
        return false;
      else 
        check[lower_case - 'a'] = true;
    }
  }
  return true;
}
