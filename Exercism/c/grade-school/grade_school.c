#include "grade_school.h"
#include <string.h>

static bool student_exists(roster_t *roster, char *name) {
  for (size_t i = 0; i < roster->count; i++) {
    if (strcmp(roster->students[i].name, name) == 0) {
      return true;
    }
  }
  return false;
}

// Determine position where we can add this student in roster.
static uint8_t where_to_add(roster_t *roster, char *name, uint8_t grade) {
  size_t i = 0;
  for (; i < roster->count; i++) {
    if (grade == roster->students[i].grade) {
      // Same grade students needs to be inserted in dictionary order.
      if (strcmp(name, roster->students[i].name) < 0)
        break; // Break if this name comes before student[i].name in dictionary.
    } else if (grade < roster->students[i].grade) {
      break; // Brake if this grade is less than next student's grade.
    }
  }
  return i;
}

void init_roster(roster_t *roster) {
  if (roster) // Check for null pointer.
    roster->count = 0;
}

bool add_student(roster_t *roster, char *name, uint8_t grade) {
  if (!roster || !name)
    return false; // Null pointers!!!
  if (roster->count >= MAX_STUDENTS || student_exists(roster, name))
    return false; // They already exists or MAX_STUDENTS reached.

  // They do not exist, add.

  uint8_t position = where_to_add(roster, name, grade);
  // Inserting in between roaster.
  if (position < roster->count) { // position can max be roster->count.
    // Traverse back and shift elements one position forward from the insertion
    // point.
    for (size_t i = roster->count; i > position; i--) {
      roster->students[i] = roster->students[i - 1];
    }
  }

  roster->students[position].grade = grade;
  strcpy(roster->students[position].name, name);
  roster->count++;
  return true;
}

roster_t get_grade(roster_t *roster, uint8_t desired_grade) {
  roster_t g_roster = {0};
  for (size_t i = 0; i < roster->count; i++) {
    if (roster->students[i].grade == desired_grade) {
      g_roster.students[g_roster.count] = roster->students[i];
      g_roster.count++;
    }
  }
  return g_roster;
}
