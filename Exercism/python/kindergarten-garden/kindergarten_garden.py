class Garden:
    STUDENTS = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Fred",
        "Ginny",
        "Harriet",
        "Ileana",
        "Joseph",
        "Kincaid",
        "Larry",
    ]

    PLANTS = {"V": "Violets", "R": "Radishes", "C": "Clover", "G": "Grass"}

    def __init__(self, diagram, students=None):
        """Receives diagram of garden and determines its owner.

        :param diagram: two row list containing the plants from left-to-right
        starting with the row nearest to the windows
        :type diagram: str

        :param students: An optional list of student names
        :type student: list"""
        if students:
            self.STUDENTS = sorted(students)
        self.diagram = diagram.split("\n")

        # all plants of a student in a tuple
        # eg. ('VCRG'),('GGRC')  when self.diagram = ["VCGG\nRGRC"]
        student_plants = zip(
            *[iter(self.diagram[0])] * 2 + [iter(self.diagram[1])] * 2
        )

        self.student_to_plant_mapping = dict(
            zip(self.STUDENTS, student_plants)
        )

    def plants(self, student):
        """Takes a student name and returns a list of his/her plants.

        :param student: Name of student whoes plants is to be returned
        :type student: str"""
        return list(
            map(self.PLANTS.get, self.student_to_plant_mapping[student])
        )


# How line 36 works?
#
# First, two list of, two, same iter object is created by [iter(self.diagram[INDEX])]*2
# then , both are added to a single list
# Now unpacking is done of the list,
# which is supplied as four distinct arguments to zip function

# NOTE: unpacking *(asterisk) prefix  has less precedence than suffix or infix *,
# therefore it is executed after addition of two lists

# Example of arguments passed after unpacking:
# zip(
#        <str_iterator object at 0x7214b798e0>,
#        <str_iterator object at 0x7214b798e0>,
#        <str_iterator object at 0x7214b79730>,
#        <str_iterator object at 0x7214b79730>
#    )

# Notice that first and last two iterator objects are same,
# hence no element is accessed twice.
