class School:
    def __init__(self):
        """Creates a roster for the school, given student's names along with there grade."""
        self._db = {}

    def add_student(self, name, grade):
        """Add student to the school databsase."""
        self._db.setdefault(grade, []).append(name)
        self._db[grade].sort()

    def roster(self):
        """Creates a roster for the school."""
        students_list = []
        for grades in sorted(self._db):
            students_list.extend(self._db[grades])
        return students_list

    def grade(self, grade_number):
        """Returns students of respective grade."""
        return self._db.get(grade_number, []).copy()
