#ifndef GRADE_SCHOOL_H
#define GRADE_SCHOOL_H

#include <stdbool.h>
#include <stddef.h>

#define MAX_NAME_LENGTH 20
#define MAX_STUDENTS 20

typedef struct {
  size_t grade;
  char name[MAX_NAME_LENGTH];
} student_t;

typedef struct {
  size_t count;
  student_t students[MAX_STUDENTS];
} roster_t;

void init_roster(roster_t *roster);
bool add_student(roster_t *roster, const char *name, size_t grade);
roster_t get_grade(const roster_t *roster, size_t desired_grade);

#endif
