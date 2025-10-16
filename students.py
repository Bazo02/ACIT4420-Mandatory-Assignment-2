# students.py
class Students:
    """Class to manage a list of students' information."""

    def __init__(self):
        self.students = []

    def add_student(self, name, email, course, preferred_time="08:00"):
        """Add a student with name, email, course, and preferred reminder time."""
        student = {
            'name': name,
            'email': email,
            'course': course,
            'preferred_time': preferred_time
        }
        self.students.append(student)

    def remove_student(self, email):
        """Remove a student by email."""
        self.students = [s for s in self.students if s['email'] != email]

    def get_students(self):
        """Retrieve the list of students."""
        return self.students
