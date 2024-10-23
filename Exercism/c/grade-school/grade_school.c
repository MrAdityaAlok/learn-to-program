#include "grade_school.h"
#include <assert.h>
#include <string.h>

static bool student_exists(roster_t *roster, const char *name) {
  for (size_t i = 0; i < roster->count; i++) {
    if (strcmp(roster->students[i].name, name) == 0) {
      return true;
    }
  }
  return false;
}

// Determine position where we can add this student in roster.
static size_t where_to_add(roster_t *roster, const char *name, size_t grade) {
  size_t index = 0;
  for (; index < roster->count; index++) {
    if (grade == roster->students[index].grade) {
      if (strcmp(name, roster->students[index].name) < 0) {
        break;
      }
    } else if (grade < roster->students[index].grade) {
      break;
    }
  }
  return index;
}

void init_roster(roster_t *roster) {
  if (roster) {
    roster->count = 0;
  }
}

bool add_student(roster_t *roster, const char *name, size_t grade) {
  assert(roster || name);
  if (roster->count >= MAX_STUDENTS || strlen(name) > MAX_NAME_LENGTH ||
      student_exists(roster, name)) {
    return false;
  }

  size_t position = where_to_add(roster, name, grade);
  // Traverse back and shift elements one index forward from the insertion
  // point.
  for (size_t i = roster->count; i > position; i--) {
    roster->students[i] = roster->students[i - 1];
  }

  roster->students[position].grade = grade;
  strcpy(roster->students[position].name, name);
  roster->count++;
  return true;
}

roster_t get_grade(const roster_t *roster, size_t desired_grade) {
  roster_t d_roster = {0};
  assert(roster);
  // Since roster is sorted, we need not traverse farther than
  // roster-->student[i].grade == grade
  for (size_t i = 0;
       roster->students[i].grade <= desired_grade && i < roster->count; i++) {
    if (roster->students[i].grade == desired_grade) {
      d_roster.students[d_roster.count++] = roster->students[i];
    }
  }

  return d_roster;
}

// ============== Note for self: ==============
/* A possible implementation of get_grade would had been to start the loop from
first position of desired_grade (using the following algorithm):
  ==> For this we assume name starts with capital letter.
  ==> "@" comes before "A" in ASCII table,
  ==> hence it should be the first one in that grade.
    size_t i = where_to_add(roster, "@", desired_grade);
But that would still requires traversing to that position(desired_grade), which
we are already doing. Hence no need of that.
*/
